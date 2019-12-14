from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/math_submit', methods=['POST'])
def math_handler():
    """
    This function handles the Math clicked input.
    :return: The math_html page template for the website.
    """
    print(request.form)
    return render_template('math_submit.html')


if __name__ == '__main__':
    app.run(debug=True)
