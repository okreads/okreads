from flask import Flask, jsonify, Blueprint, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello reads!"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.debug = True
    app.run(host='0.0.0.0')
