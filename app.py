from flask import Flask, send_file, request
from bg import RemoveBackground


app = Flask(__name__)


@app.route('/remove_background', methods=['POST'])
def remove_background():
    """
    Endpoint to remove image background

    Request fields:
        link: str
        alpha_matting: true/false
        am_ft: int
        am_bt: int
        am_es: int

    :return:
        Image with removed background
    """

    data = request.json
    link = data['image_link']
    alpha_matting = data['alpha_matting']

    if alpha_matting == 'true':
        am_ft = data['alpha_matting_foreground_threshold']
        am_bt = data['alpha_matting_background_threshold']
        am_es = data['alpha_matting_erode_size']
    else:
        am_ft = 240
        am_bt = 10
        am_es = 10

    process = RemoveBackground(link)

    try:
        input_image_path = process.download_image()
        output_image_path = process.remove_bg(input_image_path,
                                              alpha_matting, am_ft, am_bt, am_es)
    except Exception as e:
        return f"Cannot process the image: \n{e}", 501

    return send_file(output_image_path)


if __name__ == "__main__":
    app.run()
