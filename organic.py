from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
bootstrap = Bootstrap(app)


from views import *



if __name__ == "__main__":
    app.run(debug=True)

