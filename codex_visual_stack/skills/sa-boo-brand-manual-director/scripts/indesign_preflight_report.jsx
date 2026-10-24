(function () {
    if (app.documents.length === 0) {
        throw new Error("Open an InDesign manual before running.");
    }

    var doc = app.activeDocument;
    var outputFolder;
    try {
        outputFolder = doc.filePath;
    } catch (error) {
        outputFolder = Folder.desktop;
    }
    var baseName = doc.name.replace(/\.[^.]+$/, "");
    var jsonFile = File(
        outputFolder.fsName + "/" + baseName + "_preflight.json"
    );
    var textFile = File(
        outputFolder.fsName + "/" + baseName + "_preflight.txt"
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

    var overset = [];
    var badLinks = [];
    var badFonts = [];
    var emptyPages = [];
    var index;

    for (var pageIndex = 0; pageIndex < doc.pages.length; pageIndex++) {
        var page = doc.pages[pageIndex];
        var hasVisibleContent = false;
        for (index = 0; index < page.textFrames.length; index++) {
            if (page.textFrames[index].overflows) {
                overset.push({
                    page: page.name,
                    frame_index: index,
                    frame_id: page.textFrames[index].id,
                    label: page.textFrames[index].label
                });
            }
            if (String(page.textFrames[index].contents).replace(/\s/g, "") !== "") {
                hasVisibleContent = true;
            }
        }
        if (page.allGraphics.length > 0) {
            hasVisibleContent = true;
        }
        if (!hasVisibleContent) {
            emptyPages.push(page.name);
        }
    }

    for (index = 0; index < doc.links.length; index++) {
        if (doc.links[index].status !== LinkStatus.NORMAL) {
            badLinks.push({
                name: doc.links[index].name,
                status: doc.links[index].status.toString(),
                path: safe(function () {
                    return doc.links[index].filePath;
                }, "")
            });
        }
    }

    for (index = 0; index < doc.fonts.length; index++) {
        if (doc.fonts[index].status !== FontStatus.INSTALLED) {
            badFonts.push({
                family: safe(function () {
                    return doc.fonts[index].fontFamily;
                }, ""),
                style: safe(function () {
                    return doc.fonts[index].fontStyleName;
                }, ""),
                status: doc.fonts[index].status.toString()
            });
        }
    }

    var errors = overset.length + badLinks.length + badFonts.length;
    var report = {
        document_name: doc.name,
        document_path: safe(function () {
            return doc.fullName.fsName;
        }, ""),
        page_count: doc.pages.length,
        spread_count: doc.spreads.length,
        overset_frames: overset,
        bad_links: badLinks,
        missing_or_substituted_fonts: badFonts,
        possible_empty_pages: emptyPages,
        structural_error_count: errors,
        status: errors === 0 ? "PASS" : "FAIL",
        note: "Empty pages are warnings and require visual review."
    };

    jsonFile.encoding = "UTF-8";
    jsonFile.open("w");
    jsonFile.write(stringify(report));
    jsonFile.close();

    var lines = [
        "InDesign Brand Manual Preflight",
        "Document: " + doc.name,
        "Pages: " + doc.pages.length,
        "Spreads: " + doc.spreads.length,
        "",
        "Overset frames: " + overset.length,
        "Bad links: " + badLinks.length,
        "Missing/substituted fonts: " + badFonts.length,
        "Possible empty pages: " + emptyPages.length,
        "",
        "Status: " + report.status,
        "Note: Empty pages require visual review."
    ];
    textFile.encoding = "UTF-8";
    textFile.open("w");
    textFile.write(lines.join("\n"));
    textFile.close();
}());
