from flask import Flask, render_template, request
from pmt.match import matching, load_data, update_cluster


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data', methods=['GET'])
def data():
    if request.method == 'GET':
        try:
            left_data, right_data = load_data()
            return render_template('data.html', left_data=left_data, right_data=right_data)
        except:
            return render_template('page-500.html')

@app.route('/match', methods=['GET'])
def match():
    if request.method == 'GET':
        try:
            matcher = matching()
            update_cluster(matcher)
            return render_template('match.html', matcher=matcher)
        except:
            return render_template('page-500.html')
    else:
        return render_template('page-404.html', matcher=None)


if __name__ == '__main__':
   app.run(debug=True)
