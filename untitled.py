# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

trash_info = {
    "used water bottle": "non-biodegradable",
    "banana peel": "biodegradable",
    "plastic bag": "non-biodegradable",
    "paper": "biodegradable",
    "aluminum can": "non-biodegradable",
    "apple core": "biodegradable"
}

@app.route('/')
def home(): #default page
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    trash_type = request.form['trash_type'].lower()
    if trash_type in trash_info:
        result = trash_info[trash_type]
    else:
        result = "unknown"
    return render_template('result.html', trash_type=trash_type.capitalize(), result=result)

if __name__ == '__main__':
    app.run(debug=True)
