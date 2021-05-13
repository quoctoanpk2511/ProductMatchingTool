from flask import Flask, render_template
from match import start_match


app = Flask(__name__)

@app.route('/')
def index():
    matcher = start_match()
    return render_template('index.html', matcher=matcher)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/themes')
def themes():
    return render_template('themes.html')

# @app.route('/match', methods=['POST'])
# def match():

if __name__ == '__main__':
   app.run(debug=True)