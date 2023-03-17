from flask import Flask, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with the actual path to your tesseract.exe file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image from the request
        image = request.files['image']
        img = Image.open(image)

        # Perform OCR on the image
        text = pytesseract.image_to_string(img)

        # Return the extracted text
        return render_template('result.html', text=text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

