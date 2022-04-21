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

    process = RemoveBackground(link)

    try:
        input_image_path = process.download_image()
        output_image_path = process.remove_bg(input_image_path)
    except Exception as e:
        return f"Cannot process the image: \n{e}", 501

    return send_file(output_image_path)


app.run()
