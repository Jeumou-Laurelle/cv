from flask import Flask, render_template, request, jsonify, send_file
import json
import os

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', **data)

@app.route('/download-cv')
def download_cv():
    path = "CV__jeumou_ngongang_Laurelle_maiva.pdf"
    return send_file(path, as_attachment=True)

@app.route('/api/data')
def get_data():
    return jsonify(load_data())

@app.route('/api/contact', methods=['POST'])
def contact():
    # In a real app, you would send an email here
    return "", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
