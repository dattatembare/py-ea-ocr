import shutil
from argparse import ArgumentParser
from pathlib import Path

from src.pdf2images import pdf2png
from src.write2csv import write2csv


def read_files(directory, out_directory):
    for file in Path(directory).glob('**/*.pdf'):
        filename = Path(file).stem
        current_directory = Path(file).parent
        images_dir = f"{current_directory}/{filename}"
        # print(f"{file, filename, current_directory, images_dir}")
        print(file)
        path = Path(images_dir)
        path.mkdir(parents=True, exist_ok=True)
        # pdf2jpg
        pdf2png(file, images_dir)
        file_dir = Path(current_directory).stem
        csv_dir = f"{out_directory}/{file_dir}"
        path = Path(csv_dir)
        path.mkdir(parents=True, exist_ok=True)
        write2csv(images_dir, f"{csv_dir}/{filename}.csv")
        # Delete images directory
        shutil.rmtree(images_dir)


def get_args_dict() -> dict:
    parser = ArgumentParser()
    parser.add_argument('-i', '--in', help='PDF files main input directory')
    parser.add_argument('-o', '--out', help='CSV files main output directory')

    return parser.parse_args().__dict__


def execute():
    args_dict = get_args_dict()
    read_files(args_dict['in'], args_dict['out'])


if __name__ == '__main__':
    print("***** START *****")
    # read_files(r"C:\EA\OCR\2022\TEST")
    execute()
    print("***** End *****")
