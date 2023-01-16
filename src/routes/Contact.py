from flask import Blueprint, render_template, request, redirect, url_for
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

  return redirect('/contact')


@contact.route('/update')
def update_contact():
  return "Update contact"


@contact.route('/delete/<id>')
def delete_contact(id):
  contact = ContactModel.query.get(id)

  db.session.delete(contact)
  db.session.commit()

  return redirect(url_for('contact_blueprint.home'))
