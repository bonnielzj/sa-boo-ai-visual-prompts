#target illustrator

(function () {
    if (app.documents.length === 0) {
        throw new Error("Open an Illustrator identity source before running.");
    }

    var doc = app.activeDocument;
    var outputFolder;
    try {
        outputFolder = doc.fullName.parent;
    } catch (error) {
        outputFolder = Folder.desktop;
    }

    function round(value, digits) {
        var factor = Math.pow(10, digits || 3);
        return Math.round(value * factor) / factor;
    }

    function ptToMm(value) {
        return round(value * 25.4 / 72, 3);
    }

    function boundsInfo(bounds) {
        var width = bounds[2] - bounds[0];
        var height = bounds[1] - bounds[3];
        return {
            left_pt: round(bounds[0], 4),
            top_pt: round(bounds[1], 4),
            right_pt: round(bounds[2], 4),
            bottom_pt: round(bounds[3], 4),
            width_mm: ptToMm(width),
            height_mm: ptToMm(height),
            aspect_ratio: height === 0 ? null : round(width / height, 5)
        };
    }

    function safe(getter, fallback) {
        try {
            return getter();
        } catch (error) {
            return fallback;
        }
    }

    function colorInfo(color) {
        if (!color) {
            return null;
        }
        var info = {typename: color.typename};
        if (color.typename === "CMYKColor") {
            info.cmyk = [
                round(color.cyan, 2),
                round(color.magenta, 2),
                round(color.yellow, 2),
                round(color.black, 2)
            ];
        } else if (color.typename === "RGBColor") {
            info.rgb = [
                round(color.red, 2),
                round(color.green, 2),
                round(color.blue, 2)
            ];
        } else if (color.typename === "GrayColor") {
            info.gray = round(color.gray, 2);
        } else if (color.typename === "SpotColor") {
            info.spot_name = color.spot.name;
            info.tint = round(color.tint, 2);
            info.alternate = colorInfo(color.spot.color);
        }
        return info;
    }

    function layerInfo(layer, depth) {
        var children = [];
        for (var index = 0; index < layer.layers.length; index++) {
            children.push(layerInfo(layer.layers[index], depth + 1));
        }
        return {
            name: layer.name,
            visible: !!layer.visible,
            locked: !!layer.locked,
            printable: !!layer.printable,
            depth: depth,
            direct_page_items: layer.pageItems.length,
            child_layers: children
        };
    }

    function stringify(value) {
        if (value === null || value === undefined) {
            return "null";
        }
        if (typeof value === "number" || typeof value === "boolean") {
            return String(value);
        }
        if (typeof value === "string") {
            return "\"" + value
                .replace(/\\/g, "\\\\")
                .replace(/"/g, "\\\"")
                .replace(/\r/g, "\\r")
                .replace(/\n/g, "\\n")
                .replace(/\t/g, "\\t") + "\"";
        }
        var parts = [];
        var index;
        if (value instanceof Array) {
            for (index = 0; index < value.length; index++) {
                parts.push(stringify(value[index]));
            }
            return "[" + parts.join(",") + "]";
        }
        for (var key in value) {
            if (value.hasOwnProperty(key)) {
                parts.push(stringify(key) + ":" + stringify(value[key]));
            }
        }
        return "{" + parts.join(",") + "}";
    }

    var artboards = [];
    var index;
    for (index = 0; index < doc.artboards.length; index++) {
        artboards.push({
            index: index,
            name: doc.artboards[index].name,
            bounds: boundsInfo(doc.artboards[index].artboardRect)
        });
    }

    var layers = [];
    for (index = 0; index < doc.layers.length; index++) {
        layers.push(layerInfo(doc.layers[index], 0));
    }

    var swatches = [];
    for (index = 0; index < doc.swatches.length; index++) {
        swatches.push({
            name: safe(function () {
                return doc.swatches[index].name;
            }, "UNREADABLE_" + index),
            color: safe(function () {
                return colorInfo(doc.swatches[index].color);
            }, null)
        });
    }

    var textFrames = [];
    for (index = 0; index < doc.textFrames.length; index++) {
        textFrames.push({
            index: index,
            name: doc.textFrames[index].name || "",
            contents: doc.textFrames[index].contents,
            bounds: safe(function () {
                return boundsInfo(doc.textFrames[index].visibleBounds);
            }, null)
        });
    }

    var report = {
        document_name: doc.name,
        document_path: safe(function () {
            return doc.fullName.fsName;
        }, ""),
        color_space: String(doc.documentColorSpace),
        ruler_units: safe(function () {
            return String(doc.rulerUnits);
        }, "UNAVAILABLE"),
        counts: {
            artboards: doc.artboards.length,
            layers: doc.layers.length,
            page_items: doc.pageItems.length,
            paths: doc.pathItems.length,
            compound_paths: doc.compoundPathItems.length,
            groups: doc.groupItems.length,
            raster_items: doc.rasterItems.length,
            placed_items: doc.placedItems.length,
            text_frames: doc.textFrames.length,
            symbols: doc.symbols.length,
            swatches: doc.swatches.length
        },
        artboards: artboards,
        layers: layers,
        swatches: swatches,
        text_frames: textFrames,
        cautions: [
            "Measurements are evidence, not approved usage rules.",
            "Source presence does not establish hierarchy.",
            "Detected color values are not official without approval."
        ]
    };

    var baseName = doc.name.replace(/\.[^.]+$/, "");
    var outputFile = File(
        outputFolder.fsName + "/" + baseName + "_identity_audit.json"
    );
    outputFile.encoding = "UTF-8";
    outputFile.open("w");
    outputFile.write(stringify(report));
    outputFile.close();
}());
