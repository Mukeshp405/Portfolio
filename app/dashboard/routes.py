from flask import render_template, request, redirect, url_for, flash
from . import dashboard
from app.models import Project


@dashboard.route('/')
def index():
    return render_template("pages/home.html")
