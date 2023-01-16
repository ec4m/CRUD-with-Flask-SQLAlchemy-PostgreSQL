from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Routes
from routes import Contact
# Database
from database.db import db

app = Flask(__name__)
app.secret_key = "secret key"
# Estoy configurando y se estoy pasando app a la clase SQLAlchemy.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://newpostgres:elian@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

db.init_app(app) # Con esta linea se soluciona el error "raise sa.exc.UnboundExecutionError(message) from None sqlalchemy.exc.UnboundExecutionError: 'SQLALCHEMY_DATABASE_URI' config is not set. Bind key 'None' is not in 'SQLALCHEMY_BINDS' config."
with app.app_context():
  db.create_all() # Esto creara las tablas que se definieron en el modelo de datos


if __name__ == '__main__':
  app.register_blueprint(Contact.contact, url_prefix="/contact")
  app.run(debug=True, port=3000)