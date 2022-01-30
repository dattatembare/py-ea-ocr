# Project
This project could be used as a base project or template to start new project. It has 3 basic features, project config implementation,
Logging & decorators and Unit test launcher to run all unit tests in one shot.    
 
## Logging and decorators:
The logger implementation is based on standard logging module, with basic logging there are 3 decorators provided.

## Logging Features: 
* When `{time}` placeholder provided in logfile name then every run will generate the new log file with timestamp.
When `{time}` is not provided then logger functionality will work as usual.
* Custom log levels - Example provided to create the custom log levels. In this project `trace` and `perf` (performance)
log levels created.
* Handled double logging issue.

## Decorators: 
* trace - When trace decorator used on function, logs will be printed at start and end of the method call.
* timer - When timer decorator used on function, logs will be printed at start and end of the method call, with that method 
performance timings will be printed.
* exception - When exception decorator used on function, and when method will throw an exception, error message will be 
printed in error log file. Only read functionality implemented in this project, for write functionality check the documentation.

## Tesseract OCR manual commands
```
C:\Program Files\Tesseract-OCR> tesseract C:\EA\OCR\2021\003.png C:\EA\OCR\2021\003-1 -l hin+eng pdf
C:\Program Files\Tesseract-OCR> tesseract C:\EA\OCR\2021\003.png C:\EA\OCR\2021\003-1 -l hin+eng hocr
C:\Program Files\Tesseract-OCR> tesseract C:\EA\OCR\2021\003.png C:\EA\OCR\2021\003-1 -l hin+eng tsv
```

## Setup steps
**1. Installations:** 

These installations are mandatory:  **Windows** 
1. Install [VC++ 2015](https://www.microsoft.com/en-au/download/details.aspx?id=53840) - It is require to run Tesseract (Not sure if it required for V5.0.0 alpa, it was required for version 4.1)
2. Install [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/) - Read text from Images - I used [tesseract-ocr-w64-setup-v4.0.0.20181030.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe) **Choose Additional language data; select all Indian languages** (Expand the option, deselect all and select the languages you want) 
Install path (Note down an installed path, it is required to add in code)
C:\Program Files\Tesseract-OCR
3. Install [GhostScript](https://ghostscript.com/download/gsdnld.html) - PDF to images converter - I used gs923w64.exe
4. Install [ImageMagick](https://imagemagick.org/script/download.php#windows) - Image processing - I used ImageMagick-7.0.7-28-Q16-x64-dll.exe **Choose legacy utilities for ImageMagic** (Check box on install screen)
5. Install [Python 3](https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe) - Make sue check checkbox to add to path. Ex. Add Python 3.9 to PATH 
6. Install Git to pull the data from Bitbucket repository
   1. After pulling the repository, 
      1. Open commandline with project path 
      2. Verify python version `C:\py-ea-ocr> python --version`
      3. Create virtual env `C:\py-ea-ocr>python -m venv myPyEnv` 
         1. and activate venv `C:\py-ea-ocr\myPyEnv\Scripts>activate` 
         2. After running above command cmd should look like `(myPyEnv) <project path>\test-py\py-ea-ocr\myPyEnv\Scripts>`
      4. env run `C:\py-ea-ocr> pip install -r requirements.txt`
      5. Verify if all necessary modules are installed - 
      ```
      C:\py-ea-ocr>pip list
       Package         Version
       --------------- -------
       ghostscript     0.7
       html-testRunner 1.2
       Jinja2          2.9.5
       MarkupSafe      2.0.1
       Pillow          9.0.0
       pip             20.2.3
       pytesseract     0.3.8
       setuptools      49.2.1
       testfixtures    6.9.0
         ```

## Run command
Command: `C:\py-ea-ocr> python -m runner -i C:\EA\OCR\2022\TEST -o C:\EA\OCR\2022\TESTOUT`

 