from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Ensure uploads and static directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upscale', methods=['POST'])
def upscale_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the uploaded file
    upload_path = os.path.join('uploads', file.filename)
    file.save(upload_path)

    # Perform upscaling (replace this with your upscaling logic)
    upscaled_path = os.path.join('static', 'upscaled_' + file.filename)
    # Example: Assume upscaling is done and saved to upscaled_path

    # Return the URL of the upscaled image
    upscaled_url = f"/static/upscaled_{file.filename}"
    return jsonify({'image_url': upscaled_url})

if __name__ == '__main__':
    app.run(debug=True)
