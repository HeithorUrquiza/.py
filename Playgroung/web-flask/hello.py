from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        result = func()
        return "<b>" + result + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        result = func()
        return "<em>" + result + "</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        result = func()
        return "<u>" + result + "</u>"
    return wrapper
        


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello World!!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you're the {number}"

if __name__ == "__main__":
    app.run(debug=True)