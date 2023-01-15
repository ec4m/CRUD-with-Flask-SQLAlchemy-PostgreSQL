from flask import Flask

# Routes
from routes import Contact

app = Flask(__name__)


if __name__ == '__main__':
  app.register_blueprint(Contact.contact, url_prefix="/contact")
  app.run(debug=True, port=3000)