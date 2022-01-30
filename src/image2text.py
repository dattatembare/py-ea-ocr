from pathlib import Path

import bs4
import pytesseract.pytesseract
from bs4 import BeautifulSoup as bs, BeautifulSoup
from pytesseract import image_to_pdf_or_hocr

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_string(cropped_img):
    text = pytesseract.image_to_string(cropped_img)
    return text.replace(',', ';')


def get_html(cropped_img) -> BeautifulSoup:
    hocr = pytesseract.image_to_pdf_or_hocr(cropped_img, extension='hocr')
    _list = hocr.decode('utf-8').split('\n')[3:]
    _bytes = "\n".join(_list)
    f_html = bs(_bytes, "lxml").encode('utf-8')
    return f_html


def read_images_from_dir(directory) -> object:
    return {Path(file).stem: read_image(file) for file in Path(directory).glob('**/*.png')}


def format_html(html_str):
    """
    format html page source, BeautifulSoup makes sure formatted output source is valid for parsing
    :param html_str: html page source string
    :return: formatted html
    """
    soup = bs4.BeautifulSoup(html_str, 'html5lib')
    return soup.prettify()


def read_image(file_path) -> BeautifulSoup:
    # print(file_path)
    hocr = image_to_pdf_or_hocr(str(file_path), extension='hocr')
    _list = hocr.decode('utf-8').split('\n')[3:]
    _bytes = "\n".join(_list)
    _html = bs(_bytes, "lxml").encode('utf-8')
    # print(_html)
    return _html


if __name__ == '__main__':
    # read_images_from_dir("C:\\EA\\OCR\\2022\\TEST\\AC20\\S05A20P3\\3")
    # read_images_from_dir("C:\\EA\\OCR\\2022\\TEST\\AC20\\S05A20P3")
    read_image(r"C:\EA\OCR\2022\TEST\AC20\S05A20P3\1.png")
    # read_image(r"C:\EA\OCR\2022\TEST\AC20\S05A20P3\3.png")
