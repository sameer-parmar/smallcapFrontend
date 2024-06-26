# app/app.py
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__,static_folder='static')

# Path to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        # Simulate processing and store a dummy confirmation
        confirmation_id = "12345"  # This would be dynamically generated in a real app
        return jsonify({"confirmation_id": confirmation_id}), 201

@app.route('/confirmation/<confirmation_id>', methods=['GET'])
def get_confirmation(confirmation_id):
    # In a real app, fetch confirmation status from a database
    if confirmation_id == "12345":
        return render_template('confirmation.html')
    else:
        return render_template('refusal.html')

if __name__ == '__main__':
    app.run(debug=True)
