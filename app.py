# app.py
from flask import Flask, render_template, request
from model import predict_review

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        review = request.form['review']
        prediction = predict_review(review)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)