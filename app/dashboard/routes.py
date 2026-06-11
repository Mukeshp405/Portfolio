from flask import render_template, request, redirect, url_for, flash
from . import dashboard
from app.models import Project


@dashboard.route('/')
def index():
    return render_template("pages/home.html")

@dashboard.route("/about")
def about():
    return render_template("pages/about.html")

@dashboard.route('/projects')
def projects():
    return render_template("pages/projects.html")