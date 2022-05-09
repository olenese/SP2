from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Blueprint, redirect, render_template, url_for, request, flash
from .models import Logins, Users
from .security import encrypt, decrypt
from . import db

manager = Blueprint('manager', __name__)




@manager.route('/newlogin', methods=['POST'])
@login_required
def newlogin_post():
    location = request.form.get('location')
    username = request.form.get('username')
    password = request.form.get('password')
    url = request.form.get('url')
    note = request.form.get('note')
    new_login = Logins(location=location, username=username, password=encrypt(password), url=url, note=note, userID=current_user.id)
    db.session.add(new_login)
    db.session.commit()
    return redirect(url_for('main.profile'))

