from connexion import App
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = Path(__file__).parent.resolve()
connex_app = App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'tree.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)