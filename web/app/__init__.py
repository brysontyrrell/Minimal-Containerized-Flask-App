import flask
import config


app = flask.Flask(__name__)
app.config.from_object(config)


@app.route("/")
def hello():
    return "Hello World!"
