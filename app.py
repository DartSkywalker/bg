from flask import Flask, send_file, request
from bg import RemoveBackground


app = Flask(__name__)


@app.route('/remove_background', methods=['POST'])
def remove_background():
    """
    Endpoint to remove image background

    :return:
        Image with removed background
    """

    data = request.json
    link = data['image_link']
    alpha_matting = data['alpha_matting']

    process = RemoveBackground(link)

    try:
        input_image_path = process.download_image()
        output_image_path = process.remove_bg(input_image_path, alpha_matting)
    except Exception as e:
        return f"Cannot process the image: \n{e}", 501

    return send_file(output_image_path)


if __name__ == "__main__":
    app.run()
