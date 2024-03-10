from flask import Flask, render_template, redirect, url_for
from flask import Flask, render_template, request, jsonify
from backend.model import Adder

app = Flask(__name__)
adder = Adder()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_page', methods=['GET', 'POST'])
def test_page():
    return render_template('test_page.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = adder.add_numbers(num1, num2)
        return render_template('result.html', result=result)
    else:
        return redirect(url_for('test_page.html'))  # 如果是 GET 请求，重定向到主页


@app.route('/about_us')
def another_page():
    return render_template('about_us.html')


@app.route('/github')
def github_page():
    return render_template('github.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
