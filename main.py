from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', username=["username"])


@app.route("/user/<int: id>")
def user(id):
    username = request.args.get("username")
    return f"{username}. {id}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)