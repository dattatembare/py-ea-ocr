import csv
import json

import pytesseract.pytesseract
from PIL import Image
from bs4 import BeautifulSoup as bs, BeautifulSoup
from lxml import html

from src.util.file_util import get_config

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
titles = ["Name", "Husband's", "Father's", "House", "Age", "Gender", "Name:", "Age:", "Gender:"]
detailed_titles = ["voter_id", "Name", "Husband's Name", "Father's Name", "House Number", "Age", "Gender"]


def xpath_result(tree, xp) -> list:
    r_list = []
    for r in tree.xpath(xp):
        r_list.append(r)
    return r_list


def get_voter_details(f_html):
    tree = html.fromstring(f_html)
    spans = xpath_result(tree, '//span/*')
    _line = []
    for span in spans:
        _txt = span.text.strip()
        if _txt and _txt != '||' and _txt != '|]':
            _txt = _txt.replace('Aqe', 'Age').replace('Ane', 'Age')
            if _txt in titles:
                _line.append(f"|{_txt} ")
            else:
                _line.append(f"{_txt} ")

    while _line[-1].strip() not in ['MALE', 'FEMALE']:
        del _line[-1]

    voter_details = "".join(_line)
    voter_details = voter_details.replace("|Husband's |", "|Husband's ") \
        .replace("|Father's |", "|Father's ") \
        .replace(',', ';').replace('Photo is', '')
    voter_details_list = voter_details.split('|')

    elements_dict = {}
    for ele in voter_details_list:
        ele = ele.replace('-', ':') if ':' not in ele else ele
        elements = [e.strip() for e in ele.split(':') if e.strip()]
        if len(elements) == 2 and elements[0] in detailed_titles:
            elements_dict[elements[0]] = elements[1]
        else:
            v = elements_dict.get('Voter_id', '')
            elements_dict['Voter_id'] = f"{v} {''.join(elements).strip()}"

    return elements_dict


def read_file(config_file):
    configs = get_config(config_file)
    page = {}
    for k, v in configs.items():
        if k == 'voters':
            _voters = []
            for voter in v:
                f_html = get_html(get_cropped_image(voter))
                _voters.append(get_voter_details(f_html))
            page[k] = _voters
        else:
            page[k] = get_string(get_cropped_image(v))

    print(json.dumps(page))
    return page


def get_string(cropped_img):
    text = pytesseract.image_to_string(cropped_img)
    return text.replace(',', ';').replace(':', '-')


def get_html(cropped_img) -> BeautifulSoup:
    hocr = pytesseract.image_to_pdf_or_hocr(cropped_img, extension='hocr')
    _list = hocr.decode('utf-8').split('\n')[3:]
    _bytes = "\n".join(_list)
    f_html = bs(_bytes, "lxml").encode('utf-8')
    return f_html


def get_cropped_image(dimensions, _image=None):
    left, top, right, bottom = tuple(dimensions)
    _image = r"C:\EA\OCR\2022\TEST\AC20\S05A20P3\3.png"
    original = Image.open(_image)
    width, height = original.size  # Get dimensions
    size = (left, top, width - right, height - bottom)
    cropped_img = original.crop(size)
    # cropped_img.show()
    return cropped_img


def write2csv(page_dict: dict):
    csv_file = open('voters.csv', 'w')
    for k, v in page_dict.items():
        if k == 'voters':
            writer = csv.DictWriter(csv_file, fieldnames=detailed_titles)
            writer.writeheader()
            writer.writerows({k: v})
        else:
            writer = csv.DictWriter(csv_file, fieldnames=[k])
            writer.writerow({k: v})
    csv_file.close()


if __name__ == '__main__':
    read_file('configs/goa-jan-2022.json')

    # L T R B
    # header - [25, 25, 0, 3300]
    # left - 110, 865, 1615 Box - 740x280
    # top - 215, 515, 815, 1115, 1410, 1710, 2010, 2305, 2605, 2905
    # bottom - 3100, 2800, 2500, 2200, 1900, 1600, 1300, 1000, 700, 400
    # footer - [25, 3300, 0, 0]

    # voters - L, T, R, B
    # 1.1  [110,215,1630,3100]  1.2 [865,215,885,3100]  1.3 [1615,215,125,3100]
    # 2.1  [110,515,1630,2800]  2.2 [865,515,885,2800]  2.3 [1615,515,125,2800]
    # 3.1  [110,815,1630,2500]  2.2 [865,815,885,2500]  2.3 [1615,815,125,2500]
    # 4.1  [110,1115,1630,2200] 2.2 [865,1115,885,2200] 2.3 [1615,1115,125,2200]
    # 5.1  [110,1410,1630,1900] 2.2 [865,1410,885,1900] 2.3 [1615,1410,125,1900]
    # 6.1  [110,1710,1630,1600] 2.2 [865,1710,885,1600] 2.3 [1615,1710,125,1600]
    # 7.1  [110,2010,1630,1300] 2.2 [865,2010,885,1300] 2.3 [1615,2010,125,1300]
    # 8.1  [110,2305,1630,1000] 2.2 [865,2305,885,1000] 2.3 [1615,2305,125,1000]
    # 9.1  [110,2605,1630,700]  2.2 [865,2605,885,700]  2.3 [1615,2605,125,700]
    # 10.1 [110,2905,1630,400]  2.2 [865,2905,885,400]  2.3 [1615,2905,125,400]
