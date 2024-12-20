import os
from file_selector import select_photos, choose_save_directory
from image_processor import upscale_image
from user_interface import get_upscaling_factor
from config import DEFAULT_SAVE_DIRECTORY

def main():
    print("* * * Welcome to the Photo Upscaling Program! * * *")
    input("* * * Press Enter to continue * * *")

    print("Photo Upscaling Program")
    photos = select_photos()
    if not photos:
        print("No photos selected. Exiting program.")
        return

    factor = get_upscaling_factor()
    save_directory = choose_save_directory()

    if not save_directory:
        print("No save directory selected. Exiting program without saving upscaled images.")
        return

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for photo in photos:
        try:
            upscaled_image = upscale_image(photo, factor)
            filename = os.path.basename(photo)
            save_path = os.path.join(save_directory, f"upscaled_{factor}x_{filename}")
            upscaled_image.save(save_path)
            print(f"Saved upscaled image: {save_path}")
        except Exception as e:
            print(f"Failed to process {photo}: {e}")

if __name__ == "__main__":
    main()