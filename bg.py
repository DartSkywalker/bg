from rembg.bg import remove
import os
import requests
import glob


class RemoveBackground:
    """
    Class to handle all functionality for background removal
    :param:
        input_image_link: str - link to to image
    """

    def __init__(self, input_image_link):
        self.input_image_link = input_image_link

    def download_image(self):
        """
        Download image from the self.input_image_link

        :return:
            Path to the downloaded image
        """

        img_data = requests.get(self.input_image_link).content

        img_rel_name = f"input/{self.input_image_link.split('/')[-1]}"

        with open(img_rel_name, 'wb') as handler:
            handler.write(img_data)

        return img_rel_name

    @staticmethod
    def remove_bg(image_path, alpha_matting, am_ft, am_bt, am_es):
        """
        Remove background from the provided image

        :param: image_path: str - path to the image
        :return:
            Path to the image with removed background
        """

        with open(image_path, 'rb') as i:
            processed_image_name = f"processed/nobg_{image_path.split('/')[-1]}.png"

            with open(processed_image_name, 'wb') as o:
                input_im = i.read()
                if alpha_matting == 'true':
                    output = remove(input_im, alpha_matting=True,
                                    alpha_matting_foreground_threshold=am_ft,
                                    alpha_matting_background_threshold=am_bt,
                                    alpha_matting_erode_size=am_es)
                else:
                    output = remove(input_im)
                o.write(output)

        return processed_image_name

    @staticmethod
    def cleanup():
        """
        Remove all files from the 'input' and 'processed' folders
        """

        input_files = glob.glob('input')
        processed_files = glob.glob('processed')

        for f in input_files:
            os.remove(f)

        for f in processed_files:
            os.remove(f)


