from pathlib import Path

from src.pdf2images import pdf2png


def read_files(directory_name):
    for file in Path(directory_name).glob('**/*.pdf'):
        filename = Path(file).stem
        current_directory = Path(file).parent
        images_dir = f"{current_directory}/{filename}"
        print(f"{file, filename, current_directory, images_dir}")
        path = Path(images_dir)
        path.mkdir(parents=True, exist_ok=True)
        # pdf2jpg
        pdf2png(file, images_dir)


if __name__ == '__main__':
    print("Start")
    read_files(r"C:\EA\OCR\2022\TEST")
