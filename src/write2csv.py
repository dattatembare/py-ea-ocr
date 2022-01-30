import csv
from pathlib import Path

from lxml import html

from src.image2text import read_image


def xpath_result(tree, xp) -> list:
    r_list = []
    for r in tree.xpath(xp):
        r_list.append(r)
    return r_list


def read_page(image):
    tree = html.fromstring(read_image(image))
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
            if _line:
                _line_str = ','.join(_line)
                # print(_line_str)
                _lines.append(_line_str)

    return '\n'.join(_lines)


def read_file(directory_path: str) -> dict:
    print(f"2. Read text from images in dir={directory_path} \npage_number=", end="")
    pages_dict: dict = {int(Path(p).stem): p for p in Path(directory_path).glob('**/*.png')}
    pages = sorted(pages_dict.keys())
    for page_number in range(1, len(pages) + 1):
        image = pages_dict[page_number]
        print(page_number, end=',')
        pages_dict[page_number] = read_page(image)

    return pages_dict


def write2csv(directory_path: str, csv_name: str):
    pages_dict: dict = read_file(directory_path)
    # print(file_pages)
    # print(json.dumps(file_pages))
    print(f"\n3. Write csv file={csv_name}")
    with open(csv_name, 'w+') as f:
        pages = sorted(pages_dict.keys())
        for k in range(1, len(pages) + 1):
            writer = csv.DictWriter(f, fieldnames=[k])
            writer.writerow({k: pages_dict[k]})

    # Remove " from file text
    f = open(csv_name, 'r')
    s = f.read().replace("\"", "")
    f = open(csv_name, 'w')
    f.write(s)
    f.close()


if __name__ == '__main__':
    write2csv(r'C:\EA\OCR\2022\TEST\AC20\S05A20P3')
