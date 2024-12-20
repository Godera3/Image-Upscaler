from PIL import Image

def upscale_image(image_path, factor):
    """
    Upscale the image by a given factor.
    
    :param image_path: Path to the image file.
    :param factor: Upscaling factor (e.g., 2, 3, 4).
    :return: Upscaled PIL Image object.
    """
    image = Image.open(image_path)
    width, height = image.size
    new_width = width * factor
    new_height = height * factor
    upscaled_image = image.resize((new_width, new_height), Image.Resampling.BICUBIC)
    return upscaled_image
