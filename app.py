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

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        try:
            left_table = request.form.get('left_table')
            right_table = request.form.get('right_table')
            left_data, right_data = load_data(left_table, right_table)
            print(left_table)
            return render_template('data.html', left_data=left_data, right_data=right_data)
        except:
            return render_template('page-500.html')
    elif request.method == 'GET':
        return render_template('data.html', left_data=None, right_data=None)
    else:
        return render_template('page-404.html', right_data=None)

@app.route('/match', methods=['GET','POST'])
def match():
    if request.method == 'POST':
        try:
            left_table = request.form.get('left_table')
            right_table = request.form.get('right_table')
            threshold = request.form.get('threshold', type=float)
            matcher = matching(left_table, right_table, threshold)
            return render_template('match.html', matcher=matcher)
        except:
            return render_template('page-500.html')
    elif request.method == 'GET':
        return render_template('match.html', matcher=None)
    else:
        return render_template('page-404.html', matcher=None)


if __name__ == '__main__':
   app.run(debug=True)