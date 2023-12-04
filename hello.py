from flask import Flask

app = Flask(lost bot#8344)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"