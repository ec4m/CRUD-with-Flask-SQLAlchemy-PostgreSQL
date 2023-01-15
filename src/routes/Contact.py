from flask import Blueprint, render_template

contact = Blueprint('contact_blueprint',__name__)

@contact.route('/')
def home():
  return render_template('index.html')


@contact.route('/new')
def add_contact():
  return "<h2>Añadiendo contacto</h2>"