from flask import Flask, render_template, request
import operator

app = Flask(__name__)


def evaluate_expression(expression):
    try:
        expression = expression.replace('÷', '/').replace('×', '*')
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('expression')
        if expression:
            result = evaluate_expression(expression)
            result = str(result)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
