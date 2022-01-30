from PIL import Image


def get_cropped_image(dimensions, _image):
    left, top, right, bottom = tuple(dimensions)
    original = Image.open(_image)
    width, height = original.size  # Get dimensions
    size = (left, top, width - right, height - bottom)
    cropped_img = original.crop(size)
    # cropped_img.show()
    return cropped_img
