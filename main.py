from flask import Flask
from flask import render_template
from flask import request

app = Flask("Formular")


@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/form', methods=["GET","POST"])
def fomular():
    if request.method == "POST":
        return "Formular empfangen"
    return render_template("formular.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
