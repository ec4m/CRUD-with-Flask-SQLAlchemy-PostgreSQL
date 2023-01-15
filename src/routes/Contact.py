from flask import Blueprint, render_template

contact = Blueprint('contact_blueprint',__name__)


@contact.route('/')
def home():
  return render_template('index.html')


@contact.route('/new', methods=['POST'])
def add_contact():
  return "<h2>Añadiendo contacto</h2>"


@contact.route('/update', methods=['PUT'])
def update_contact():
  return "Update contact"


@contact.route('/delete', methods=['DELETE'])
def delete_contact():
  return "Delete contact"
