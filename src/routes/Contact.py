from flask import Blueprint, render_template, request, redirect, url_for, flash
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

  flash("Contact added successfully!")

  return redirect('/contact')


@contact.route('/update/<id>', methods=['GET','POST'])
def update_contact(id):
  contact = ContactModel.query.get(id)

  if request.method == 'POST':
    contact.fullname = request.form['fullname'] # Se asignan los nuevos valores
    contact.email = request.form['email']
    contact.phone = request.form['phone']
    
    db.session.commit()

    flash("Contact updated successfully!")

    return redirect(url_for('contact_blueprint.home'))
  else:
    return render_template('update.html', contact=contact)



@contact.route('/delete/<id>')
def delete_contact(id):
  contact = ContactModel.query.get(id)

  db.session.delete(contact)
  db.session.commit()

  flash("Contact deleted successfully!")

  return redirect(url_for('contact_blueprint.home'))


@contact.route('/about')
def about():
  return render_template('about.html')