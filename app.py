from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def new():
    result = ""
    return render_template('index.htm', result=result)

@app.route('/result', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        result = request.form['Name']
        blob = TextBlob(result)
        for sentence in blob.sentences:
            result = sentence.sentiment.polarity
        return render_template('index.htm', result=result)
    else:
        return render_template('index.htm')

if __name__ == '__main__':
    app.debug = True
    app.run()