from flask import Blueprint, render_template, request, redirect
from models.ContactModel import ContactModel
from database.db import db

contact = Blueprint('contact_blueprint',__name__)


@contact.route('/')
def home():
  contacts = ContactModel.query.all()
  return render_template('index.html', contacts=contacts)


@contact.route('/new', methods=['POST'])
def add_contact():
  fullname = request.form['fullname']
  email = request.form['email']
  phone = request.form['phone']

  contact = ContactModel(fullname, email, phone)

  db.session.add(contact)
  db.session.commit()

  return redirect('/contact/')


@contact.route('/update', methods=['PUT'])
def update_contact():
  return "Update contact"


@contact.route('/delete', methods=['DELETE'])
def delete_contact():
  return "Delete contact"
