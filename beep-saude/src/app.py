from flask import Flask
from flask_cors import CORS
from resources import chart_api


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(chart_api, url_prefix='/api')
CORS(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
