#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, url_for

from settings import MENUS, SERVER
from utils import read_csv_data, read_txt_data

app = Flask(__name__)
app.debug = SERVER['debug']

@app.route('/')
def home():
    return render_template('home.html', menus=MENUS)

@app.route('/contact')
def contact():
    return render_template('contact.html', menus=MENUS)

@app.route('/courses')
def courses():
    return render_template('courses.html', menus=MENUS,
           courses_under=read_csv_data('courses_under.csv'),
           courses_grad=read_csv_data('courses_grad.csv'))

@app.route('/datamining')
def datamining():
    return render_template('datamining.html',\
    		menus=MENUS, 
    		contents=read_csv_data('datamining.csv'))

@app.route('/admission')
def admission():
    return render_template('admission.html',\
           menus=MENUS,
           admission=read_csv_data('admission.csv'))

@app.route('/members')
def members():
    return render_template('members.html',\
           menus=MENUS,
           members=read_csv_data('members.csv'),
           alumni_ms=read_csv_data('alumni_ms.csv'),
           alumni_phd=read_csv_data('alumni_ms.csv'))

@app.route('/projects')
def projects():
    return redirect(url_for('faq'))

@app.route('/projects/faq')
def faq():
    return render_template('faq.html',\
           menus=MENUS,
           faq=read_csv_data('faq.csv'))

@app.route('/research')
def research():
    return redirect(url_for('publications'))

@app.route('/research/publications')
def publications():
    return render_template('publications.html',\
           menus=MENUS,
           pub_dom_conferences=read_txt_data('pub_dom_conferences.txt'),
           pub_dom_journals=read_txt_data('pub_dom_journals.txt'),
           pub_int_conferences=read_txt_data('pub_int_conferences.txt'),
           pub_int_journals=read_txt_data('pub_int_journals.txt'))

@app.route('/software')
def software():
    return render_template('software.html',\
           menus=MENUS,
           software=read_csv_data('software.csv'))

if __name__=='__main__':
    app.run(SERVER['host'], SERVER['port'])
