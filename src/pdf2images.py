import locale

import ghostscript


def pdf2png(input_pdf_file, output_file_path):
    print(input_pdf_file, output_file_path)
    args_list = ["-q",
                 "-dQUIET", "-dSAFER", "-dBATCH", "-dNOPAUSE", "-dNOPROMPT", "-dMaxBitmap=900000000",
                 "-dAlignToPixels=0", "-dGridFitTT=2", "-sDEVICE=pnggray", "-r1200", "-dDownScaleFactor=4",
                 "-dTextAlphaBits=4", "-dGraphicsAlphaBits=4", "-dUseTrimBox", "-dQFactor=1",
                 "-dColorConversionStrategy=/Gray", "-dProcessColorModel=/DeviceGray",
                 "-sOutputFile=" + output_file_path + "/%d.png", input_pdf_file]
    try:
        # arguments have to be bytes, encode them
        encoding = locale.getpreferredencoding()
        args = [str(a).encode(encoding) for a in args_list]

        gs = ghostscript.Ghostscript(*args)
        gs.exit()
    except ghostscript.GhostscriptError as e:
        print(e)


if __name__ == '__main__':
    pdf2png(r'C:\EA\OCR\2022\TEST\AC\S05A20P25.pdf', r'C:\EA\OCR\2022\TEST\AC\S05A20P25')
