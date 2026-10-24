#import <AppKit/AppKit.h>
#import <PDFKit/PDFKit.h>

static int Fail(NSString *message, int code) {
    fprintf(stderr, "%s\n", message.UTF8String);
    return code;
}

int main(int argc, const char *argv[]) {
    @autoreleasepool {
        if (argc != 4) {
            return Fail(@"usage: render_pdf_pages INPUT.pdf OUTPUT_DIR DPI", 64);
        }

        NSString *inputPath = [NSString stringWithUTF8String:argv[1]];
        NSString *outputPath = [NSString stringWithUTF8String:argv[2]];
        double dpi = strtod(argv[3], NULL);
        if (dpi <= 0) {
            return Fail(@"DPI must be a positive number", 64);
        }

        NSURL *inputURL = [NSURL fileURLWithPath:inputPath];
        PDFDocument *document = [[PDFDocument alloc] initWithURL:inputURL];
        if (document == nil) {
            return Fail([NSString stringWithFormat:@"Unable to open PDF: %@", inputPath], 66);
        }

        NSError *directoryError = nil;
        BOOL madeDirectory = [[NSFileManager defaultManager]
            createDirectoryAtPath:outputPath
            withIntermediateDirectories:YES
            attributes:nil
            error:&directoryError];
        if (!madeDirectory) {
            return Fail(
                [NSString stringWithFormat:@"Unable to create output directory: %@", directoryError],
                73
            );
        }

        double scale = dpi / 72.0;
        for (NSInteger index = 0; index < document.pageCount; index++) {
            PDFPage *page = [document pageAtIndex:index];
            if (page == nil) {
                return Fail(
                    [NSString stringWithFormat:@"Unable to read PDF page %ld", (long)index + 1],
                    65
                );
            }

            NSRect bounds = [page boundsForBox:kPDFDisplayBoxMediaBox];
            NSInteger width = MAX(1, (NSInteger)ceil(bounds.size.width * scale));
            NSInteger height = MAX(1, (NSInteger)ceil(bounds.size.height * scale));
            NSBitmapImageRep *bitmap = [[NSBitmapImageRep alloc]
                initWithBitmapDataPlanes:NULL
                pixelsWide:width
                pixelsHigh:height
                bitsPerSample:8
                samplesPerPixel:4
                hasAlpha:YES
                isPlanar:NO
                colorSpaceName:NSDeviceRGBColorSpace
                bytesPerRow:0
                bitsPerPixel:0];
            if (bitmap == nil) {
                return Fail(@"Unable to allocate PDF page bitmap", 70);
            }

            NSGraphicsContext *graphicsContext =
                [NSGraphicsContext graphicsContextWithBitmapImageRep:bitmap];
            if (graphicsContext == nil) {
                return Fail(@"Unable to create PDF graphics context", 70);
            }

            [NSGraphicsContext saveGraphicsState];
            [NSGraphicsContext setCurrentContext:graphicsContext];
            CGContextRef context = graphicsContext.CGContext;
            CGContextSetRGBFillColor(context, 1.0, 1.0, 1.0, 1.0);
            CGContextFillRect(context, CGRectMake(0, 0, width, height));
            CGContextScaleCTM(context, scale, scale);
            CGContextTranslateCTM(context, -bounds.origin.x, -bounds.origin.y);
            [page drawWithBox:kPDFDisplayBoxMediaBox toContext:context];
            [NSGraphicsContext restoreGraphicsState];

            NSData *png = [bitmap
                representationUsingType:NSBitmapImageFileTypePNG
                properties:@{}];
            if (png == nil) {
                return Fail(@"Unable to encode PDF page as PNG", 70);
            }
            NSString *filename = [NSString stringWithFormat:@"page-%ld.png", (long)index + 1];
            NSString *destination = [outputPath stringByAppendingPathComponent:filename];
            if (![png writeToFile:destination atomically:YES]) {
                return Fail(
                    [NSString stringWithFormat:@"Unable to write %@", destination],
                    74
                );
            }
        }

        printf(
            "{\"status\":\"rendered\",\"page_count\":%ld,\"backend\":\"macos-pdfkit\"}\n",
            (long)document.pageCount
        );
        return 0;
    }
}
