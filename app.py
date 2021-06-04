from flask import Flask, render_template, request
from pmt.match import matching, load_data


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/themes')
def themes():
    return render_template('themes.html')

@app.route('/data')
def data():
    left_data, right_data = load_data()
    return render_template('data.html', left_data=left_data, right_data=right_data)

@app.route('/match', methods=['GET','POST'])
def match():
    if request.method == 'POST':
        try:
            max_df = request.form.get('max_df', type=float)
            min_df = request.form.get('min_df', type=float)
            min_ngram = request.form.get('min_ngram', type=int)
            max_ngram = request.form.get('max_ngram', type=int)
            threshold = request.form.get('threshold', type=float)
            matcher = matching(max_df, min_df, min_ngram, max_ngram, threshold)
            return render_template('match.html', matcher=matcher)
        except:
            return render_template('page-500.html')
    elif request.method == 'GET':
        return render_template('match.html', matcher=None)
    else:
        return render_template('page-404.html', matcher=None)


if __name__ == '__main__':
   app.run(debug=True)