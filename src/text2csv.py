import bs4

html_text = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title></title>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type"/>
    <meta content="tesseract v5.0.0-alpha.20210811" name="ocr-system"/>
    <meta content="ocr_page ocr_carea ocr_par ocr_line ocrx_word ocrp_wconf" name="ocr-capabilities"/>
</head>
<body>
<div class="ocr_page" id="page_1"
     title='image "C:\EA\OCR\2022\TEST\AC20\S05A20P3\3\3.png"; bbox 0 0 2479 3508; ppageno 0'>
    <div class="ocr_carea" id="block_1_1" title="bbox 116 36 911 72">
        <p class="ocr_par" id="par_1_1" lang="eng" title="bbox 116 36 911 72">
<span class="ocr_header" id="line_1_1"
      title="bbox 116 36 911 72; baseline 0 -8; x_size 36; x_descenders 8; x_ascenders 8">
<span class="ocrx_word" id="word_1_1" title="bbox 116 36 284 72; x_wconf 96">Assembly</span>
<span class="ocrx_word" id="word_1_2" title="bbox 296 36 511 72; x_wconf 96">Constituency</span>
<span class="ocrx_word" id="word_1_3" title="bbox 524 36 568 64; x_wconf 96">No</span>
<span class="ocrx_word" id="word_1_4" title="bbox 581 36 639 64; x_wconf 96">and</span>
<span class="ocrx_word" id="word_1_5" title="bbox 654 36 749 64; x_wconf 73">Name</span>
<span class="ocrx_word" id="word_1_6" title="bbox 750 32 765 76; x_wconf 73">:</span>
<span class="ocrx_word" id="word_1_7" title="bbox 783 36 911 64; x_wconf 92">20-Priol</span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_2" title="bbox 118 124 1067 154">
        <p class="ocr_par" id="par_1_2" lang="eng" title="bbox 118 124 1067 154">
<span class="ocr_header" id="line_1_2"
      title="bbox 118 124 1067 154; baseline 0 -6; x_size 30; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_8" title="bbox 118 124 224 148; x_wconf 95">Section</span>
<span class="ocrx_word" id="word_1_9" title="bbox 238 124 274 148; x_wconf 96">No</span>
<span class="ocrx_word" id="word_1_10" title="bbox 287 124 338 148; x_wconf 96">and</span>
<span class="ocrx_word" id="word_1_11" title="bbox 352 124 432 148; x_wconf 88">Name</span>
<span class="ocrx_word" id="word_1_12" title="bbox 447 130 450 148; x_wconf 18">:</span>
<span class="ocrx_word" id="word_1_13" title="bbox 467 124 564 148; x_wconf 90">1-Near</span>
<span class="ocrx_word" id="word_1_14" title="bbox 575 124 759 148; x_wconf 90">Cremotorium</span>
<span class="ocrx_word" id="word_1_15" title="bbox 773 124 965 154; x_wconf 90">Cristianwada,</span>
<span class="ocrx_word" id="word_1_16" title="bbox 981 124 1067 154; x_wconf 91">Orgao</span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_3" title="bbox 1952 36 2234 64">
        <p class="ocr_par" id="par_1_3" lang="eng" title="bbox 1952 36 2234 64">
<span class="ocr_header" id="line_1_3"
      title="bbox 1952 36 2234 64; baseline 0 0; x_size 33.377777; x_descenders 5.3777776; x_ascenders 6">
<span class="ocrx_word" id="word_1_17" title="bbox 1952 36 2026 64; x_wconf 96">Part</span>
<span class="ocrx_word" id="word_1_18" title="bbox 2038 36 2180 64; x_wconf 91">number</span>
<span class="ocrx_word" id="word_1_19" title="bbox 2194 42 2200 64; x_wconf 91">:</span>
<span class="ocrx_word" id="word_1_20" title="bbox 2215 36 2234 64; x_wconf 97">3</span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_4" title="bbox 102 208 2361 213">
        <p class="ocr_par" id="par_1_4" lang="eng" title="bbox 102 208 2361 213">
<span class="ocr_line" id="line_1_4"
      title="bbox 102 208 2361 213; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_21" title="bbox 102 208 2361 213; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_5" title="bbox 657 276 839 280">
        <p class="ocr_par" id="par_1_5" lang="eng" title="bbox 657 276 839 280">
<span class="ocr_line" id="line_1_5"
      title="bbox 657 276 839 280; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_22" title="bbox 657 276 839 280; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_6" title="bbox 657 276 661 496">
        <p class="ocr_par" id="par_1_6" lang="eng" title="bbox 657 276 661 496">
<span class="ocr_line" id="line_1_6"
      title="bbox 657 276 661 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_23" title="bbox 657 276 661 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_7" title="bbox 835 276 839 496">
        <p class="ocr_par" id="par_1_7" lang="eng" title="bbox 835 276 839 496">
<span class="ocr_line" id="line_1_7"
      title="bbox 835 276 839 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_24" title="bbox 835 276 839 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_8" title="bbox 657 492 839 496">
        <p class="ocr_par" id="par_1_8" lang="eng" title="bbox 657 492 839 496">
<span class="ocr_line" id="line_1_8"
      title="bbox 657 492 839 496; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_25" title="bbox 657 492 839 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_9" title="bbox 1410 276 1592 280">
        <p class="ocr_par" id="par_1_9" lang="eng" title="bbox 1410 276 1592 280">
<span class="ocr_line" id="line_1_9"
      title="bbox 1410 276 1592 280; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_26" title="bbox 1410 276 1592 280; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_10" title="bbox 1410 276 1415 496">
        <p class="ocr_par" id="par_1_10" lang="eng" title="bbox 1410 276 1415 496">
<span class="ocr_line" id="line_1_10"
      title="bbox 1410 276 1415 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_27" title="bbox 1410 276 1415 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_11" title="bbox 1588 276 1592 496">
        <p class="ocr_par" id="par_1_11" lang="eng" title="bbox 1588 276 1592 496">
<span class="ocr_line" id="line_1_11"
      title="bbox 1588 276 1592 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_28" title="bbox 1588 276 1592 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_12" title="bbox 1410 492 1592 496">
        <p class="ocr_par" id="par_1_12" lang="eng" title="bbox 1410 492 1592 496">
<span class="ocr_line" id="line_1_12"
      title="bbox 1410 492 1592 496; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_29" title="bbox 1410 492 1592 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_13" title="bbox 2163 276 2345 280">
        <p class="ocr_par" id="par_1_13" lang="eng" title="bbox 2163 276 2345 280">
<span class="ocr_line" id="line_1_13"
      title="bbox 2163 276 2345 280; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_30" title="bbox 2163 276 2345 280; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_14" title="bbox 2163 276 2168 496">
        <p class="ocr_par" id="par_1_14" lang="eng" title="bbox 2163 276 2168 496">
<span class="ocr_line" id="line_1_14"
      title="bbox 2163 276 2168 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_31" title="bbox 2163 276 2168 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_15" title="bbox 2341 276 2345 496">
        <p class="ocr_par" id="par_1_15" lang="eng" title="bbox 2341 276 2345 496">
<span class="ocr_line" id="line_1_15"
      title="bbox 2341 276 2345 496; baseline 0 0; x_size 110; x_descenders -55; x_ascenders 55">
<span class="ocrx_word" id="word_1_32" title="bbox 2341 276 2345 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_16" title="bbox 2163 492 2345 496">
        <p class="ocr_par" id="par_1_16" lang="eng" title="bbox 2163 492 2345 496">
<span class="ocr_line" id="line_1_16"
      title="bbox 2163 492 2345 496; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_33" title="bbox 2163 492 2345 496; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_17" title="bbox 102 500 2361 510">
        <p class="ocr_par" id="par_1_17" lang="eng" title="bbox 102 500 2361 510">
<span class="ocr_line" id="line_1_17"
      title="bbox 102 500 2361 510; baseline 0 0; x_size 5; x_descenders -2.5; x_ascenders 2.5">
<span class="ocrx_word" id="word_1_34" title="bbox 102 500 2361 510; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_18" title="bbox 657 575 839 580">
        <p class="ocr_par" id="par_1_18" lang="eng" title="bbox 657 575 839 580">
<span class="ocr_line" id="line_1_18"
      title="bbox 657 575 839 580; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_35" title="bbox 657 575 839 580; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_19" title="bbox 657 276 661 795">
        <p class="ocr_par" id="par_1_19" lang="eng" title="bbox 657 276 661 795">
<span class="ocr_line" id="line_1_19"
      title="bbox 657 276 661 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_36" title="bbox 657 276 661 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_20" title="bbox 835 276 839 795">
        <p class="ocr_par" id="par_1_20" lang="eng" title="bbox 835 276 839 795">
<span class="ocr_line" id="line_1_20"
      title="bbox 835 276 839 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_37" title="bbox 835 276 839 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_21" title="bbox 657 791 839 795">
        <p class="ocr_par" id="par_1_21" lang="eng" title="bbox 657 791 839 795">
<span class="ocr_line" id="line_1_21"
      title="bbox 657 791 839 795; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_38" title="bbox 657 791 839 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_22" title="bbox 1410 575 1592 580">
        <p class="ocr_par" id="par_1_22" lang="eng" title="bbox 1410 575 1592 580">
<span class="ocr_line" id="line_1_22"
      title="bbox 1410 575 1592 580; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_39" title="bbox 1410 575 1592 580; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_23" title="bbox 1410 276 1415 795">
        <p class="ocr_par" id="par_1_23" lang="eng" title="bbox 1410 276 1415 795">
<span class="ocr_line" id="line_1_23"
      title="bbox 1410 276 1415 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_40" title="bbox 1410 276 1415 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_24" title="bbox 1588 276 1592 795">
        <p class="ocr_par" id="par_1_24" lang="eng" title="bbox 1588 276 1592 795">
<span class="ocr_line" id="line_1_24"
      title="bbox 1588 276 1592 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_41" title="bbox 1588 276 1592 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_25" title="bbox 1410 791 1592 795">
        <p class="ocr_par" id="par_1_25" lang="eng" title="bbox 1410 791 1592 795">
<span class="ocr_line" id="line_1_25"
      title="bbox 1410 791 1592 795; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_42" title="bbox 1410 791 1592 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_26" title="bbox 2163 575 2345 580">
        <p class="ocr_par" id="par_1_26" lang="eng" title="bbox 2163 575 2345 580">
<span class="ocr_line" id="line_1_26"
      title="bbox 2163 575 2345 580; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_43" title="bbox 2163 575 2345 580; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_27" title="bbox 2163 276 2168 795">
        <p class="ocr_par" id="par_1_27" lang="eng" title="bbox 2163 276 2168 795">
<span class="ocr_line" id="line_1_27"
      title="bbox 2163 276 2168 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_44" title="bbox 2163 276 2168 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_28" title="bbox 2341 276 2345 795">
        <p class="ocr_par" id="par_1_28" lang="eng" title="bbox 2341 276 2345 795">
<span class="ocr_line" id="line_1_28"
      title="bbox 2341 276 2345 795; baseline 0 0; x_size 259.5; x_descenders -129.75; x_ascenders 129.75">
<span class="ocrx_word" id="word_1_45" title="bbox 2341 276 2345 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_29" title="bbox 2163 791 2345 795">
        <p class="ocr_par" id="par_1_29" lang="eng" title="bbox 2163 791 2345 795">
<span class="ocr_line" id="line_1_29"
      title="bbox 2163 791 2345 795; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_46" title="bbox 2163 791 2345 795; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_30" title="bbox 102 799 2361 810">
        <p class="ocr_par" id="par_1_30" lang="eng" title="bbox 102 799 2361 810">
<span class="ocr_line" id="line_1_30"
      title="bbox 102 799 2361 810; baseline 0 0; x_size 5.5; x_descenders -2.75; x_ascenders 2.75">
<span class="ocrx_word" id="word_1_47" title="bbox 102 799 2361 810; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_31" title="bbox 657 875 839 879">
        <p class="ocr_par" id="par_1_31" lang="eng" title="bbox 657 875 839 879">
<span class="ocr_line" id="line_1_31"
      title="bbox 657 875 839 879; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_48" title="bbox 657 875 839 879; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_32" title="bbox 657 276 661 1100">
        <p class="ocr_par" id="par_1_32" lang="eng" title="bbox 657 276 661 1100">
<span class="ocr_line" id="line_1_32"
      title="bbox 657 276 661 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_49" title="bbox 657 276 661 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_33" title="bbox 835 276 839 1100">
        <p class="ocr_par" id="par_1_33" lang="eng" title="bbox 835 276 839 1100">
<span class="ocr_line" id="line_1_33"
      title="bbox 835 276 839 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_50" title="bbox 835 276 839 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_34" title="bbox 1410 875 1592 879">
        <p class="ocr_par" id="par_1_34" lang="eng" title="bbox 1410 875 1592 879">
<span class="ocr_line" id="line_1_34"
      title="bbox 1410 875 1592 879; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_51" title="bbox 1410 875 1592 879; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_35" title="bbox 1410 276 1415 1100">
        <p class="ocr_par" id="par_1_35" lang="eng" title="bbox 1410 276 1415 1100">
<span class="ocr_line" id="line_1_35"
      title="bbox 1410 276 1415 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_52" title="bbox 1410 276 1415 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_36" title="bbox 1588 276 1592 1100">
        <p class="ocr_par" id="par_1_36" lang="eng" title="bbox 1588 276 1592 1100">
<span class="ocr_line" id="line_1_36"
      title="bbox 1588 276 1592 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_53" title="bbox 1588 276 1592 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_37" title="bbox 2163 875 2345 879">
        <p class="ocr_par" id="par_1_37" lang="eng" title="bbox 2163 875 2345 879">
<span class="ocr_line" id="line_1_37"
      title="bbox 2163 875 2345 879; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_54" title="bbox 2163 875 2345 879; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_38" title="bbox 2163 276 2168 1100">
        <p class="ocr_par" id="par_1_38" lang="eng" title="bbox 2163 276 2168 1100">
<span class="ocr_line" id="line_1_38"
      title="bbox 2163 276 2168 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_55" title="bbox 2163 276 2168 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_39" title="bbox 2341 276 2345 1100">
        <p class="ocr_par" id="par_1_39" lang="eng" title="bbox 2341 276 2345 1100">
<span class="ocr_line" id="line_1_39"
      title="bbox 2341 276 2345 1100; baseline 0 0; x_size 412; x_descenders -206; x_ascenders 206">
<span class="ocrx_word" id="word_1_56" title="bbox 2341 276 2345 1100; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_40" title="bbox 102 1096 2361 1101">
        <p class="ocr_par" id="par_1_40" lang="eng" title="bbox 102 1096 2361 1101">
<span class="ocr_line" id="line_1_40"
      title="bbox 102 1096 2361 1101; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_57" title="bbox 102 1096 2361 1101; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_41" title="bbox 102 1105 2361 1110">
        <p class="ocr_par" id="par_1_41" lang="eng" title="bbox 102 1105 2361 1110">
<span class="ocr_line" id="line_1_41"
      title="bbox 102 1105 2361 1110; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_58" title="bbox 102 1105 2361 1110; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_42" title="bbox 657 1173 839 1177">
        <p class="ocr_par" id="par_1_42" lang="eng" title="bbox 657 1173 839 1177">
<span class="ocr_line" id="line_1_42"
      title="bbox 657 1173 839 1177; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_59" title="bbox 657 1173 839 1177; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_43" title="bbox 657 276 661 1393">
        <p class="ocr_par" id="par_1_43" lang="eng" title="bbox 657 276 661 1393">
<span class="ocr_line" id="line_1_43"
      title="bbox 657 276 661 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_60" title="bbox 657 276 661 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_44" title="bbox 835 276 839 1393">
        <p class="ocr_par" id="par_1_44" lang="eng" title="bbox 835 276 839 1393">
<span class="ocr_line" id="line_1_44"
      title="bbox 835 276 839 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_61" title="bbox 835 276 839 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_45" title="bbox 657 1389 839 1393">
        <p class="ocr_par" id="par_1_45" lang="eng" title="bbox 657 1389 839 1393">
<span class="ocr_line" id="line_1_45"
      title="bbox 657 1389 839 1393; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_62" title="bbox 657 1389 839 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_46" title="bbox 1410 1173 1592 1177">
        <p class="ocr_par" id="par_1_46" lang="eng" title="bbox 1410 1173 1592 1177">
<span class="ocr_line" id="line_1_46"
      title="bbox 1410 1173 1592 1177; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_63" title="bbox 1410 1173 1592 1177; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_47" title="bbox 1410 276 1415 1393">
        <p class="ocr_par" id="par_1_47" lang="eng" title="bbox 1410 276 1415 1393">
<span class="ocr_line" id="line_1_47"
      title="bbox 1410 276 1415 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_64" title="bbox 1410 276 1415 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_48" title="bbox 1588 276 1592 1393">
        <p class="ocr_par" id="par_1_48" lang="eng" title="bbox 1588 276 1592 1393">
<span class="ocr_line" id="line_1_48"
      title="bbox 1588 276 1592 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_65" title="bbox 1588 276 1592 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_49" title="bbox 1410 1389 1592 1393">
        <p class="ocr_par" id="par_1_49" lang="eng" title="bbox 1410 1389 1592 1393">
<span class="ocr_line" id="line_1_49"
      title="bbox 1410 1389 1592 1393; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_66" title="bbox 1410 1389 1592 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_50" title="bbox 2163 1173 2345 1177">
        <p class="ocr_par" id="par_1_50" lang="eng" title="bbox 2163 1173 2345 1177">
<span class="ocr_line" id="line_1_50"
      title="bbox 2163 1173 2345 1177; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_67" title="bbox 2163 1173 2345 1177; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_51" title="bbox 2163 276 2168 1393">
        <p class="ocr_par" id="par_1_51" lang="eng" title="bbox 2163 276 2168 1393">
<span class="ocr_line" id="line_1_51"
      title="bbox 2163 276 2168 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_68" title="bbox 2163 276 2168 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_52" title="bbox 2341 276 2345 1393">
        <p class="ocr_par" id="par_1_52" lang="eng" title="bbox 2341 276 2345 1393">
<span class="ocr_line" id="line_1_52"
      title="bbox 2341 276 2345 1393; baseline 0 0; x_size 558.5; x_descenders -279.25; x_ascenders 279.25">
<span class="ocrx_word" id="word_1_69" title="bbox 2341 276 2345 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_53" title="bbox 2163 1389 2345 1393">
        <p class="ocr_par" id="par_1_53" lang="eng" title="bbox 2163 1389 2345 1393">
<span class="ocr_line" id="line_1_53"
      title="bbox 2163 1389 2345 1393; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_70" title="bbox 2163 1389 2345 1393; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_54" title="bbox 102 1397 2361 1408">
        <p class="ocr_par" id="par_1_54" lang="eng" title="bbox 102 1397 2361 1408">
<span class="ocr_line" id="line_1_54"
      title="bbox 102 1397 2361 1408; baseline 0 0; x_size 5.5; x_descenders -2.75; x_ascenders 2.75">
<span class="ocrx_word" id="word_1_71" title="bbox 102 1397 2361 1408; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_55" title="bbox 657 1472 839 1477">
        <p class="ocr_par" id="par_1_55" lang="eng" title="bbox 657 1472 839 1477">
<span class="ocr_line" id="line_1_55"
      title="bbox 657 1472 839 1477; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_72" title="bbox 657 1472 839 1477; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_56" title="bbox 657 276 661 1698">
        <p class="ocr_par" id="par_1_56" lang="eng" title="bbox 657 276 661 1698">
<span class="ocr_line" id="line_1_56"
      title="bbox 657 276 661 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_73" title="bbox 657 276 661 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_57" title="bbox 835 276 839 1698">
        <p class="ocr_par" id="par_1_57" lang="eng" title="bbox 835 276 839 1698">
<span class="ocr_line" id="line_1_57"
      title="bbox 835 276 839 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_74" title="bbox 835 276 839 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_58" title="bbox 1410 1472 1592 1477">
        <p class="ocr_par" id="par_1_58" lang="eng" title="bbox 1410 1472 1592 1477">
<span class="ocr_line" id="line_1_58"
      title="bbox 1410 1472 1592 1477; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_75" title="bbox 1410 1472 1592 1477; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_59" title="bbox 1410 276 1415 1698">
        <p class="ocr_par" id="par_1_59" lang="eng" title="bbox 1410 276 1415 1698">
<span class="ocr_line" id="line_1_59"
      title="bbox 1410 276 1415 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_76" title="bbox 1410 276 1415 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_60" title="bbox 1588 276 1592 1698">
        <p class="ocr_par" id="par_1_60" lang="eng" title="bbox 1588 276 1592 1698">
<span class="ocr_line" id="line_1_60"
      title="bbox 1588 276 1592 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_77" title="bbox 1588 276 1592 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_61" title="bbox 2163 1472 2345 1477">
        <p class="ocr_par" id="par_1_61" lang="eng" title="bbox 2163 1472 2345 1477">
<span class="ocr_line" id="line_1_61"
      title="bbox 2163 1472 2345 1477; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_78" title="bbox 2163 1472 2345 1477; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_62" title="bbox 2163 276 2168 1698">
        <p class="ocr_par" id="par_1_62" lang="eng" title="bbox 2163 276 2168 1698">
<span class="ocr_line" id="line_1_62"
      title="bbox 2163 276 2168 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_79" title="bbox 2163 276 2168 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_63" title="bbox 2341 276 2345 1698">
        <p class="ocr_par" id="par_1_63" lang="eng" title="bbox 2341 276 2345 1698">
<span class="ocr_line" id="line_1_63"
      title="bbox 2341 276 2345 1698; baseline 0 0; x_size 711; x_descenders -355.5; x_ascenders 355.5">
<span class="ocrx_word" id="word_1_80" title="bbox 2341 276 2345 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_64" title="bbox 102 1693 2361 1698">
        <p class="ocr_par" id="par_1_64" lang="eng" title="bbox 102 1693 2361 1698">
<span class="ocr_line" id="line_1_64"
      title="bbox 102 1693 2361 1698; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_81" title="bbox 102 1693 2361 1698; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_65" title="bbox 102 1702 2361 1707">
        <p class="ocr_par" id="par_1_65" lang="eng" title="bbox 102 1702 2361 1707">
<span class="ocr_line" id="line_1_65"
      title="bbox 102 1702 2361 1707; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_82" title="bbox 102 1702 2361 1707; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_66" title="bbox 657 1770 839 1774">
        <p class="ocr_par" id="par_1_66" lang="eng" title="bbox 657 1770 839 1774">
<span class="ocr_line" id="line_1_66"
      title="bbox 657 1770 839 1774; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_83" title="bbox 657 1770 839 1774; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_67" title="bbox 657 276 661 1990">
        <p class="ocr_par" id="par_1_67" lang="eng" title="bbox 657 276 661 1990">
<span class="ocr_line" id="line_1_67"
      title="bbox 657 276 661 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_84" title="bbox 657 276 661 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_68" title="bbox 835 276 839 1990">
        <p class="ocr_par" id="par_1_68" lang="eng" title="bbox 835 276 839 1990">
<span class="ocr_line" id="line_1_68"
      title="bbox 835 276 839 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_85" title="bbox 835 276 839 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_69" title="bbox 657 1986 839 1990">
        <p class="ocr_par" id="par_1_69" lang="eng" title="bbox 657 1986 839 1990">
<span class="ocr_line" id="line_1_69"
      title="bbox 657 1986 839 1990; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_86" title="bbox 657 1986 839 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_70" title="bbox 1410 1770 1592 1774">
        <p class="ocr_par" id="par_1_70" lang="eng" title="bbox 1410 1770 1592 1774">
<span class="ocr_line" id="line_1_70"
      title="bbox 1410 1770 1592 1774; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_87" title="bbox 1410 1770 1592 1774; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_71" title="bbox 1410 276 1415 1990">
        <p class="ocr_par" id="par_1_71" lang="eng" title="bbox 1410 276 1415 1990">
<span class="ocr_line" id="line_1_71"
      title="bbox 1410 276 1415 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_88" title="bbox 1410 276 1415 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_72" title="bbox 1588 276 1592 1990">
        <p class="ocr_par" id="par_1_72" lang="eng" title="bbox 1588 276 1592 1990">
<span class="ocr_line" id="line_1_72"
      title="bbox 1588 276 1592 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_89" title="bbox 1588 276 1592 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_73" title="bbox 1410 1986 1592 1990">
        <p class="ocr_par" id="par_1_73" lang="eng" title="bbox 1410 1986 1592 1990">
<span class="ocr_line" id="line_1_73"
      title="bbox 1410 1986 1592 1990; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_90" title="bbox 1410 1986 1592 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_74" title="bbox 2163 1770 2345 1774">
        <p class="ocr_par" id="par_1_74" lang="eng" title="bbox 2163 1770 2345 1774">
<span class="ocr_line" id="line_1_74"
      title="bbox 2163 1770 2345 1774; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_91" title="bbox 2163 1770 2345 1774; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_75" title="bbox 2163 276 2168 1990">
        <p class="ocr_par" id="par_1_75" lang="eng" title="bbox 2163 276 2168 1990">
<span class="ocr_line" id="line_1_75"
      title="bbox 2163 276 2168 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_92" title="bbox 2163 276 2168 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_76" title="bbox 2341 276 2345 1990">
        <p class="ocr_par" id="par_1_76" lang="eng" title="bbox 2341 276 2345 1990">
<span class="ocr_line" id="line_1_76"
      title="bbox 2341 276 2345 1990; baseline 0 0; x_size 857; x_descenders -428.5; x_ascenders 428.5">
<span class="ocrx_word" id="word_1_93" title="bbox 2341 276 2345 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_77" title="bbox 2163 1986 2345 1990">
        <p class="ocr_par" id="par_1_77" lang="eng" title="bbox 2163 1986 2345 1990">
<span class="ocr_line" id="line_1_77"
      title="bbox 2163 1986 2345 1990; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_94" title="bbox 2163 1986 2345 1990; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_78" title="bbox 102 1994 2361 2005">
        <p class="ocr_par" id="par_1_78" lang="eng" title="bbox 102 1994 2361 2005">
<span class="ocr_line" id="line_1_78"
      title="bbox 102 1994 2361 2005; baseline 0 0; x_size 5.5; x_descenders -2.75; x_ascenders 2.75">
<span class="ocrx_word" id="word_1_95" title="bbox 102 1994 2361 2005; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_79" title="bbox 657 2070 839 2074">
        <p class="ocr_par" id="par_1_79" lang="eng" title="bbox 657 2070 839 2074">
<span class="ocr_line" id="line_1_79"
      title="bbox 657 2070 839 2074; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_96" title="bbox 657 2070 839 2074; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_80" title="bbox 657 276 661 2290">
        <p class="ocr_par" id="par_1_80" lang="eng" title="bbox 657 276 661 2290">
<span class="ocr_line" id="line_1_80"
      title="bbox 657 276 661 2290; baseline 0 0; x_size 1007; x_descenders -503.5; x_ascenders 503.5">
<span class="ocrx_word" id="word_1_97" title="bbox 657 276 661 2290; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_81" title="bbox 835 276 839 2290">
        <p class="ocr_par" id="par_1_81" lang="eng" title="bbox 835 276 839 2290">
<span class="ocr_line" id="line_1_81"
      title="bbox 835 276 839 2290; baseline 0 0; x_size 1007; x_descenders -503.5; x_ascenders 503.5">
<span class="ocrx_word" id="word_1_98" title="bbox 835 276 839 2290; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_82" title="bbox 657 2286 839 2290">
        <p class="ocr_par" id="par_1_82" lang="eng" title="bbox 657 2286 839 2290">
<span class="ocr_line" id="line_1_82"
      title="bbox 657 2286 839 2290; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_99" title="bbox 657 2286 839 2290; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_83" title="bbox 1410 2070 1592 2074">
        <p class="ocr_par" id="par_1_83" lang="eng" title="bbox 1410 2070 1592 2074">
<span class="ocr_line" id="line_1_83"
      title="bbox 1410 2070 1592 2074; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_100" title="bbox 1410 2070 1592 2074; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_84" title="bbox 1410 276 1415 2296">
        <p class="ocr_par" id="par_1_84" lang="eng" title="bbox 1410 276 1415 2296">
<span class="ocr_line" id="line_1_84"
      title="bbox 1410 276 1415 2296; baseline 0 0; x_size 1010; x_descenders -505; x_ascenders 505">
<span class="ocrx_word" id="word_1_101" title="bbox 1410 276 1415 2296; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_85" title="bbox 1588 276 1592 2296">
        <p class="ocr_par" id="par_1_85" lang="eng" title="bbox 1588 276 1592 2296">
<span class="ocr_line" id="line_1_85"
      title="bbox 1588 276 1592 2296; baseline 0 0; x_size 1010; x_descenders -505; x_ascenders 505">
<span class="ocrx_word" id="word_1_102" title="bbox 1588 276 1592 2296; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_86" title="bbox 2163 2070 2345 2074">
        <p class="ocr_par" id="par_1_86" lang="eng" title="bbox 2163 2070 2345 2074">
<span class="ocr_line" id="line_1_86"
      title="bbox 2163 2070 2345 2074; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_103" title="bbox 2163 2070 2345 2074; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_87" title="bbox 2163 276 2168 2296">
        <p class="ocr_par" id="par_1_87" lang="eng" title="bbox 2163 276 2168 2296">
<span class="ocr_line" id="line_1_87"
      title="bbox 2163 276 2168 2296; baseline 0 0; x_size 1010; x_descenders -505; x_ascenders 505">
<span class="ocrx_word" id="word_1_104" title="bbox 2163 276 2168 2296; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_88" title="bbox 2341 276 2345 2296">
        <p class="ocr_par" id="par_1_88" lang="eng" title="bbox 2341 276 2345 2296">
<span class="ocr_line" id="line_1_88"
      title="bbox 2341 276 2345 2296; baseline 0 0; x_size 1010; x_descenders -505; x_ascenders 505">
<span class="ocrx_word" id="word_1_105" title="bbox 2341 276 2345 2296; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_89" title="bbox 102 2283 2361 2300">
        <p class="ocr_par" id="par_1_89" lang="eng" title="bbox 102 2283 2361 2300">
<span class="ocr_line" id="line_1_89"
      title="bbox 102 2283 2361 2300; baseline 0 0; x_size 8.5; x_descenders -4.25; x_ascenders 4.25">
<span class="ocrx_word" id="word_1_106" title="bbox 102 2283 2361 2300; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_90" title="bbox 102 2298 2361 2305">
        <p class="ocr_par" id="par_1_90" lang="eng" title="bbox 102 2298 2361 2305">
<span class="ocr_line" id="line_1_90"
      title="bbox 102 2298 2361 2305; baseline 0 0; x_size 3.5; x_descenders -1.75; x_ascenders 1.75">
<span class="ocrx_word" id="word_1_107" title="bbox 102 2298 2361 2305; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_91" title="bbox 657 2367 839 2372">
        <p class="ocr_par" id="par_1_91" lang="eng" title="bbox 657 2367 839 2372">
<span class="ocr_line" id="line_1_91"
      title="bbox 657 2367 839 2372; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_108" title="bbox 657 2367 839 2372; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_92" title="bbox 657 276 661 2587">
        <p class="ocr_par" id="par_1_92" lang="eng" title="bbox 657 276 661 2587">
<span class="ocr_line" id="line_1_92"
      title="bbox 657 276 661 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_109" title="bbox 657 276 661 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_93" title="bbox 835 276 839 2587">
        <p class="ocr_par" id="par_1_93" lang="eng" title="bbox 835 276 839 2587">
<span class="ocr_line" id="line_1_93"
      title="bbox 835 276 839 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_110" title="bbox 835 276 839 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_94" title="bbox 657 2583 839 2587">
        <p class="ocr_par" id="par_1_94" lang="eng" title="bbox 657 2583 839 2587">
<span class="ocr_line" id="line_1_94"
      title="bbox 657 2583 839 2587; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_111" title="bbox 657 2583 839 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_95" title="bbox 1410 2367 1592 2372">
        <p class="ocr_par" id="par_1_95" lang="eng" title="bbox 1410 2367 1592 2372">
<span class="ocr_line" id="line_1_95"
      title="bbox 1410 2367 1592 2372; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_112" title="bbox 1410 2367 1592 2372; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_96" title="bbox 1410 276 1415 2587">
        <p class="ocr_par" id="par_1_96" lang="eng" title="bbox 1410 276 1415 2587">
<span class="ocr_line" id="line_1_96"
      title="bbox 1410 276 1415 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_113" title="bbox 1410 276 1415 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_97" title="bbox 1588 276 1592 2587">
        <p class="ocr_par" id="par_1_97" lang="eng" title="bbox 1588 276 1592 2587">
<span class="ocr_line" id="line_1_97"
      title="bbox 1588 276 1592 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_114" title="bbox 1588 276 1592 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_98" title="bbox 1410 2583 1592 2587">
        <p class="ocr_par" id="par_1_98" lang="eng" title="bbox 1410 2583 1592 2587">
<span class="ocr_line" id="line_1_98"
      title="bbox 1410 2583 1592 2587; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_115" title="bbox 1410 2583 1592 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_99" title="bbox 2163 2367 2345 2372">
        <p class="ocr_par" id="par_1_99" lang="eng" title="bbox 2163 2367 2345 2372">
<span class="ocr_line" id="line_1_99"
      title="bbox 2163 2367 2345 2372; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_116" title="bbox 2163 2367 2345 2372; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_100" title="bbox 2163 276 2168 2587">
        <p class="ocr_par" id="par_1_100" lang="eng" title="bbox 2163 276 2168 2587">
<span class="ocr_line" id="line_1_100"
      title="bbox 2163 276 2168 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_117" title="bbox 2163 276 2168 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_101" title="bbox 2341 276 2345 2587">
        <p class="ocr_par" id="par_1_101" lang="eng" title="bbox 2341 276 2345 2587">
<span class="ocr_line" id="line_1_101"
      title="bbox 2341 276 2345 2587; baseline 0 0; x_size 1155.5; x_descenders -577.75; x_ascenders 577.75">
<span class="ocrx_word" id="word_1_118" title="bbox 2341 276 2345 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_102" title="bbox 2163 2583 2345 2587">
        <p class="ocr_par" id="par_1_102" lang="eng" title="bbox 2163 2583 2345 2587">
<span class="ocr_line" id="line_1_102"
      title="bbox 2163 2583 2345 2587; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_119" title="bbox 2163 2583 2345 2587; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_103" title="bbox 102 2591 2361 2602">
        <p class="ocr_par" id="par_1_103" lang="eng" title="bbox 102 2591 2361 2602">
<span class="ocr_line" id="line_1_103"
      title="bbox 102 2591 2361 2602; baseline 0 0; x_size 5.5; x_descenders -2.75; x_ascenders 2.75">
<span class="ocrx_word" id="word_1_120" title="bbox 102 2591 2361 2602; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_104" title="bbox 657 2667 839 2671">
        <p class="ocr_par" id="par_1_104" lang="eng" title="bbox 657 2667 839 2671">
<span class="ocr_line" id="line_1_104"
      title="bbox 657 2667 839 2671; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_121" title="bbox 657 2667 839 2671; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_105" title="bbox 657 276 661 2887">
        <p class="ocr_par" id="par_1_105" lang="eng" title="bbox 657 276 661 2887">
<span class="ocr_line" id="line_1_105"
      title="bbox 657 276 661 2887; baseline 0 0; x_size 1305.5; x_descenders -652.75; x_ascenders 652.75">
<span class="ocrx_word" id="word_1_122" title="bbox 657 276 661 2887; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_106" title="bbox 835 276 839 2887">
        <p class="ocr_par" id="par_1_106" lang="eng" title="bbox 835 276 839 2887">
<span class="ocr_line" id="line_1_106"
      title="bbox 835 276 839 2887; baseline 0 0; x_size 1305.5; x_descenders -652.75; x_ascenders 652.75">
<span class="ocrx_word" id="word_1_123" title="bbox 835 276 839 2887; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_107" title="bbox 657 2883 839 2887">
        <p class="ocr_par" id="par_1_107" lang="eng" title="bbox 657 2883 839 2887">
<span class="ocr_line" id="line_1_107"
      title="bbox 657 2883 839 2887; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_124" title="bbox 657 2883 839 2887; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_108" title="bbox 1410 2667 1592 2671">
        <p class="ocr_par" id="par_1_108" lang="eng" title="bbox 1410 2667 1592 2671">
<span class="ocr_line" id="line_1_108"
      title="bbox 1410 2667 1592 2671; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_125" title="bbox 1410 2667 1592 2671; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_109" title="bbox 1410 276 1415 2893">
        <p class="ocr_par" id="par_1_109" lang="eng" title="bbox 1410 276 1415 2893">
<span class="ocr_line" id="line_1_109"
      title="bbox 1410 276 1415 2893; baseline 0 0; x_size 1308.5; x_descenders -654.25; x_ascenders 654.25">
<span class="ocrx_word" id="word_1_126" title="bbox 1410 276 1415 2893; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_110" title="bbox 1588 276 1592 2893">
        <p class="ocr_par" id="par_1_110" lang="eng" title="bbox 1588 276 1592 2893">
<span class="ocr_line" id="line_1_110"
      title="bbox 1588 276 1592 2893; baseline 0 0; x_size 1308.5; x_descenders -654.25; x_ascenders 654.25">
<span class="ocrx_word" id="word_1_127" title="bbox 1588 276 1592 2893; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_111" title="bbox 2163 2667 2345 2671">
        <p class="ocr_par" id="par_1_111" lang="eng" title="bbox 2163 2667 2345 2671">
<span class="ocr_line" id="line_1_111"
      title="bbox 2163 2667 2345 2671; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_128" title="bbox 2163 2667 2345 2671; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_112" title="bbox 2163 276 2168 2893">
        <p class="ocr_par" id="par_1_112" lang="eng" title="bbox 2163 276 2168 2893">
<span class="ocr_line" id="line_1_112"
      title="bbox 2163 276 2168 2893; baseline 0 0; x_size 1308.5; x_descenders -654.25; x_ascenders 654.25">
<span class="ocrx_word" id="word_1_129" title="bbox 2163 276 2168 2893; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_113" title="bbox 2341 276 2345 2893">
        <p class="ocr_par" id="par_1_113" lang="eng" title="bbox 2341 276 2345 2893">
<span class="ocr_line" id="line_1_113"
      title="bbox 2341 276 2345 2893; baseline 0 0; x_size 1308.5; x_descenders -654.25; x_ascenders 654.25">
<span class="ocrx_word" id="word_1_130" title="bbox 2341 276 2345 2893; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_114" title="bbox 102 2880 2361 2897">
        <p class="ocr_par" id="par_1_114" lang="eng" title="bbox 102 2880 2361 2897">
<span class="ocr_line" id="line_1_114"
      title="bbox 102 2880 2361 2897; baseline 0 0; x_size 8.5; x_descenders -4.25; x_ascenders 4.25">
<span class="ocrx_word" id="word_1_131" title="bbox 102 2880 2361 2897; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_115" title="bbox 102 2895 2361 2902">
        <p class="ocr_par" id="par_1_115" lang="eng" title="bbox 102 2895 2361 2902">
<span class="ocr_line" id="line_1_115"
      title="bbox 102 2895 2361 2902; baseline 0 0; x_size 3.5; x_descenders -1.75; x_ascenders 1.75">
<span class="ocrx_word" id="word_1_132" title="bbox 102 2895 2361 2902; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_116" title="bbox 102 210 104 3193">
        <p class="ocr_par" id="par_1_116" lang="eng" title="bbox 102 210 104 3193">
<span class="ocr_line" id="line_1_116"
      title="bbox 102 210 104 3193; baseline 0 0; x_size 1491.5; x_descenders -745.75; x_ascenders 745.75">
<span class="ocrx_word" id="word_1_133" title="bbox 102 210 104 3193; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_117" title="bbox 657 2965 839 2969">
        <p class="ocr_par" id="par_1_117" lang="eng" title="bbox 657 2965 839 2969">
<span class="ocr_line" id="line_1_117"
      title="bbox 657 2965 839 2969; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_134" title="bbox 657 2965 839 2969; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_118" title="bbox 657 276 661 3185">
        <p class="ocr_par" id="par_1_118" lang="eng" title="bbox 657 276 661 3185">
<span class="ocr_line" id="line_1_118"
      title="bbox 657 276 661 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_135" title="bbox 657 276 661 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_119" title="bbox 853 210 857 3193">
        <p class="ocr_par" id="par_1_119" lang="eng" title="bbox 853 210 857 3193">
<span class="ocr_line" id="line_1_119"
      title="bbox 853 210 857 3193; baseline 0 0; x_size 1491.5; x_descenders -745.75; x_ascenders 745.75">
<span class="ocrx_word" id="word_1_136" title="bbox 853 210 857 3193; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_120" title="bbox 835 276 839 3185">
        <p class="ocr_par" id="par_1_120" lang="eng" title="bbox 835 276 839 3185">
<span class="ocr_line" id="line_1_120"
      title="bbox 835 276 839 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_137" title="bbox 835 276 839 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_121" title="bbox 657 3180 839 3185">
        <p class="ocr_par" id="par_1_121" lang="eng" title="bbox 657 3180 839 3185">
<span class="ocr_line" id="line_1_121"
      title="bbox 657 3180 839 3185; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_138" title="bbox 657 3180 839 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_122" title="bbox 1410 2965 1592 2969">
        <p class="ocr_par" id="par_1_122" lang="eng" title="bbox 1410 2965 1592 2969">
<span class="ocr_line" id="line_1_122"
      title="bbox 1410 2965 1592 2969; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_139" title="bbox 1410 2965 1592 2969; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_123" title="bbox 1410 276 1415 3185">
        <p class="ocr_par" id="par_1_123" lang="eng" title="bbox 1410 276 1415 3185">
<span class="ocr_line" id="line_1_123"
      title="bbox 1410 276 1415 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_140" title="bbox 1410 276 1415 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_124" title="bbox 1606 210 1610 3193">
        <p class="ocr_par" id="par_1_124" lang="eng" title="bbox 1606 210 1610 3193">
<span class="ocr_line" id="line_1_124"
      title="bbox 1606 210 1610 3193; baseline 0 0; x_size 1491.5; x_descenders -745.75; x_ascenders 745.75">
<span class="ocrx_word" id="word_1_141" title="bbox 1606 210 1610 3193; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_125" title="bbox 1588 276 1592 3185">
        <p class="ocr_par" id="par_1_125" lang="eng" title="bbox 1588 276 1592 3185">
<span class="ocr_line" id="line_1_125"
      title="bbox 1588 276 1592 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_142" title="bbox 1588 276 1592 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_126" title="bbox 1410 3180 1592 3185">
        <p class="ocr_par" id="par_1_126" lang="eng" title="bbox 1410 3180 1592 3185">
<span class="ocr_line" id="line_1_126"
      title="bbox 1410 3180 1592 3185; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_143" title="bbox 1410 3180 1592 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_127" title="bbox 2163 2965 2345 2969">
        <p class="ocr_par" id="par_1_127" lang="eng" title="bbox 2163 2965 2345 2969">
<span class="ocr_line" id="line_1_127"
      title="bbox 2163 2965 2345 2969; baseline 0 0; x_size 2; x_descenders -1; x_ascenders 1">
<span class="ocrx_word" id="word_1_144" title="bbox 2163 2965 2345 2969; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_128" title="bbox 2163 276 2168 3185">
        <p class="ocr_par" id="par_1_128" lang="eng" title="bbox 2163 276 2168 3185">
<span class="ocr_line" id="line_1_128"
      title="bbox 2163 276 2168 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_145" title="bbox 2163 276 2168 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_129" title="bbox 2341 276 2345 3185">
        <p class="ocr_par" id="par_1_129" lang="eng" title="bbox 2341 276 2345 3185">
<span class="ocr_line" id="line_1_129"
      title="bbox 2341 276 2345 3185; baseline 0 0; x_size 1454.5; x_descenders -727.25; x_ascenders 727.25">
<span class="ocrx_word" id="word_1_146" title="bbox 2341 276 2345 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_130" title="bbox 2163 3180 2345 3185">
        <p class="ocr_par" id="par_1_130" lang="eng" title="bbox 2163 3180 2345 3185">
<span class="ocr_line" id="line_1_130"
      title="bbox 2163 3180 2345 3185; baseline 0 0; x_size 2.5; x_descenders -1.25; x_ascenders 1.25">
<span class="ocrx_word" id="word_1_147" title="bbox 2163 3180 2345 3185; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_131" title="bbox 102 3190 2361 3193">
        <p class="ocr_par" id="par_1_131" lang="eng" title="bbox 102 3190 2361 3193">
<span class="ocr_line" id="line_1_131"
      title="bbox 102 3190 2361 3193; baseline 0 0; x_size 1.5; x_descenders -0.75; x_ascenders 0.75">
<span class="ocrx_word" id="word_1_148" title="bbox 102 3190 2361 3193; x_wconf 95"> </span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_132" title="bbox 54 222 2343 3464">
        <p class="ocr_par" id="par_1_132" lang="eng" title="bbox 54 222 2343 3464">
<span class="ocr_line" id="line_1_132"
      title="bbox 246 222 2343 260; baseline 0 -10; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_149" title="bbox 246 222 254 240; x_wconf 76">1</span>
<span class="ocrx_word" id="word_1_150" title="bbox 651 222 835 260; x_wconf 86">HNL6961486</span>
<span class="ocrx_word" id="word_1_151" title="bbox 997 222 1009 240; x_wconf 96">2</span>
<span class="ocrx_word" id="word_1_152" title="bbox 1401 226 1589 250; x_wconf 92">REX0383539</span>
<span class="ocrx_word" id="word_1_153" title="bbox 1752 222 1762 240; x_wconf 95">3</span>
<span class="ocrx_word" id="word_1_154" title="bbox 2154 226 2343 250; x_wconf 91">REX0320440</span>
</span>
            <span class="ocr_line" id="line_1_133"
                  title="bbox 116 264 1964 292; baseline 0 -6; x_size 28; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_155" title="bbox 116 264 205 286; x_wconf 86">Name</span>
<span class="ocrx_word" id="word_1_156" title="bbox 199 260 211 296; x_wconf 57">:</span>
<span class="ocrx_word" id="word_1_157" title="bbox 224 264 336 286; x_wconf 78">Vasudha</span>
<span class="ocrx_word" id="word_1_158" title="bbox 346 264 394 286; x_wconf 96">Tari</span>
<span class="ocrx_word" id="word_1_159" title="bbox 869 264 959 286; x_wconf 81">Name</span>
<span class="ocrx_word" id="word_1_160" title="bbox 952 260 964 296; x_wconf 69">:</span>
<span class="ocrx_word" id="word_1_161" title="bbox 979 264 1057 292; x_wconf 78">Sathej</span>
<span class="ocrx_word" id="word_1_162" title="bbox 1069 264 1123 286; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_163" title="bbox 1622 264 1712 286; x_wconf 89">Name</span>
<span class="ocrx_word" id="word_1_164" title="bbox 1705 260 1717 296; x_wconf 67">:</span>
<span class="ocrx_word" id="word_1_165" title="bbox 1730 264 1814 292; x_wconf 93">Vidhya</span>
<span class="ocrx_word" id="word_1_166" title="bbox 1826 264 1964 286; x_wconf 92">Bandodkar</span>
</span>
            <span class="ocr_line" id="line_1_134"
                  title="bbox 116 298 2142 320; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_167" title="bbox 116 298 250 320; x_wconf 96">Husband's</span>
<span class="ocrx_word" id="word_1_168" title="bbox 262 298 351 320; x_wconf 52">Name:</span>
<span class="ocrx_word" id="word_1_169" title="bbox 370 298 482 320; x_wconf 91">Vasudev</span>
<span class="ocrx_word" id="word_1_170" title="bbox 490 298 538 320; x_wconf 96">Tari</span>
<span class="ocrx_word" id="word_1_171" title="bbox 869 298 971 320; x_wconf 95">Father's</span>
<span class="ocrx_word" id="word_1_172" title="bbox 983 298 1058 320; x_wconf 83">Name</span>
<span class="ocrx_word" id="word_1_173" title="bbox 1069 304 1072 320; x_wconf 70">:</span>
<span class="ocrx_word" id="word_1_174" title="bbox 1093 298 1221 320; x_wconf 91">Sadanand</span>
<span class="ocrx_word" id="word_1_175" title="bbox 1232 298 1287 320; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_176" title="bbox 1622 298 1756 320; x_wconf 96">Husband's</span>
<span class="ocrx_word" id="word_1_177" title="bbox 1768 298 1858 320; x_wconf 86">Name:</span>
<span class="ocrx_word" id="word_1_178" title="bbox 1878 298 1994 320; x_wconf 93">Prashant</span>
<span class="ocrx_word" id="word_1_179" title="bbox 2004 298 2142 320; x_wconf 90">Bandodkar</span>
</span>
            <span class="ocr_line" id="line_1_135"
                  title="bbox 116 332 1914 352; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_180" title="bbox 116 332 193 352; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_181" title="bbox 204 332 313 352; x_wconf 87">Number</span>
<span class="ocrx_word" id="word_1_182" title="bbox 306 325 316 362; x_wconf 55">:</span>
<span class="ocrx_word" id="word_1_183" title="bbox 332 344 341 346; x_wconf 91">-</span>
<span class="ocrx_word" id="word_1_184" title="bbox 869 332 947 352; x_wconf 95">House</span>
<span class="ocrx_word" id="word_1_185" title="bbox 957 332 1066 352; x_wconf 70">Number</span>
<span class="ocrx_word" id="word_1_186" title="bbox 1062 325 1072 362; x_wconf 56">:</span>
<span class="ocrx_word" id="word_1_187" title="bbox 1086 332 1151 352; x_wconf 80">334/1</span>
<span class="ocrx_word" id="word_1_188" title="bbox 1622 332 1700 352; x_wconf 95">House</span>
<span class="ocrx_word" id="word_1_189" title="bbox 1710 332 1820 352; x_wconf 82">Number</span>
<span class="ocrx_word" id="word_1_190" title="bbox 1815 325 1825 362; x_wconf 82">:</span>
<span class="ocrx_word" id="word_1_191" title="bbox 1840 332 1914 352; x_wconf 88">803-A</span>
</span>
            <span class="ocr_line" id="line_1_136"
                  title="bbox 114 360 2302 392; baseline 0 -6; x_size 30; x_descenders 4; x_ascenders 10">
<span class="ocrx_word" id="word_1_192" title="bbox 114 364 177 392; x_wconf 93">Age:</span>
<span class="ocrx_word" id="word_1_193" title="bbox 196 364 226 386; x_wconf 96">49</span>
<span class="ocrx_word" id="word_1_194" title="bbox 246 364 353 386; x_wconf 86">Gender:</span>
<span class="ocrx_word" id="word_1_195" title="bbox 374 364 484 386; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_196" title="bbox 693 360 765 382; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_197" title="bbox 777 360 795 382; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_198" title="bbox 867 364 931 392; x_wconf 89">Age:</span>
<span class="ocrx_word" id="word_1_199" title="bbox 949 364 979 386; x_wconf 94">23</span>
<span class="ocrx_word" id="word_1_200" title="bbox 999 364 1106 386; x_wconf 88">Gender:</span>
<span class="ocrx_word" id="word_1_201" title="bbox 1127 364 1199 386; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_202" title="bbox 1446 360 1518 382; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_203" title="bbox 1530 360 1549 382; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_204" title="bbox 1620 364 1684 392; x_wconf 93">Age:</span>
<span class="ocrx_word" id="word_1_205" title="bbox 1704 364 1732 386; x_wconf 95">39</span>
<span class="ocrx_word" id="word_1_206" title="bbox 1752 364 1859 386; x_wconf 85">Gender:</span>
<span class="ocrx_word" id="word_1_207" title="bbox 1880 364 1990 386; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_208" title="bbox 2200 360 2272 382; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_209" title="bbox 2283 360 2302 382; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_137"
                  title="bbox 691 390 2311 426; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_210" title="bbox 691 390 805 426; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_211" title="bbox 1444 390 1558 426; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_212" title="bbox 2197 394 2311 416; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_138"
                  title="bbox 244 520 2337 550; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_213" title="bbox 244 520 257 538; x_wconf 96">4</span>
<span class="ocrx_word" id="word_1_214" title="bbox 647 526 835 550; x_wconf 91">REX0122382</span>
<span class="ocrx_word" id="word_1_215" title="bbox 999 520 1009 538; x_wconf 95">5</span>
<span class="ocrx_word" id="word_1_216" title="bbox 1401 526 1589 550; x_wconf 85">REX0341123</span>
<span class="ocrx_word" id="word_1_217" title="bbox 1752 520 1762 538; x_wconf 59">6</span>
<span class="ocrx_word" id="word_1_218" title="bbox 2154 526 2337 550; x_wconf 91">REX0425231</span>
</span>
            <span class="ocr_line" id="line_1_139"
                  title="bbox 116 563 1936 592; baseline 0 -6; x_size 29; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_219" title="bbox 116 563 205 586; x_wconf 69">Name:</span>
<span class="ocrx_word" id="word_1_220" title="bbox 226 563 310 586; x_wconf 93">Bharat</span>
<span class="ocrx_word" id="word_1_221" title="bbox 320 563 416 586; x_wconf 91">Chavan</span>
<span class="ocrx_word" id="word_1_222" title="bbox 869 563 959 586; x_wconf 78">Name</span>
<span class="ocrx_word" id="word_1_223" title="bbox 951 559 964 596; x_wconf 78">:</span>
<span class="ocrx_word" id="word_1_224" title="bbox 979 563 1087 592; x_wconf 93">Priyanka</span>
<span class="ocrx_word" id="word_1_225" title="bbox 1099 563 1203 586; x_wconf 91">Chawan</span>
<span class="ocrx_word" id="word_1_226" title="bbox 1622 563 1712 586; x_wconf 66">Name:</span>
<span class="ocrx_word" id="word_1_227" title="bbox 1732 563 1848 586; x_wconf 96">Prashant</span>
<span class="ocrx_word" id="word_1_228" title="bbox 1861 563 1936 586; x_wconf 96">Yadav</span>
</span>
            <span class="ocr_line" id="line_1_140"
                  title="bbox 116 597 2002 620; baseline 0 0; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_229" title="bbox 116 597 218 620; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_230" title="bbox 230 597 305 620; x_wconf 83">Name</span>
<span class="ocrx_word" id="word_1_231" title="bbox 316 604 319 619; x_wconf 79">:</span>
<span class="ocrx_word" id="word_1_232" title="bbox 338 597 424 620; x_wconf 91">Jairam</span>
<span class="ocrx_word" id="word_1_233" title="bbox 435 597 532 620; x_wconf 92">Chavan</span>
<span class="ocrx_word" id="word_1_234" title="bbox 869 597 1003 620; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_235" title="bbox 1015 597 1104 620; x_wconf 80">Name:</span>
<span class="ocrx_word" id="word_1_236" title="bbox 1125 597 1208 620; x_wconf 92">Bharat</span>
<span class="ocrx_word" id="word_1_237" title="bbox 1218 597 1323 620; x_wconf 92">Chawan</span>
<span class="ocrx_word" id="word_1_238" title="bbox 1622 597 1724 620; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_239" title="bbox 1736 597 1826 620; x_wconf 62">Name:</span>
<span class="ocrx_word" id="word_1_240" title="bbox 1846 597 1912 620; x_wconf 96">Datta</span>
<span class="ocrx_word" id="word_1_241" title="bbox 1922 597 2002 620; x_wconf 96">Yadav</span>
</span>
            <span class="ocr_line" id="line_1_141"
                  title="bbox 116 631 2286 660; baseline 0 -8; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_242" title="bbox 116 631 193 652; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_243" title="bbox 204 631 313 652; x_wconf 77">Number</span>
<span class="ocrx_word" id="word_1_244" title="bbox 309 625 319 662; x_wconf 77">:</span>
<span class="ocrx_word" id="word_1_245" title="bbox 333 631 378 652; x_wconf 96">804</span>
<span class="ocrx_word" id="word_1_246" title="bbox 777 657 779 660; x_wconf 26">;</span>
<span class="ocrx_word" id="word_1_247" title="bbox 869 631 947 652; x_wconf 95">House</span>
<span class="ocrx_word" id="word_1_248" title="bbox 957 631 1066 652; x_wconf 65">Number:</span>
<span class="ocrx_word" id="word_1_249" title="bbox 1087 631 1131 652; x_wconf 93">804</span>
<span class="ocrx_word" id="word_1_250" title="bbox 1530 657 1532 660; x_wconf 27">;</span>
<span class="ocrx_word" id="word_1_251" title="bbox 1622 631 1700 652; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_252" title="bbox 1710 631 1820 652; x_wconf 67">Number:</span>
<span class="ocrx_word" id="word_1_253" title="bbox 1840 631 1914 652; x_wconf 91">805-A</span>
<span class="ocrx_word" id="word_1_254" title="bbox 2283 657 2286 660; x_wconf 0">:</span>
</span>
            <span class="ocr_line" id="line_1_142"
                  title="bbox 114 657 2302 692; baseline 0 -6; x_size 35; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_255" title="bbox 114 663 177 692; x_wconf 83">Age:</span>
<span class="ocrx_word" id="word_1_256" title="bbox 196 663 226 686; x_wconf 96">46</span>
<span class="ocrx_word" id="word_1_257" title="bbox 246 663 353 686; x_wconf 93">Gender:</span>
<span class="ocrx_word" id="word_1_258" title="bbox 373 663 446 686; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_259" title="bbox 693 657 765 680; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_260" title="bbox 777 663 795 680; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_261" title="bbox 867 663 931 692; x_wconf 88">Age:</span>
<span class="ocrx_word" id="word_1_262" title="bbox 949 663 979 686; x_wconf 95">44</span>
<span class="ocrx_word" id="word_1_263" title="bbox 999 663 1106 686; x_wconf 92">Gender:</span>
<span class="ocrx_word" id="word_1_264" title="bbox 1127 663 1237 686; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_265" title="bbox 1446 657 1518 680; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_266" title="bbox 1530 663 1549 680; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_267" title="bbox 1620 663 1684 692; x_wconf 77">Age:</span>
<span class="ocrx_word" id="word_1_268" title="bbox 1704 663 1734 686; x_wconf 96">50</span>
<span class="ocrx_word" id="word_1_269" title="bbox 1752 663 1859 686; x_wconf 94">Gender:</span>
<span class="ocrx_word" id="word_1_270" title="bbox 1880 663 1952 686; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_271" title="bbox 2200 657 2272 680; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_272" title="bbox 2283 663 2302 680; x_wconf 93">is</span>
</span>
            <span class="ocr_line" id="line_1_143"
                  title="bbox 691 687 2311 724; baseline 0 -10; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_273" title="bbox 691 687 805 724; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_274" title="bbox 1444 687 1558 724; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_275" title="bbox 2197 691 2311 714; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_144"
                  title="bbox 112 807 2342 860; baseline 0 -13; x_size 44.418274; x_descenders 8.418272; x_ascenders 12">
<span class="ocrx_word" id="word_1_276" title="bbox 112 807 157 860; x_wconf 0">L</span>
<span class="ocrx_word" id="word_1_277" title="bbox 209 807 271 860; x_wconf 0">7]</span>
<span class="ocrx_word" id="word_1_278" title="bbox 647 823 831 847; x_wconf 92">REX0263541</span>
<span class="ocrx_word" id="word_1_279" title="bbox 999 819 1009 837; x_wconf 65">8</span>
<span class="ocrx_word" id="word_1_280" title="bbox 1405 823 1589 847; x_wconf 92">HNL1386853</span>
<span class="ocrx_word" id="word_1_281" title="bbox 1622 811 1774 853; x_wconf 18">||</span>
<span class="ocrx_word" id="word_1_282" title="bbox 1745 807 1777 860; x_wconf 18">94</span>
<span class="ocrx_word" id="word_1_283" title="bbox 2154 823 2342 847; x_wconf 91">REX0327882</span>
</span>
            <span class="ocr_line" id="line_1_145"
                  title="bbox 116 863 1876 891; baseline 0 -6; x_size 28; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_284" title="bbox 116 863 205 885; x_wconf 85">Name:</span>
<span class="ocrx_word" id="word_1_285" title="bbox 226 863 316 885; x_wconf 95">Prasad</span>
<span class="ocrx_word" id="word_1_286" title="bbox 326 863 406 885; x_wconf 96">Yadav</span>
<span class="ocrx_word" id="word_1_287" title="bbox 869 863 959 885; x_wconf 75">Name:</span>
<span class="ocrx_word" id="word_1_288" title="bbox 979 863 1057 885; x_wconf 91">Sarika</span>
<span class="ocrx_word" id="word_1_289" title="bbox 1067 863 1147 885; x_wconf 96">Yadav</span>
<span class="ocrx_word" id="word_1_290" title="bbox 1622 863 1712 885; x_wconf 81">Name:</span>
<span class="ocrx_word" id="word_1_291" title="bbox 1732 863 1820 891; x_wconf 95">Shreya</span>
<span class="ocrx_word" id="word_1_292" title="bbox 1832 863 1876 885; x_wconf 96">Lad</span>
</span>
            <span class="ocr_line" id="line_1_146"
                  title="bbox 116 897 2016 919; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_293" title="bbox 116 897 218 919; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_294" title="bbox 230 897 305 919; x_wconf 65">Name</span>
<span class="ocrx_word" id="word_1_295" title="bbox 316 903 319 919; x_wconf 65">:</span>
<span class="ocrx_word" id="word_1_296" title="bbox 340 897 406 919; x_wconf 95">Datta</span>
<span class="ocrx_word" id="word_1_297" title="bbox 416 897 496 919; x_wconf 96">Yadav</span>
<span class="ocrx_word" id="word_1_298" title="bbox 869 897 1003 919; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_299" title="bbox 1015 897 1104 919; x_wconf 77">Name:</span>
<span class="ocrx_word" id="word_1_300" title="bbox 1125 897 1240 919; x_wconf 96">Prashant</span>
<span class="ocrx_word" id="word_1_301" title="bbox 1249 897 1329 919; x_wconf 96">Yadav</span>
<span class="ocrx_word" id="word_1_302" title="bbox 1622 897 1724 919; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_303" title="bbox 1736 897 1826 919; x_wconf 90">Name</span>
<span class="ocrx_word" id="word_1_304" title="bbox 1822 893 1834 929; x_wconf 57">:</span>
<span class="ocrx_word" id="word_1_305" title="bbox 1846 897 1960 919; x_wconf 96">Chandan</span>
<span class="ocrx_word" id="word_1_306" title="bbox 1972 897 2016 919; x_wconf 96">Lad</span>
</span>
            <span class="ocr_line" id="line_1_147"
                  title="bbox 116 931 1884 951; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_307" title="bbox 116 931 193 951; x_wconf 95">House</span>
<span class="ocrx_word" id="word_1_308" title="bbox 204 931 313 951; x_wconf 63">Number:</span>
<span class="ocrx_word" id="word_1_309" title="bbox 333 931 408 951; x_wconf 91">805-A</span>
<span class="ocrx_word" id="word_1_310" title="bbox 869 931 947 951; x_wconf 94">House</span>
<span class="ocrx_word" id="word_1_311" title="bbox 957 931 1066 951; x_wconf 70">Number:</span>
<span class="ocrx_word" id="word_1_312" title="bbox 1087 931 1161 951; x_wconf 90">805-A</span>
<span class="ocrx_word" id="word_1_313" title="bbox 1622 931 1700 951; x_wconf 95">House</span>
<span class="ocrx_word" id="word_1_314" title="bbox 1710 931 1820 951; x_wconf 73">Number:</span>
<span class="ocrx_word" id="word_1_315" title="bbox 1840 931 1884 951; x_wconf 96">806</span>
</span>
            <span class="ocr_line" id="line_1_148"
                  title="bbox 114 957 2302 991; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_316" title="bbox 114 963 177 991; x_wconf 90">Age:</span>
<span class="ocrx_word" id="word_1_317" title="bbox 196 963 226 985; x_wconf 96">46</span>
<span class="ocrx_word" id="word_1_318" title="bbox 246 963 353 985; x_wconf 93">Gender:</span>
<span class="ocrx_word" id="word_1_319" title="bbox 373 963 446 985; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_320" title="bbox 693 957 765 979; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_321" title="bbox 777 957 795 979; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_322" title="bbox 867 963 931 991; x_wconf 86">Age:</span>
<span class="ocrx_word" id="word_1_323" title="bbox 949 963 981 985; x_wconf 96">40</span>
<span class="ocrx_word" id="word_1_324" title="bbox 999 963 1106 985; x_wconf 90">Gender:</span>
<span class="ocrx_word" id="word_1_325" title="bbox 1127 963 1237 985; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_326" title="bbox 1446 957 1518 979; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_327" title="bbox 1530 957 1549 979; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_328" title="bbox 1620 963 1684 991; x_wconf 82">Age:</span>
<span class="ocrx_word" id="word_1_329" title="bbox 1704 963 1732 985; x_wconf 95">36</span>
<span class="ocrx_word" id="word_1_330" title="bbox 1752 963 1859 985; x_wconf 82">Gender:</span>
<span class="ocrx_word" id="word_1_331" title="bbox 1880 963 1990 985; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_332" title="bbox 2200 957 2272 979; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_333" title="bbox 2283 957 2302 979; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_149"
                  title="bbox 691 987 2311 1023; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_334" title="bbox 691 987 805 1023; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_335" title="bbox 1444 987 1558 1023; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_336" title="bbox 2197 991 2311 1013; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_150"
                  title="bbox 112 1107 2343 1165; baseline -0.003 -11.987; x_size 49.769035; x_descenders 8.7690334; x_ascenders 16">
<span class="ocrx_word" id="word_1_337" title="bbox 112 1107 219 1165; x_wconf 13">L___</span>
<span class="ocrx_word" id="word_1_338" title="bbox 237 1107 272 1165; x_wconf 60">9]</span>
<span class="ocrx_word" id="word_1_339" title="bbox 647 1123 835 1147; x_wconf 86">REX0425223</span>
<span class="ocrx_word" id="word_1_340" title="bbox 869 1111 1021 1153; x_wconf 9">[L__1"]</span>
<span class="ocrx_word" id="word_1_341" title="bbox 1405 1123 1590 1147; x_wconf 88">HNL3818028</span>
<span class="ocrx_word" id="word_1_342" title="bbox 1622 1111 1774 1153; x_wconf 16">[L__72]</span>
<span class="ocrx_word" id="word_1_343" title="bbox 2154 1123 2343 1147; x_wconf 92">REX0263558</span>
</span>
            <span class="ocr_line" id="line_1_151"
                  title="bbox 116 1161 1918 1183; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_344" title="bbox 116 1161 205 1183; x_wconf 67">Name</span>
<span class="ocrx_word" id="word_1_345" title="bbox 199 1157 211 1193; x_wconf 67">:</span>
<span class="ocrx_word" id="word_1_346" title="bbox 226 1161 366 1183; x_wconf 93">Shantaram</span>
<span class="ocrx_word" id="word_1_347" title="bbox 378 1161 438 1183; x_wconf 91">Laad</span>
<span class="ocrx_word" id="word_1_348" title="bbox 869 1161 959 1183; x_wconf 65">Name:</span>
<span class="ocrx_word" id="word_1_349" title="bbox 979 1161 1057 1183; x_wconf 93">Sunita</span>
<span class="ocrx_word" id="word_1_350" title="bbox 1069 1161 1129 1183; x_wconf 92">Laad</span>
<span class="ocrx_word" id="word_1_351" title="bbox 1622 1161 1712 1183; x_wconf 85">Name</span>
<span class="ocrx_word" id="word_1_352" title="bbox 1705 1157 1717 1193; x_wconf 65">:</span>
<span class="ocrx_word" id="word_1_353" title="bbox 1732 1161 1846 1183; x_wconf 92">Chandan</span>
<span class="ocrx_word" id="word_1_354" title="bbox 1858 1161 1918 1183; x_wconf 92">Laad</span>
</span>
            <span class="ocr_line" id="line_1_152"
                  title="bbox 116 1195 2058 1217; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_355" title="bbox 116 1195 218 1217; x_wconf 94">Father's</span>
<span class="ocrx_word" id="word_1_356" title="bbox 230 1195 305 1217; x_wconf 83">Name</span>
<span class="ocrx_word" id="word_1_357" title="bbox 316 1201 319 1217; x_wconf 83">:</span>
<span class="ocrx_word" id="word_1_358" title="bbox 339 1195 460 1217; x_wconf 73">Saviaram</span>
<span class="ocrx_word" id="word_1_359" title="bbox 472 1195 532 1217; x_wconf 91">Laad</span>
<span class="ocrx_word" id="word_1_360" title="bbox 869 1195 1003 1217; x_wconf 96">Husband's</span>
<span class="ocrx_word" id="word_1_361" title="bbox 1015 1195 1104 1217; x_wconf 84">Name:</span>
<span class="ocrx_word" id="word_1_362" title="bbox 1125 1195 1265 1217; x_wconf 90">Shantaram</span>
<span class="ocrx_word" id="word_1_363" title="bbox 1277 1195 1337 1217; x_wconf 90">Laad</span>
<span class="ocrx_word" id="word_1_364" title="bbox 1622 1195 1724 1217; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_365" title="bbox 1736 1195 1826 1217; x_wconf 86">Name</span>
<span class="ocrx_word" id="word_1_366" title="bbox 1819 1191 1834 1227; x_wconf 77">:</span>
<span class="ocrx_word" id="word_1_367" title="bbox 1846 1195 1986 1217; x_wconf 93">Shantaram</span>
<span class="ocrx_word" id="word_1_368" title="bbox 1998 1195 2058 1217; x_wconf 89">Laad</span>
</span>
            <span class="ocr_line" id="line_1_153"
                  title="bbox 116 1229 1914 1249; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_369" title="bbox 116 1229 193 1249; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_370" title="bbox 204 1229 313 1249; x_wconf 46">Number:</span>
<span class="ocrx_word" id="word_1_371" title="bbox 333 1229 408 1249; x_wconf 92">806-A</span>
<span class="ocrx_word" id="word_1_372" title="bbox 869 1229 947 1249; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_373" title="bbox 957 1229 1066 1249; x_wconf 58">Number:</span>
<span class="ocrx_word" id="word_1_374" title="bbox 1087 1229 1161 1249; x_wconf 91">806-A</span>
<span class="ocrx_word" id="word_1_375" title="bbox 1622 1229 1700 1249; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_376" title="bbox 1710 1229 1820 1249; x_wconf 67">Number:</span>
<span class="ocrx_word" id="word_1_377" title="bbox 1840 1229 1914 1249; x_wconf 91">806-A</span>
</span>
            <span class="ocr_line" id="line_1_154"
                  title="bbox 114 1255 2302 1289; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_378" title="bbox 114 1261 177 1289; x_wconf 86">Age:</span>
<span class="ocrx_word" id="word_1_379" title="bbox 197 1261 226 1283; x_wconf 96">78</span>
<span class="ocrx_word" id="word_1_380" title="bbox 246 1261 353 1283; x_wconf 87">Gender:</span>
<span class="ocrx_word" id="word_1_381" title="bbox 373 1261 446 1283; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_382" title="bbox 693 1255 765 1277; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_383" title="bbox 777 1255 795 1277; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_384" title="bbox 867 1261 931 1289; x_wconf 78">Age:</span>
<span class="ocrx_word" id="word_1_385" title="bbox 951 1261 979 1283; x_wconf 93">73</span>
<span class="ocrx_word" id="word_1_386" title="bbox 999 1261 1106 1283; x_wconf 86">Gender:</span>
<span class="ocrx_word" id="word_1_387" title="bbox 1127 1261 1237 1283; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_388" title="bbox 1446 1255 1518 1277; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_389" title="bbox 1530 1255 1549 1277; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_390" title="bbox 1620 1261 1684 1289; x_wconf 87">Age:</span>
<span class="ocrx_word" id="word_1_391" title="bbox 1702 1261 1732 1283; x_wconf 95">46</span>
<span class="ocrx_word" id="word_1_392" title="bbox 1752 1261 1859 1283; x_wconf 92">Gender:</span>
<span class="ocrx_word" id="word_1_393" title="bbox 1880 1261 1952 1283; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_394" title="bbox 2200 1255 2272 1277; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_395" title="bbox 2283 1255 2302 1277; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_155"
                  title="bbox 691 1285 2311 1321; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_396" title="bbox 691 1285 805 1321; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_397" title="bbox 1444 1285 1558 1321; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_398" title="bbox 2197 1289 2311 1311; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_156"
                  title="bbox 232 1417 2342 1455; baseline 0 -10; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_399" title="bbox 232 1417 256 1435; x_wconf 95">13</span>
<span class="ocrx_word" id="word_1_400" title="bbox 647 1421 835 1445; x_wconf 88">REX0425215</span>
<span class="ocrx_word" id="word_1_401" title="bbox 985 1417 1010 1435; x_wconf 87">14</span>
<span class="ocrx_word" id="word_1_402" title="bbox 1401 1417 1589 1455; x_wconf 92">REX0425207</span>
<span class="ocrx_word" id="word_1_403" title="bbox 1738 1417 1762 1435; x_wconf 90">15</span>
<span class="ocrx_word" id="word_1_404" title="bbox 2154 1421 2342 1445; x_wconf 91">REX0425199</span>
</span>
            <span class="ocr_line" id="line_1_157"
                  title="bbox 116 1460 1914 1489; baseline 0 -6; x_size 29; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_405" title="bbox 116 1460 205 1483; x_wconf 69">Name:</span>
<span class="ocrx_word" id="word_1_406" title="bbox 226 1460 338 1483; x_wconf 92">Sandesh</span>
<span class="ocrx_word" id="word_1_407" title="bbox 350 1460 410 1483; x_wconf 92">Laad</span>
<span class="ocrx_word" id="word_1_408" title="bbox 869 1460 959 1483; x_wconf 72">Name:</span>
<span class="ocrx_word" id="word_1_409" title="bbox 979 1460 1067 1483; x_wconf 95">Bharati</span>
<span class="ocrx_word" id="word_1_410" title="bbox 1079 1460 1127 1489; x_wconf 96">Nag</span>
<span class="ocrx_word" id="word_1_411" title="bbox 1622 1460 1712 1483; x_wconf 57">Name:</span>
<span class="ocrx_word" id="word_1_412" title="bbox 1732 1460 1854 1483; x_wconf 92">Shambhu</span>
<span class="ocrx_word" id="word_1_413" title="bbox 1866 1460 1914 1489; x_wconf 96">Nag</span>
</span>
            <span class="ocr_line" id="line_1_158"
                  title="bbox 116 1494 2112 1523; baseline 0 -6; x_size 29; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_414" title="bbox 116 1494 218 1517; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_415" title="bbox 230 1494 305 1517; x_wconf 86">Name</span>
<span class="ocrx_word" id="word_1_416" title="bbox 316 1501 319 1516; x_wconf 75">:</span>
<span class="ocrx_word" id="word_1_417" title="bbox 339 1494 480 1517; x_wconf 93">Shantaram</span>
<span class="ocrx_word" id="word_1_418" title="bbox 492 1494 551 1517; x_wconf 92">Laad</span>
<span class="ocrx_word" id="word_1_419" title="bbox 869 1494 1003 1517; x_wconf 96">Husband's</span>
<span class="ocrx_word" id="word_1_420" title="bbox 1015 1494 1104 1517; x_wconf 64">Name:</span>
<span class="ocrx_word" id="word_1_421" title="bbox 1125 1494 1333 1517; x_wconf 91">Dhirendrakumar</span>
<span class="ocrx_word" id="word_1_422" title="bbox 1342 1494 1391 1523; x_wconf 96">Nag</span>
<span class="ocrx_word" id="word_1_423" title="bbox 1622 1494 1724 1517; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_424" title="bbox 1736 1494 1826 1517; x_wconf 88">Name</span>
<span class="ocrx_word" id="word_1_425" title="bbox 1818 1490 1831 1527; x_wconf 72">:</span>
<span class="ocrx_word" id="word_1_426" title="bbox 1846 1494 2054 1517; x_wconf 92">Dhirendrakumar</span>
<span class="ocrx_word" id="word_1_427" title="bbox 2064 1494 2112 1523; x_wconf 96">Nag</span>
</span>
            <span class="ocr_line" id="line_1_159"
                  title="bbox 116 1528 2286 1557; baseline 0 -8; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_428" title="bbox 116 1528 193 1549; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_429" title="bbox 204 1528 313 1549; x_wconf 83">Number</span>
<span class="ocrx_word" id="word_1_430" title="bbox 309 1522 322 1559; x_wconf 76">:</span>
<span class="ocrx_word" id="word_1_431" title="bbox 333 1528 408 1549; x_wconf 92">806-A</span>
<span class="ocrx_word" id="word_1_432" title="bbox 777 1554 779 1557; x_wconf 26">;</span>
<span class="ocrx_word" id="word_1_433" title="bbox 869 1528 947 1549; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_434" title="bbox 957 1528 1066 1549; x_wconf 78">Number</span>
<span class="ocrx_word" id="word_1_435" title="bbox 1062 1522 1072 1559; x_wconf 78">:</span>
<span class="ocrx_word" id="word_1_436" title="bbox 1087 1528 1131 1549; x_wconf 95">807</span>
<span class="ocrx_word" id="word_1_437" title="bbox 1530 1554 1532 1557; x_wconf 27">;</span>
<span class="ocrx_word" id="word_1_438" title="bbox 1622 1528 1700 1549; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_439" title="bbox 1710 1528 1820 1549; x_wconf 81">Number</span>
<span class="ocrx_word" id="word_1_440" title="bbox 1815 1522 1825 1559; x_wconf 81">:</span>
<span class="ocrx_word" id="word_1_441" title="bbox 1840 1528 1884 1549; x_wconf 94">807</span>
<span class="ocrx_word" id="word_1_442" title="bbox 2283 1554 2286 1557; x_wconf 0">:</span>
</span>
            <span class="ocr_line" id="line_1_160"
                  title="bbox 114 1554 2302 1589; baseline 0 -6; x_size 35; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_443" title="bbox 114 1560 177 1589; x_wconf 77">Age:</span>
<span class="ocrx_word" id="word_1_444" title="bbox 196 1560 226 1583; x_wconf 96">42</span>
<span class="ocrx_word" id="word_1_445" title="bbox 246 1560 353 1583; x_wconf 95">Gender:</span>
<span class="ocrx_word" id="word_1_446" title="bbox 373 1560 446 1583; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_447" title="bbox 693 1554 765 1577; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_448" title="bbox 777 1560 795 1577; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_449" title="bbox 867 1560 931 1589; x_wconf 68">Age:</span>
<span class="ocrx_word" id="word_1_450" title="bbox 951 1560 979 1583; x_wconf 96">82</span>
<span class="ocrx_word" id="word_1_451" title="bbox 999 1560 1106 1583; x_wconf 91">Gender:</span>
<span class="ocrx_word" id="word_1_452" title="bbox 1127 1560 1237 1583; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_453" title="bbox 1446 1554 1518 1577; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_454" title="bbox 1530 1560 1549 1577; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_455" title="bbox 1620 1560 1684 1589; x_wconf 88">Age:</span>
<span class="ocrx_word" id="word_1_456" title="bbox 1704 1560 1728 1583; x_wconf 93">51</span>
<span class="ocrx_word" id="word_1_457" title="bbox 1752 1560 1859 1583; x_wconf 95">Gender:</span>
<span class="ocrx_word" id="word_1_458" title="bbox 1880 1560 1952 1583; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_459" title="bbox 2200 1554 2272 1577; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_460" title="bbox 2283 1560 2302 1577; x_wconf 93">is</span>
</span>
            <span class="ocr_line" id="line_1_161"
                  title="bbox 691 1584 2311 1621; baseline 0 -10; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_461" title="bbox 691 1584 805 1621; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_462" title="bbox 1444 1584 1558 1621; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_463" title="bbox 2197 1588 2311 1611; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_162"
                  title="bbox 232 1714 2342 1744; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_464" title="bbox 232 1714 256 1732; x_wconf 96">16</span>
<span class="ocrx_word" id="word_1_465" title="bbox 651 1720 835 1744; x_wconf 91">HNL1383009</span>
<span class="ocrx_word" id="word_1_466" title="bbox 963 1714 1009 1732; x_wconf 94">#17</span>
<span class="ocrx_word" id="word_1_467" title="bbox 1401 1720 1589 1744; x_wconf 92">REX0383489</span>
<span class="ocrx_word" id="word_1_468" title="bbox 1738 1714 1762 1732; x_wconf 92">18</span>
<span class="ocrx_word" id="word_1_469" title="bbox 2154 1720 2342 1744; x_wconf 86">REX0383653</span>
</span>
            <span class="ocr_line" id="line_1_163"
                  title="bbox 116 1758 1941 1786; baseline 0 -6; x_size 28; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_470" title="bbox 116 1758 205 1780; x_wconf 91">Name</span>
<span class="ocrx_word" id="word_1_471" title="bbox 193 1754 205 1790; x_wconf 69">:</span>
<span class="ocrx_word" id="word_1_472" title="bbox 226 1758 296 1786; x_wconf 88">Lipika</span>
<span class="ocrx_word" id="word_1_473" title="bbox 308 1758 356 1786; x_wconf 96">Nag</span>
<span class="ocrx_word" id="word_1_474" title="bbox 869 1758 959 1780; x_wconf 77">Name</span>
<span class="ocrx_word" id="word_1_475" title="bbox 952 1754 964 1790; x_wconf 71">:</span>
<span class="ocrx_word" id="word_1_476" title="bbox 979 1758 1095 1780; x_wconf 92">Narendra</span>
<span class="ocrx_word" id="word_1_477" title="bbox 1107 1758 1196 1780; x_wconf 86">Phadte</span>
<span class="ocrx_word" id="word_1_478" title="bbox 1622 1758 1712 1780; x_wconf 83">Name</span>
<span class="ocrx_word" id="word_1_479" title="bbox 1705 1754 1717 1790; x_wconf 71">:</span>
<span class="ocrx_word" id="word_1_480" title="bbox 1732 1758 1840 1780; x_wconf 92">Namrata</span>
<span class="ocrx_word" id="word_1_481" title="bbox 1852 1758 1941 1780; x_wconf 90">Phadte</span>
</span>
            <span class="ocr_line" id="line_1_164"
                  title="bbox 116 1792 2095 1820; baseline 0 -6; x_size 28; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_482" title="bbox 116 1792 250 1814; x_wconf 96">Husband's</span>
<span class="ocrx_word" id="word_1_483" title="bbox 262 1792 337 1814; x_wconf 71">Name</span>
<span class="ocrx_word" id="word_1_484" title="bbox 348 1798 351 1814; x_wconf 54">-</span>
<span class="ocrx_word" id="word_1_485" title="bbox 371 1792 494 1814; x_wconf 91">Shambhu</span>
<span class="ocrx_word" id="word_1_486" title="bbox 505 1792 553 1820; x_wconf 96">Nag</span>
<span class="ocrx_word" id="word_1_487" title="bbox 869 1792 971 1814; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_488" title="bbox 983 1792 1058 1814; x_wconf 68">Name</span>
<span class="ocrx_word" id="word_1_489" title="bbox 1069 1798 1072 1814; x_wconf 68">:</span>
<span class="ocrx_word" id="word_1_490" title="bbox 1093 1792 1159 1814; x_wconf 93">Datta</span>
<span class="ocrx_word" id="word_1_491" title="bbox 1171 1792 1260 1814; x_wconf 90">Phadte</span>
<span class="ocrx_word" id="word_1_492" title="bbox 1622 1792 1756 1814; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_493" title="bbox 1768 1792 1858 1814; x_wconf 76">Name:</span>
<span class="ocrx_word" id="word_1_494" title="bbox 1878 1792 1994 1814; x_wconf 92">Narendra</span>
<span class="ocrx_word" id="word_1_495" title="bbox 2006 1792 2095 1814; x_wconf 92">Phadte</span>
</span>
            <span class="ocr_line" id="line_1_165"
                  title="bbox 116 1826 1904 1846; baseline 0 0; x_size 25.060951; x_descenders 5.0609522; x_ascenders 5.5715227">
<span class="ocrx_word" id="word_1_496" title="bbox 116 1826 193 1846; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_497" title="bbox 204 1826 313 1846; x_wconf 87">Number</span>
<span class="ocrx_word" id="word_1_498" title="bbox 307 1822 319 1856; x_wconf 86">:</span>
<span class="ocrx_word" id="word_1_499" title="bbox 333 1826 378 1846; x_wconf 96">807</span>
<span class="ocrx_word" id="word_1_500" title="bbox 869 1826 947 1846; x_wconf 94">House</span>
<span class="ocrx_word" id="word_1_501" title="bbox 957 1826 1066 1846; x_wconf 76">Number:</span>
<span class="ocrx_word" id="word_1_502" title="bbox 1087 1826 1151 1846; x_wconf 88">807/1</span>
<span class="ocrx_word" id="word_1_503" title="bbox 1622 1826 1700 1846; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_504" title="bbox 1710 1826 1820 1846; x_wconf 70">Number:</span>
<span class="ocrx_word" id="word_1_505" title="bbox 1840 1826 1904 1846; x_wconf 10">807/14</span>
</span>
            <span class="ocr_line" id="line_1_166"
                  title="bbox 114 1852 2302 1886; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_506" title="bbox 114 1858 177 1886; x_wconf 86">Age:</span>
<span class="ocrx_word" id="word_1_507" title="bbox 196 1858 226 1880; x_wconf 95">44</span>
<span class="ocrx_word" id="word_1_508" title="bbox 246 1858 353 1880; x_wconf 91">Gender:</span>
<span class="ocrx_word" id="word_1_509" title="bbox 374 1858 484 1880; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_510" title="bbox 693 1852 765 1874; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_511" title="bbox 777 1852 795 1874; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_512" title="bbox 867 1858 931 1886; x_wconf 84">Age:</span>
<span class="ocrx_word" id="word_1_513" title="bbox 949 1858 975 1880; x_wconf 96">61</span>
<span class="ocrx_word" id="word_1_514" title="bbox 999 1858 1106 1880; x_wconf 92">Gender:</span>
<span class="ocrx_word" id="word_1_515" title="bbox 1127 1858 1199 1880; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_516" title="bbox 1446 1852 1518 1874; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_517" title="bbox 1530 1852 1549 1874; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_518" title="bbox 1620 1858 1684 1886; x_wconf 75">Age:</span>
<span class="ocrx_word" id="word_1_519" title="bbox 1704 1858 1732 1880; x_wconf 95">54</span>
<span class="ocrx_word" id="word_1_520" title="bbox 1752 1858 1859 1880; x_wconf 83">Gender:</span>
<span class="ocrx_word" id="word_1_521" title="bbox 1880 1858 1990 1880; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_522" title="bbox 2200 1852 2272 1874; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_523" title="bbox 2283 1852 2302 1874; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_167"
                  title="bbox 691 1882 2311 1918; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_524" title="bbox 691 1882 805 1918; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_525" title="bbox 1444 1882 1558 1918; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_526" title="bbox 2197 1886 2311 1908; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_168"
                  title="bbox 232 2014 2343 2044; baseline 0 -2; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_527" title="bbox 232 2014 256 2032; x_wconf 94">19</span>
<span class="ocrx_word" id="word_1_528" title="bbox 647 2018 835 2042; x_wconf 89">REX0383513</span>
<span class="ocrx_word" id="word_1_529" title="bbox 983 2014 1009 2032; x_wconf 96">20</span>
<span class="ocrx_word" id="word_1_530" title="bbox 1399 2018 1589 2044; x_wconf 90">UQA0389122</span>
<span class="ocrx_word" id="word_1_531" title="bbox 1736 2014 1760 2032; x_wconf 80">21</span>
<span class="ocrx_word" id="word_1_532" title="bbox 2158 2018 2343 2042; x_wconf 90">HNL6962278</span>
</span>
            <span class="ocr_line" id="line_1_169"
                  title="bbox 116 2058 1862 2086; baseline 0 -6; x_size 28; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_533" title="bbox 116 2058 205 2080; x_wconf 90">Name</span>
<span class="ocrx_word" id="word_1_534" title="bbox 199 2054 211 2090; x_wconf 67">:</span>
<span class="ocrx_word" id="word_1_535" title="bbox 226 2058 322 2080; x_wconf 93">Nandan</span>
<span class="ocrx_word" id="word_1_536" title="bbox 334 2058 423 2080; x_wconf 89">Phadte</span>
<span class="ocrx_word" id="word_1_537" title="bbox 869 2058 959 2080; x_wconf 91">Name</span>
<span class="ocrx_word" id="word_1_538" title="bbox 952 2054 964 2090; x_wconf 61">:</span>
<span class="ocrx_word" id="word_1_539" title="bbox 979 2058 1090 2080; x_wconf 93">Abhishek</span>
<span class="ocrx_word" id="word_1_540" title="bbox 1103 2058 1181 2080; x_wconf 92">Jotkar</span>
<span class="ocrx_word" id="word_1_541" title="bbox 1622 2058 1712 2080; x_wconf 52">Name:</span>
<span class="ocrx_word" id="word_1_542" title="bbox 1732 2058 1796 2086; x_wconf 96">Maya</span>
<span class="ocrx_word" id="word_1_543" title="bbox 1808 2058 1862 2080; x_wconf 96">Naik</span>
</span>
            <span class="ocr_line" id="line_1_170"
                  title="bbox 116 2092 2026 2114; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_544" title="bbox 116 2092 218 2114; x_wconf 95">Father's</span>
<span class="ocrx_word" id="word_1_545" title="bbox 230 2092 305 2114; x_wconf 84">Name</span>
<span class="ocrx_word" id="word_1_546" title="bbox 316 2098 319 2114; x_wconf 73">:</span>
<span class="ocrx_word" id="word_1_547" title="bbox 339 2092 456 2114; x_wconf 93">Narendra</span>
<span class="ocrx_word" id="word_1_548" title="bbox 468 2092 557 2114; x_wconf 92">Phadte</span>
<span class="ocrx_word" id="word_1_549" title="bbox 869 2092 971 2114; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_550" title="bbox 983 2092 1058 2114; x_wconf 89">Name</span>
<span class="ocrx_word" id="word_1_551" title="bbox 1069 2098 1072 2114; x_wconf 73">:</span>
<span class="ocrx_word" id="word_1_552" title="bbox 1091 2092 1151 2114; x_wconf 91">Vittal</span>
<span class="ocrx_word" id="word_1_553" title="bbox 1161 2092 1239 2114; x_wconf 93">Jotkar</span>
<span class="ocrx_word" id="word_1_554" title="bbox 1622 2092 1756 2114; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_555" title="bbox 1768 2092 1858 2114; x_wconf 66">Name:</span>
<span class="ocrx_word" id="word_1_556" title="bbox 1878 2092 1960 2114; x_wconf 96">Mohan</span>
<span class="ocrx_word" id="word_1_557" title="bbox 1972 2092 2026 2114; x_wconf 95">Naik</span>
</span>
            <span class="ocr_line" id="line_1_171"
                  title="bbox 116 2126 1914 2146; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_558" title="bbox 116 2126 193 2146; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_559" title="bbox 204 2126 313 2146; x_wconf 81">Number</span>
<span class="ocrx_word" id="word_1_560" title="bbox 309 2119 319 2156; x_wconf 60">:</span>
<span class="ocrx_word" id="word_1_561" title="bbox 333 2126 398 2146; x_wconf 40">807/14</span>
<span class="ocrx_word" id="word_1_562" title="bbox 869 2126 947 2146; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_563" title="bbox 957 2126 1066 2146; x_wconf 73">Number</span>
<span class="ocrx_word" id="word_1_564" title="bbox 1062 2119 1072 2156; x_wconf 57">:</span>
<span class="ocrx_word" id="word_1_565" title="bbox 1087 2126 1151 2146; x_wconf 62">808/1</span>
<span class="ocrx_word" id="word_1_566" title="bbox 1622 2126 1700 2146; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_567" title="bbox 1710 2126 1820 2146; x_wconf 69">Number:</span>
<span class="ocrx_word" id="word_1_568" title="bbox 1840 2126 1914 2146; x_wconf 89">808-A</span>
</span>
            <span class="ocr_line" id="line_1_172"
                  title="bbox 114 2152 2302 2186; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_569" title="bbox 114 2158 177 2186; x_wconf 89">Age:</span>
<span class="ocrx_word" id="word_1_570" title="bbox 196 2158 222 2180; x_wconf 95">21</span>
<span class="ocrx_word" id="word_1_571" title="bbox 246 2158 353 2180; x_wconf 90">Gender:</span>
<span class="ocrx_word" id="word_1_572" title="bbox 373 2158 446 2180; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_573" title="bbox 693 2152 765 2174; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_574" title="bbox 777 2152 795 2174; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_575" title="bbox 867 2158 931 2186; x_wconf 77">Age:</span>
<span class="ocrx_word" id="word_1_576" title="bbox 951 2158 979 2180; x_wconf 95">38</span>
<span class="ocrx_word" id="word_1_577" title="bbox 999 2158 1106 2180; x_wconf 94">Gender:</span>
<span class="ocrx_word" id="word_1_578" title="bbox 1127 2158 1199 2180; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_579" title="bbox 1446 2152 1518 2174; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_580" title="bbox 1530 2152 1549 2174; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_581" title="bbox 1620 2158 1684 2186; x_wconf 90">Age:</span>
<span class="ocrx_word" id="word_1_582" title="bbox 1702 2158 1728 2180; x_wconf 96">61</span>
<span class="ocrx_word" id="word_1_583" title="bbox 1752 2158 1859 2180; x_wconf 88">Gender:</span>
<span class="ocrx_word" id="word_1_584" title="bbox 1880 2158 1990 2180; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_585" title="bbox 2200 2152 2272 2174; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_586" title="bbox 2283 2152 2302 2174; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_173"
                  title="bbox 691 2182 2311 2218; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_587" title="bbox 691 2182 805 2218; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_588" title="bbox 1444 2182 1558 2218; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_589" title="bbox 2197 2186 2311 2208; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_174"
                  title="bbox 230 2311 2342 2342; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_590" title="bbox 230 2311 256 2330; x_wconf 95">22</span>
<span class="ocrx_word" id="word_1_591" title="bbox 651 2317 831 2342; x_wconf 91">HNL6962351</span>
<span class="ocrx_word" id="word_1_592" title="bbox 983 2311 1009 2330; x_wconf 89">23</span>
<span class="ocrx_word" id="word_1_593" title="bbox 1405 2317 1589 2342; x_wconf 92">HNL1382084</span>
<span class="ocrx_word" id="word_1_594" title="bbox 1736 2311 1764 2330; x_wconf 95">24</span>
<span class="ocrx_word" id="word_1_595" title="bbox 2154 2317 2342 2342; x_wconf 91">REX0299115</span>
</span>
            <span class="ocr_line" id="line_1_175"
                  title="bbox 116 2355 1876 2378; baseline 0 0; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_596" title="bbox 116 2355 205 2378; x_wconf 78">Name</span>
<span class="ocrx_word" id="word_1_597" title="bbox 198 2351 211 2388; x_wconf 65">:</span>
<span class="ocrx_word" id="word_1_598" title="bbox 226 2355 308 2378; x_wconf 96">Mohan</span>
<span class="ocrx_word" id="word_1_599" title="bbox 320 2355 374 2378; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_600" title="bbox 869 2355 959 2378; x_wconf 55">Name:</span>
<span class="ocrx_word" id="word_1_601" title="bbox 979 2355 1101 2378; x_wconf 92">Shraddha</span>
<span class="ocrx_word" id="word_1_602" title="bbox 1113 2355 1167 2378; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_603" title="bbox 1622 2355 1712 2378; x_wconf 73">Name:</span>
<span class="ocrx_word" id="word_1_604" title="bbox 1732 2355 1810 2378; x_wconf 90">Monali</span>
<span class="ocrx_word" id="word_1_605" title="bbox 1822 2355 1876 2378; x_wconf 95">Naik</span>
</span>
            <span class="ocr_line" id="line_1_176"
                  title="bbox 116 2389 1994 2412; baseline 0 0; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_606" title="bbox 116 2389 218 2412; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_607" title="bbox 230 2389 305 2412; x_wconf 76">Name</span>
<span class="ocrx_word" id="word_1_608" title="bbox 316 2396 319 2411; x_wconf 76">:</span>
<span class="ocrx_word" id="word_1_609" title="bbox 339 2389 430 2412; x_wconf 91">Noraso</span>
<span class="ocrx_word" id="word_1_610" title="bbox 441 2389 496 2412; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_611" title="bbox 869 2389 971 2412; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_612" title="bbox 983 2389 1058 2412; x_wconf 84">Name</span>
<span class="ocrx_word" id="word_1_613" title="bbox 1069 2396 1072 2411; x_wconf 69">:</span>
<span class="ocrx_word" id="word_1_614" title="bbox 1093 2389 1175 2412; x_wconf 96">Mohan</span>
<span class="ocrx_word" id="word_1_615" title="bbox 1187 2389 1241 2412; x_wconf 95">Naik</span>
<span class="ocrx_word" id="word_1_616" title="bbox 1622 2389 1724 2412; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_617" title="bbox 1736 2389 1826 2412; x_wconf 84">Name</span>
<span class="ocrx_word" id="word_1_618" title="bbox 1818 2385 1834 2422; x_wconf 75">:</span>
<span class="ocrx_word" id="word_1_619" title="bbox 1846 2389 1928 2412; x_wconf 96">Mohan</span>
<span class="ocrx_word" id="word_1_620" title="bbox 1940 2389 1994 2412; x_wconf 96">Naik</span>
</span>
            <span class="ocr_line" id="line_1_177"
                  title="bbox 116 2423 2286 2452; baseline 0 -8; x_size 26.313999; x_descenders 5.3140001; x_ascenders 5.8500986">
<span class="ocrx_word" id="word_1_621" title="bbox 116 2423 193 2444; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_622" title="bbox 204 2423 313 2444; x_wconf 92">Number</span>
<span class="ocrx_word" id="word_1_623" title="bbox 307 2419 322 2454; x_wconf 88">:</span>
<span class="ocrx_word" id="word_1_624" title="bbox 333 2423 408 2444; x_wconf 89">808-A</span>
<span class="ocrx_word" id="word_1_625" title="bbox 777 2449 779 2452; x_wconf 0">.</span>
<span class="ocrx_word" id="word_1_626" title="bbox 869 2423 947 2444; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_627" title="bbox 957 2423 1066 2444; x_wconf 86">Number</span>
<span class="ocrx_word" id="word_1_628" title="bbox 1060 2419 1073 2454; x_wconf 84">:</span>
<span class="ocrx_word" id="word_1_629" title="bbox 1087 2423 1161 2444; x_wconf 84">808-A</span>
<span class="ocrx_word" id="word_1_630" title="bbox 1530 2449 1532 2452; x_wconf 0">:</span>
<span class="ocrx_word" id="word_1_631" title="bbox 1622 2423 1700 2444; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_632" title="bbox 1710 2423 1820 2444; x_wconf 76">Number</span>
<span class="ocrx_word" id="word_1_633" title="bbox 1813 2419 1828 2454; x_wconf 76">:</span>
<span class="ocrx_word" id="word_1_634" title="bbox 1840 2423 1914 2444; x_wconf 84">808-A</span>
<span class="ocrx_word" id="word_1_635" title="bbox 2283 2449 2286 2452; x_wconf 0">.</span>
</span>
            <span class="ocr_line" id="line_1_178"
                  title="bbox 114 2449 2302 2484; baseline 0 -6; x_size 35; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_636" title="bbox 114 2455 177 2484; x_wconf 86">Age:</span>
<span class="ocrx_word" id="word_1_637" title="bbox 196 2455 222 2478; x_wconf 96">61</span>
<span class="ocrx_word" id="word_1_638" title="bbox 246 2455 353 2478; x_wconf 96">Gender:</span>
<span class="ocrx_word" id="word_1_639" title="bbox 373 2455 446 2478; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_640" title="bbox 693 2449 765 2472; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_641" title="bbox 777 2455 795 2472; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_642" title="bbox 867 2455 931 2484; x_wconf 70">Age:</span>
<span class="ocrx_word" id="word_1_643" title="bbox 951 2455 979 2478; x_wconf 96">35</span>
<span class="ocrx_word" id="word_1_644" title="bbox 999 2455 1106 2478; x_wconf 94">Gender:</span>
<span class="ocrx_word" id="word_1_645" title="bbox 1127 2455 1237 2478; x_wconf 95">FEMALE</span>
<span class="ocrx_word" id="word_1_646" title="bbox 1446 2449 1518 2472; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_647" title="bbox 1530 2455 1549 2472; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_648" title="bbox 1620 2455 1684 2484; x_wconf 66">Age:</span>
<span class="ocrx_word" id="word_1_649" title="bbox 1704 2455 1732 2478; x_wconf 96">32</span>
<span class="ocrx_word" id="word_1_650" title="bbox 1752 2455 1859 2478; x_wconf 94">Gender:</span>
<span class="ocrx_word" id="word_1_651" title="bbox 1880 2455 1990 2478; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_652" title="bbox 2200 2449 2272 2472; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_653" title="bbox 2283 2455 2302 2472; x_wconf 93">is</span>
</span>
            <span class="ocr_line" id="line_1_179"
                  title="bbox 691 2479 2311 2516; baseline 0 -10; x_size 28.962944; x_descenders 5.9629431; x_ascenders 6">
<span class="ocrx_word" id="word_1_654" title="bbox 691 2479 805 2516; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_655" title="bbox 1444 2479 1558 2516; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_656" title="bbox 2197 2483 2311 2506; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_180"
                  title="bbox 230 2611 2342 2639; baseline 0 0; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_657" title="bbox 230 2611 256 2629; x_wconf 95">25</span>
<span class="ocrx_word" id="word_1_658" title="bbox 647 2615 835 2639; x_wconf 86">REX0356543</span>
<span class="ocrx_word" id="word_1_659" title="bbox 983 2611 1009 2629; x_wconf 96">26</span>
<span class="ocrx_word" id="word_1_660" title="bbox 1405 2615 1589 2639; x_wconf 90">HNL3818044</span>
<span class="ocrx_word" id="word_1_661" title="bbox 1736 2611 1762 2629; x_wconf 93">27</span>
<span class="ocrx_word" id="word_1_662" title="bbox 2158 2615 2342 2639; x_wconf 91">HNL3818077</span>
</span>
            <span class="ocr_line" id="line_1_181"
                  title="bbox 116 2655 1898 2677; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_663" title="bbox 116 2655 205 2677; x_wconf 70">Name:</span>
<span class="ocrx_word" id="word_1_664" title="bbox 226 2655 298 2677; x_wconf 94">Shruti</span>
<span class="ocrx_word" id="word_1_665" title="bbox 310 2655 364 2677; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_666" title="bbox 869 2655 959 2677; x_wconf 48">Name:</span>
<span class="ocrx_word" id="word_1_667" title="bbox 979 2655 1107 2677; x_wconf 91">Sadanand</span>
<span class="ocrx_word" id="word_1_668" title="bbox 1119 2655 1173 2677; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_669" title="bbox 1622 2655 1712 2677; x_wconf 50">Name:</span>
<span class="ocrx_word" id="word_1_670" title="bbox 1732 2655 1832 2677; x_wconf 91">Suvidha</span>
<span class="ocrx_word" id="word_1_671" title="bbox 1844 2655 1898 2677; x_wconf 96">Naik</span>
</span>
            <span class="ocr_line" id="line_1_182"
                  title="bbox 116 2689 2072 2711; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_672" title="bbox 116 2689 218 2711; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_673" title="bbox 230 2689 305 2711; x_wconf 88">Name</span>
<span class="ocrx_word" id="word_1_674" title="bbox 316 2695 319 2711; x_wconf 68">:</span>
<span class="ocrx_word" id="word_1_675" title="bbox 339 2689 422 2711; x_wconf 96">Mohan</span>
<span class="ocrx_word" id="word_1_676" title="bbox 433 2689 488 2711; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_677" title="bbox 869 2689 971 2711; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_678" title="bbox 983 2689 1058 2711; x_wconf 75">Name</span>
<span class="ocrx_word" id="word_1_679" title="bbox 1069 2695 1072 2711; x_wconf 70">:</span>
<span class="ocrx_word" id="word_1_680" title="bbox 1093 2689 1167 2711; x_wconf 92">Narso</span>
<span class="ocrx_word" id="word_1_681" title="bbox 1179 2689 1233 2711; x_wconf 96">Naik</span>
<span class="ocrx_word" id="word_1_682" title="bbox 1622 2689 1756 2711; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_683" title="bbox 1768 2689 1858 2711; x_wconf 71">Name:</span>
<span class="ocrx_word" id="word_1_684" title="bbox 1878 2689 2006 2711; x_wconf 90">Sadanand</span>
<span class="ocrx_word" id="word_1_685" title="bbox 2018 2689 2072 2711; x_wconf 96">Naik</span>
</span>
            <span class="ocr_line" id="line_1_183"
                  title="bbox 116 2723 1912 2743; baseline 0 0; x_size 25.060951; x_descenders 5.0609522; x_ascenders 5.5715227">
<span class="ocrx_word" id="word_1_686" title="bbox 116 2723 193 2743; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_687" title="bbox 204 2723 313 2743; x_wconf 89">Number</span>
<span class="ocrx_word" id="word_1_688" title="bbox 307 2719 322 2753; x_wconf 86">:</span>
<span class="ocrx_word" id="word_1_689" title="bbox 333 2723 408 2743; x_wconf 92">808-A</span>
<span class="ocrx_word" id="word_1_690" title="bbox 869 2723 947 2743; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_691" title="bbox 957 2723 1066 2743; x_wconf 82">Number</span>
<span class="ocrx_word" id="word_1_692" title="bbox 1060 2719 1075 2753; x_wconf 82">:</span>
<span class="ocrx_word" id="word_1_693" title="bbox 1087 2723 1159 2743; x_wconf 92">808-B</span>
<span class="ocrx_word" id="word_1_694" title="bbox 1622 2723 1700 2743; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_695" title="bbox 1710 2723 1820 2743; x_wconf 78">Number</span>
<span class="ocrx_word" id="word_1_696" title="bbox 1813 2719 1828 2753; x_wconf 78">:</span>
<span class="ocrx_word" id="word_1_697" title="bbox 1840 2723 1912 2743; x_wconf 81">808-B</span>
</span>
            <span class="ocr_line" id="line_1_184"
                  title="bbox 114 2749 2302 2783; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_698" title="bbox 114 2755 177 2783; x_wconf 84">Age:</span>
<span class="ocrx_word" id="word_1_699" title="bbox 196 2755 226 2777; x_wconf 95">24</span>
<span class="ocrx_word" id="word_1_700" title="bbox 246 2755 353 2777; x_wconf 92">Gender:</span>
<span class="ocrx_word" id="word_1_701" title="bbox 374 2755 484 2777; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_702" title="bbox 693 2749 765 2771; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_703" title="bbox 777 2749 795 2771; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_704" title="bbox 867 2755 931 2783; x_wconf 65">Age:</span>
<span class="ocrx_word" id="word_1_705" title="bbox 951 2755 979 2777; x_wconf 93">52</span>
<span class="ocrx_word" id="word_1_706" title="bbox 999 2755 1106 2777; x_wconf 93">Gender:</span>
<span class="ocrx_word" id="word_1_707" title="bbox 1127 2755 1199 2777; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_708" title="bbox 1446 2749 1518 2771; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_709" title="bbox 1530 2749 1549 2771; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_710" title="bbox 1620 2755 1684 2783; x_wconf 90">Age:</span>
<span class="ocrx_word" id="word_1_711" title="bbox 1702 2755 1732 2777; x_wconf 94">44</span>
<span class="ocrx_word" id="word_1_712" title="bbox 1752 2755 1859 2777; x_wconf 87">Gender:</span>
<span class="ocrx_word" id="word_1_713" title="bbox 1880 2755 1990 2777; x_wconf 95">FEMALE</span>
<span class="ocrx_word" id="word_1_714" title="bbox 2200 2749 2272 2771; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_715" title="bbox 2283 2749 2302 2771; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_185"
                  title="bbox 691 2779 2311 2815; baseline 0 -10; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_716" title="bbox 691 2779 805 2815; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_717" title="bbox 1444 2779 1558 2815; x_wconf 96">Available</span>
<span class="ocrx_word" id="word_1_718" title="bbox 2197 2783 2311 2805; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_186"
                  title="bbox 230 2909 2342 2949; baseline 0 -10; x_size 29.428314; x_descenders 5.9429226; x_ascenders 6.5424695">
<span class="ocrx_word" id="word_1_719" title="bbox 230 2909 256 2927; x_wconf 95">28</span>
<span class="ocrx_word" id="word_1_720" title="bbox 651 2911 835 2949; x_wconf 88">HNL5724984</span>
<span class="ocrx_word" id="word_1_721" title="bbox 983 2909 1009 2927; x_wconf 95">29</span>
<span class="ocrx_word" id="word_1_722" title="bbox 1401 2915 1589 2939; x_wconf 92">REX0299164</span>
<span class="ocrx_word" id="word_1_723" title="bbox 1738 2909 1762 2927; x_wconf 95">30</span>
<span class="ocrx_word" id="word_1_724" title="bbox 2154 2915 2342 2939; x_wconf 92">REX0323782</span>
</span>
            <span class="ocr_line" id="line_1_187"
                  title="bbox 116 2953 1960 2975; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_725" title="bbox 116 2953 205 2975; x_wconf 71">Name</span>
<span class="ocrx_word" id="word_1_726" title="bbox 199 2949 214 2985; x_wconf 71">:</span>
<span class="ocrx_word" id="word_1_727" title="bbox 226 2953 422 2975; x_wconf 91">Sharadchandra</span>
<span class="ocrx_word" id="word_1_728" title="bbox 434 2953 524 2975; x_wconf 96">Kadam</span>
<span class="ocrx_word" id="word_1_729" title="bbox 869 2953 959 2975; x_wconf 78">Name:</span>
<span class="ocrx_word" id="word_1_730" title="bbox 979 2953 1073 2975; x_wconf 95">Sheetal</span>
<span class="ocrx_word" id="word_1_731" title="bbox 1085 2953 1175 2975; x_wconf 96">Kadam</span>
<span class="ocrx_word" id="word_1_732" title="bbox 1622 2953 1712 2975; x_wconf 65">Name:</span>
<span class="ocrx_word" id="word_1_733" title="bbox 1732 2953 1860 2975; x_wconf 95">Shashank</span>
<span class="ocrx_word" id="word_1_734" title="bbox 1870 2953 1960 2975; x_wconf 95">Kadam</span>
</span>
            <span class="ocr_line" id="line_1_188"
                  title="bbox 116 2987 2058 3009; baseline 0 0; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_735" title="bbox 116 2987 218 3009; x_wconf 95">Father's</span>
<span class="ocrx_word" id="word_1_736" title="bbox 230 2987 305 3009; x_wconf 87">Name</span>
<span class="ocrx_word" id="word_1_737" title="bbox 316 2993 319 3009; x_wconf 75">:</span>
<span class="ocrx_word" id="word_1_738" title="bbox 340 2987 440 3009; x_wconf 96">Laxman</span>
<span class="ocrx_word" id="word_1_739" title="bbox 452 2987 542 3009; x_wconf 96">Kadam</span>
<span class="ocrx_word" id="word_1_740" title="bbox 869 2987 1003 3009; x_wconf 95">Husband's</span>
<span class="ocrx_word" id="word_1_741" title="bbox 1015 2987 1104 3009; x_wconf 86">Name:</span>
<span class="ocrx_word" id="word_1_742" title="bbox 1125 2987 1338 3009; x_wconf 91">Sharashchandre</span>
<span class="ocrx_word" id="word_1_743" title="bbox 1622 2987 1724 3009; x_wconf 96">Father's</span>
<span class="ocrx_word" id="word_1_744" title="bbox 1736 2987 1826 3009; x_wconf 90">Name</span>
<span class="ocrx_word" id="word_1_745" title="bbox 1819 2983 1834 3019; x_wconf 71">:</span>
<span class="ocrx_word" id="word_1_746" title="bbox 1846 2987 2058 3009; x_wconf 92">Sharashchandra</span>
</span>
            <span class="ocr_line" id="line_1_189"
                  title="bbox 116 3021 1712 3043; baseline 0.001 -2; x_size 27.612183; x_descenders 5.6121817; x_ascenders 6">
<span class="ocrx_word" id="word_1_747" title="bbox 116 3021 193 3041; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_748" title="bbox 204 3021 313 3041; x_wconf 92">Number</span>
<span class="ocrx_word" id="word_1_749" title="bbox 307 3015 319 3051; x_wconf 72">:</span>
<span class="ocrx_word" id="word_1_750" title="bbox 333 3021 378 3041; x_wconf 96">820</span>
<span class="ocrx_word" id="word_1_751" title="bbox 869 3021 959 3043; x_wconf 96">Kadam</span>
<span class="ocrx_word" id="word_1_752" title="bbox 1622 3021 1712 3043; x_wconf 96">Kadam</span>
</span>
            <span class="ocr_line" id="line_1_190"
                  title="bbox 114 3047 2302 3081; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 12">
<span class="ocrx_word" id="word_1_753" title="bbox 114 3053 177 3081; x_wconf 76">Age:</span>
<span class="ocrx_word" id="word_1_754" title="bbox 196 3053 226 3075; x_wconf 96">63</span>
<span class="ocrx_word" id="word_1_755" title="bbox 246 3053 353 3075; x_wconf 85">Gender:</span>
<span class="ocrx_word" id="word_1_756" title="bbox 373 3053 446 3075; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_757" title="bbox 693 3047 765 3069; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_758" title="bbox 777 3047 795 3069; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_759" title="bbox 869 3055 947 3075; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_760" title="bbox 957 3055 1066 3075; x_wconf 68">Number:</span>
<span class="ocrx_word" id="word_1_761" title="bbox 1087 3055 1131 3075; x_wconf 96">820</span>
<span class="ocrx_word" id="word_1_762" title="bbox 1446 3047 1518 3069; x_wconf 95">Photo</span>
<span class="ocrx_word" id="word_1_763" title="bbox 1530 3047 1549 3069; x_wconf 96">is</span>
<span class="ocrx_word" id="word_1_764" title="bbox 1622 3055 1700 3075; x_wconf 96">House</span>
<span class="ocrx_word" id="word_1_765" title="bbox 1710 3055 1820 3075; x_wconf 72">Number:</span>
<span class="ocrx_word" id="word_1_766" title="bbox 1840 3055 1884 3075; x_wconf 96">820</span>
<span class="ocrx_word" id="word_1_767" title="bbox 2200 3047 2272 3069; x_wconf 96">Photo</span>
<span class="ocrx_word" id="word_1_768" title="bbox 2283 3047 2302 3069; x_wconf 96">is</span>
</span>
            <span class="ocr_line" id="line_1_191"
                  title="bbox 691 3081 2311 3115; baseline 0 -6; x_size 34; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_769" title="bbox 691 3081 805 3103; x_wconf 85">Available</span>
<span class="ocrx_word" id="word_1_770" title="bbox 830 3077 862 3119; x_wconf 47">|]</span>
<span class="ocrx_word" id="word_1_771" title="bbox 867 3087 931 3115; x_wconf 47">Age:</span>
<span class="ocrx_word" id="word_1_772" title="bbox 951 3087 979 3109; x_wconf 95">57</span>
<span class="ocrx_word" id="word_1_773" title="bbox 999 3087 1106 3109; x_wconf 95">Gender:</span>
<span class="ocrx_word" id="word_1_774" title="bbox 1127 3087 1237 3109; x_wconf 96">FEMALE</span>
<span class="ocrx_word" id="word_1_775" title="bbox 1444 3081 1558 3103; x_wconf 78">Available</span>
<span class="ocrx_word" id="word_1_776" title="bbox 1583 3077 1612 3119; x_wconf 50">||</span>
<span class="ocrx_word" id="word_1_777" title="bbox 1620 3087 1684 3115; x_wconf 50">Age:</span>
<span class="ocrx_word" id="word_1_778" title="bbox 1704 3087 1734 3109; x_wconf 95">30</span>
<span class="ocrx_word" id="word_1_779" title="bbox 1752 3087 1859 3109; x_wconf 95">Gender:</span>
<span class="ocrx_word" id="word_1_780" title="bbox 1880 3087 1952 3109; x_wconf 96">MALE</span>
<span class="ocrx_word" id="word_1_781" title="bbox 2197 3081 2311 3103; x_wconf 96">Available</span>
</span>
            <span class="ocr_line" id="line_1_192"
                  title="bbox 54 3434 2272 3464; baseline 0 -6; x_size 30; x_descenders 6; x_ascenders 6">
<span class="ocrx_word" id="word_1_782" title="bbox 54 3434 110 3464; x_wconf 94">Age</span>
<span class="ocrx_word" id="word_1_783" title="bbox 123 3440 154 3458; x_wconf 94">as</span>
<span class="ocrx_word" id="word_1_784" title="bbox 167 3440 200 3458; x_wconf 94">on</span>
<span class="ocrx_word" id="word_1_785" title="bbox 213 3434 374 3458; x_wconf 94">01.01.2022</span>
<span class="ocrx_word" id="word_1_786" title="bbox 689 3434 707 3458; x_wconf 91">#</span>
<span class="ocrx_word" id="word_1_787" title="bbox 718 3448 729 3450; x_wconf 91">-</span>
<span class="ocrx_word" id="word_1_788" title="bbox 741 3434 861 3458; x_wconf 95">Modified</span>
<span class="ocrx_word" id="word_1_789" title="bbox 875 3440 905 3458; x_wconf 95">as</span>
<span class="ocrx_word" id="word_1_790" title="bbox 919 3440 965 3464; x_wconf 95">per</span>
<span class="ocrx_word" id="word_1_791" title="bbox 977 3434 1139 3464; x_wconf 95">supplement</span>
<span class="ocrx_word" id="word_1_792" title="bbox 1151 3434 1215 3458; x_wconf 96">Date</span>
<span class="ocrx_word" id="word_1_793" title="bbox 1228 3434 1256 3458; x_wconf 93">of</span>
<span class="ocrx_word" id="word_1_794" title="bbox 1267 3434 1613 3458; x_wconf 91">Publication:-05-01-2022</span>
<span class="ocrx_word" id="word_1_795" title="bbox 1891 3434 1958 3458; x_wconf 96">Total</span>
<span class="ocrx_word" id="word_1_796" title="bbox 1972 3434 2060 3464; x_wconf 96">Pages</span>
<span class="ocrx_word" id="word_1_797" title="bbox 2083 3434 2116 3458; x_wconf 93">35</span>
<span class="ocrx_word" id="word_1_798" title="bbox 2138 3448 2149 3450; x_wconf 91">-</span>
<span class="ocrx_word" id="word_1_799" title="bbox 2162 3434 2234 3464; x_wconf 96">Page</span>
<span class="ocrx_word" id="word_1_800" title="bbox 2257 3434 2272 3458; x_wconf 96">3</span>
</span>
        </p>
    </div>
    <div class="ocr_carea" id="block_1_133" title="bbox 2359 210 2361 3193">
        <p class="ocr_par" id="par_1_133" lang="eng" title="bbox 2359 210 2361 3193">
<span class="ocr_line" id="line_1_193"
      title="bbox 2359 210 2361 3193; baseline 0 0; x_size 1491.5; x_descenders -745.75; x_ascenders 745.75">
<span class="ocrx_word" id="word_1_801" title="bbox 2359 210 2361 3193; x_wconf 95"> </span>
</span>
        </p>
    </div>
</div>
</body>
</html>"""

from lxml import html

titles = ["Name", "Husband's", "Father's", "House", "Age", "Name:", "Age:"]


def page_1_to_csv(bs_content):
    pass


def xpath_result(tree, xp) -> list:
    r_list = []
    for r in tree.xpath(xp):
        r_list.append(r)
    return r_list


def html_to_csv(f_html):
    tree = html.fromstring(f_html)
    pages_3_to_second_last(tree)


def pages_3_to_second_last(tree):
    divs = xpath_result(tree, '/html/body/div/*')
    v_flag = False
    page_dict = {}
    for _div in divs:
        spans = _div.xpath('./p/span')
        for span in spans:
            # print(f'table.text :: {etree.tostring(span)}')
            spans1 = span.xpath('./span')
            _line = []
            for span1 in spans1:
                _txt = span1.text.strip()
                if _txt and _txt != 'Available' and _txt != '||' and _txt != '|]':
                    if v_flag and _txt in titles:
                        _line.append(f" | {_txt} ")
                    else:
                        _line.append(f"{_txt} ")
            # format line
            if _line:
                formatted_line = "".join(_line)
                if not v_flag:
                    # header
                    header = page_dict.get('header', '')
                    page_dict['header'] = f"{header} {formatted_line}"
                    if 'Part number' in formatted_line or 'Part' in formatted_line:
                        v_flag = True
                    continue
                elif v_flag and '|' not in formatted_line and 'Part ' not in formatted_line:
                    _line = [f"{txt} | " if len(txt.strip()) == 10 else txt for txt in _line]
                elif "Father's" in formatted_line or "Husband's" in formatted_line:
                    _line = [txt.replace(" | Name", "Name") if "Name" in txt else txt for txt in _line]

                formatted_line = "".join(_line)
                if 'Total Pages' in formatted_line or 'Total' in formatted_line or 'Pages' in formatted_line:
                    # last page
                    formatted_line = formatted_line.replace('Photo is', '').replace(" | Age", "Age")
                    page_dict['footer'] = formatted_line
                    continue
                else:
                    # voter details
                    _voter = [v.strip() for v in formatted_line.split('|') if v.strip()]
                    if len(_voter) == 3:
                        v1, v2, v3 = tuple(_voter)
                    elif len(_voter) == 2:
                        v1, v2 = tuple(_voter)
                    else:
                        v1 = "".join(_voter)
                    print(v1, v2, v3)
                # print(formatted_line)

    print(page_dict)


def format_html(html_str):
    """
    format html page source, BeautifulSoup makes sure formatted output source is valid for parsing
    :param html_str: html page source string
    :return: formatted html
    """
    soup = bs4.BeautifulSoup(html_str, 'html5lib')
    return soup.prettify()


if __name__ == '__main__':
    # _html_dict = read_images_from_dir("C:\\EA\\OCR\\2022\\TEST\\AC20\\S05A20P3\\3")
    # html_to_csv(format_html(html_text))
    html_to_csv(html_text)
