from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html', pagination=pagination)
