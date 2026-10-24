(function () {
    if (app.documents.length === 0) {
        throw new Error("Open an InDesign template before running.");
    }

    var doc = app.activeDocument;
    var outputFolder;
    try {
        outputFolder = doc.filePath;
    } catch (error) {
        outputFolder = Folder.desktop;
    }
    var baseName = doc.name.replace(/\.[^.]+$/, "");
    var reportFile = File(
        outputFolder.fsName + "/" + baseName + "_template_audit.json"
    );
    var previewFile = File(
        outputFolder.fsName + "/" + baseName + "_template_preview.pdf"
    );

    function safe(getter, fallback) {
        try {
            return getter();
        } catch (error) {
            return fallback;
        }
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

    function boundsArray(bounds) {
        var values = [];
        for (var index = 0; index < bounds.length; index++) {
            values.push(Number(bounds[index]));
        }
        return values;
    }

    var fonts = [];
    var index;
    for (index = 0; index < doc.fonts.length; index++) {
        fonts.push({
            family: safe(function () {
                return doc.fonts[index].fontFamily;
            }, ""),
            style: safe(function () {
                return doc.fonts[index].fontStyleName;
            }, ""),
            status: safe(function () {
                return doc.fonts[index].status.toString();
            }, "UNKNOWN")
        });
    }

    var links = [];
    for (index = 0; index < doc.links.length; index++) {
        links.push({
            name: doc.links[index].name,
            status: safe(function () {
                return doc.links[index].status.toString();
            }, "UNKNOWN"),
            path: safe(function () {
                return doc.links[index].filePath;
            }, "")
        });
    }

    var pages = [];
    for (var pageIndex = 0; pageIndex < doc.pages.length; pageIndex++) {
        var page = doc.pages[pageIndex];
        var textFrames = [];
        var rectangles = [];
        for (index = 0; index < page.textFrames.length; index++) {
            var textFrame = page.textFrames[index];
            textFrames.push({
                index: index,
                id: textFrame.id,
                label: textFrame.label,
                bounds: boundsArray(textFrame.geometricBounds),
                contents: safe(function () {
                    return textFrame.contents;
                }, ""),
                paragraph_style: safe(function () {
                    return textFrame.paragraphs[0].appliedParagraphStyle.name;
                }, ""),
                font: safe(function () {
                    return String(textFrame.characters[0].appliedFont);
                }, ""),
                point_size: safe(function () {
                    return Number(textFrame.characters[0].pointSize);
                }, 0)
            });
        }
        for (index = 0; index < page.rectangles.length; index++) {
            var rectangle = page.rectangles[index];
            rectangles.push({
                index: index,
                id: rectangle.id,
                label: rectangle.label,
                bounds: boundsArray(rectangle.geometricBounds),
                graphics: rectangle.allGraphics.length,
                fill: safe(function () {
                    return rectangle.fillColor.name;
                }, "")
            });
        }
        pages.push({
            page: page.name,
            applied_master: safe(function () {
                return page.appliedMaster.name;
            }, ""),
            text_frames: textFrames,
            rectangles: rectangles
        });
    }

    var paragraphStyles = [];
    for (index = 0; index < doc.allParagraphStyles.length; index++) {
        paragraphStyles.push(doc.allParagraphStyles[index].name);
    }
    var characterStyles = [];
    for (index = 0; index < doc.allCharacterStyles.length; index++) {
        characterStyles.push(doc.allCharacterStyles[index].name);
    }
    var swatches = [];
    for (index = 0; index < doc.swatches.length; index++) {
        swatches.push(doc.swatches[index].name);
    }

    var originalHorizontalUnits = doc.viewPreferences.horizontalMeasurementUnits;
    var originalVerticalUnits = doc.viewPreferences.verticalMeasurementUnits;
    doc.viewPreferences.horizontalMeasurementUnits = MeasurementUnits.POINTS;
    doc.viewPreferences.verticalMeasurementUnits = MeasurementUnits.POINTS;
    var pageWidthPoints = Number(doc.documentPreferences.pageWidth);
    var pageHeightPoints = Number(doc.documentPreferences.pageHeight);
    doc.viewPreferences.horizontalMeasurementUnits = originalHorizontalUnits;
    doc.viewPreferences.verticalMeasurementUnits = originalVerticalUnits;

    var report = {
        document_name: doc.name,
        document_path: safe(function () {
            return doc.fullName.fsName;
        }, ""),
        page_count: doc.pages.length,
        spread_count: doc.spreads.length,
        original_horizontal_units: String(originalHorizontalUnits),
        original_vertical_units: String(originalVerticalUnits),
        page_width_points: pageWidthPoints,
        page_height_points: pageHeightPoints,
        page_width_mm: Math.round(pageWidthPoints * 25.4 / 72 * 1000) / 1000,
        page_height_mm: Math.round(pageHeightPoints * 25.4 / 72 * 1000) / 1000,
        facing_pages: !!doc.documentPreferences.facingPages,
        master_spreads: doc.masterSpreads.length,
        fonts: fonts,
        links: links,
        paragraph_styles: paragraphStyles,
        character_styles: characterStyles,
        swatches: swatches,
        pages: pages
    };

    reportFile.encoding = "UTF-8";
    reportFile.open("w");
    reportFile.write(stringify(report));
    reportFile.close();

    var preset = null;
    for (index = 0; index < app.pdfExportPresets.length; index++) {
        var name = app.pdfExportPresets[index].name;
        if (
            name.indexOf("High Quality") >= 0 ||
            name.indexOf("High-Quality") >= 0 ||
            name.indexOf("高质量") >= 0
        ) {
            preset = app.pdfExportPresets[index];
            break;
        }
    }
    if (preset) {
        doc.exportFile(ExportFormat.PDF_TYPE, previewFile, false, preset);
    } else {
        doc.exportFile(ExportFormat.PDF_TYPE, previewFile, false);
    }
}());
