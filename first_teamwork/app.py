#  app.py
#  coding=gbk

from users import users_bp
from add import add_bp
from flask import Flask, jsonify
from utils import HttpError

app = Flask(__name__)


app.register_blueprint(users_bp)
app.register_blueprint(add_bp)


@app.errorhandler(HttpError)
def error_handle(error):
    response = jsonify(error.show())
    response.status_code = error.status_code
    response.message = error.message
    return response


if __name__ == '__main__':
    app.run()
