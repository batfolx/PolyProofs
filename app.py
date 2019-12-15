from flask import Flask, render_template, request
from utils import get_math_proofs

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.form)
    return render_template('home.html')


@app.route('/math_submit', methods=['POST'])
def math_handler():
    """
    This function handles the Math clicked input.
    :return: The math_html page template for the website.
    """
    button_clicked = ''
    for item in request.form.items():
        button_clicked = item
        break

    math_concept = button_clicked[0]
    return render_template('math_submit.html', topic=button_clicked[1], proofs=get_math_proofs(math_concept))


@app.route('/physics_submit', methods=['POST'])
def physics_handler():
    button_clicked = ''
    print(request.form)
    for item in request.form.items():
        button_clicked = item
        break

    return render_template('physics_submit.html')


if __name__ == '__main__':
    app.run(debug=True)
