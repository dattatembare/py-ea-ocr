import csv
import datetime
import json
from pathlib import Path

from lxml import html

from src.image2text import get_string, read_image
from src.image_processor import get_cropped_image
from src.util.file_util import get_config


def xpath_result(tree, xp) -> list:
    r_list = []
    for r in tree.xpath(xp):
        r_list.append(r)
    return r_list


def read_page_1(image):
    image_name = Path(image).stem
    tree = html.fromstring(read_image(image))
    # spans = xpath_result(tree, '//span/*')
    divs = xpath_result(tree, '/html/body/div/*')
    _lines = []
    for _div in divs:
        spans = _div.xpath('./p/span')
        for span in spans:
            # print(f'table.text :: {etree.tostring(span)}')
            spans1 = span.xpath('./span')
            _line = []
            for span1 in spans1:
                _txt = span1.text.strip()
                if _txt:
                    _line.append(_txt)
            _line_str = ' , '.join(_line)
            # print(_line_str)
            _lines.append(_line_str)
    return {image_name, '\n'.join(_lines)}


def read_page_3_to_second_last(configs, image):
    page = {}
    for k, v in configs.items():
        if k == 'voters':
            _voters = []
            for voter in v:
                _voter = get_string(get_cropped_image(voter, r"C:\EA\OCR\2022\TEST\AC20\S05A20P3\9.png"))
                _voter = _voter.replace('Photo', '').replace('is', '').replace('Available', '')
                _voter_details = [d.strip() for d in _voter.split('\n') if d.strip()]
                if _voter_details:
                    while 'gender' in _voter.lower() and 'gender' not in _voter_details[-1].strip().lower():
                        del _voter_details[-1]
                    _voters.append({_voter_details[0]: ' | '.join(_voter_details[1:])})
            page[k] = _voters
        else:
            page[k] = get_string(get_cropped_image(v, image)).replace('\n', '')
    # print(json.dumps(page))
    return page


def read_file(config_file, directory_path) -> dict:
    configs = get_config(config_file)
    pages_dict: dict = {int(Path(p).stem): p for p in Path(directory_path).glob('**/*.png')}
    pages = sorted(pages_dict.keys())
    first_and_last_page = [pages[0], pages[-1]]
    for page_number, image in pages_dict.items():
        print(image, str(datetime.datetime.now()))
        if page_number in first_and_last_page:
            pages_dict[page_number] = read_page_1(image)
        elif page_number != pages[0]:
            pages_dict[page_number] = read_page_3_to_second_last(configs, image)
    return pages_dict


def write2csv(page_dict: dict, csv_name):
    csv_file = open(csv_name, 'w')
    for k, v in page_dict.items():
        if k == 'voters':
            writer = csv.DictWriter(csv_file, fieldnames=['voter_id', 'voter_details'])
            writer.writeheader()
            for voter in v:
                voter_id, voter_details = [(k, voter[k]) for k in voter][0]
                writer.writerow({'voter_id': voter_id, 'voter_details': voter_details})
        else:
            writer = csv.DictWriter(csv_file, fieldnames=[k])
            writer.writerow({k: v})
    csv_file.close()


if __name__ == '__main__':
    file_pages = read_file('configs/goa-jan-2022.json', r'C:\EA\OCR\2022\TEST\AC20\S05A20P3')
    print(json.dumps(file_pages))
    # page = read_file('configs/goa-jan-2022.json', r'C:\EA\OCR\2022\TEST\AC20\S05A20P3\3.png')
    # write2csv(page)
