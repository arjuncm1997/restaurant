import os 
from flask import Flask, flash, session
from flask import render_template, flash, redirect, request, abort, url_for
from restaurant import app,db
from restaurant.models import AddCategory, AddFood, AddContact




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def gallery():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        contacts  = AddContact(firstname=firstname,lastname=lastname,email=email,subject=subject,message=message)
        try:
            db.session.add(contacts)
            db.session.commit()
            return redirect('/contact')
        except:
            return 'There was an issue adding your task'
    else:
        return render_template('contact.html')

@app.route('/contactview')
def contactview():
    tasks = AddContact.query.all()
    return render_template('contactview.html',tasks=tasks)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/aadmin')
def aadmin():
    return render_template('aadmin.html')

@app.route('/add_category',methods=['GET','POST'])
def add_category():
    if request.method == 'POST':
        category = request.form['category']
        categories  = AddCategory(category=category)
        try:
            db.session.add(categories)
            db.session.commit()
            return redirect('/add_categoryview')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('add_category.html')

@app.route('/add_categoryview')
def add_categoryview():
    tasks = AddCategory.query.all()
    return render_template('add_categoryview.html',tasks=tasks)

@app.route('/add_categorydelete/<int:id>')
def add_categorydelete(id):
    task_to_delete = AddCategory.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/add_categoryview')
    except:
        return 'There was a problem deleting that task'


@app.route('/add_categoryupdate/<int:id>', methods=['GET', 'POST'])
def add_categoryupdate(id):
    task = AddCategory.query.get_or_404(id)

    if request.method == 'POST':
        task.category = request.form['category']
        try:
            db.session.commit()
            return redirect('/add_categoryview')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('add_categoryupdate.html', task=task)

@app.route('/add_food',methods=['GET','POST'])
def add_food():
    if request.method == 'POST':
        itemtype = request.form['itemtype']
        timeinterval = request.form['timeinterval']
        category = request.form['category']
        foodname = request.form['foodname']
        amount = request.form['amount']
        fooditem  = AddFood(itemtype=itemtype,timeinterval=timeinterval,category=category,foodname=foodname,amount=amount)
        try:
            db.session.add(fooditem)
            db.session.commit()
            return redirect('/add_foodview')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('add_food.html')

@app.route('/add_foodview')
def add_foodview():
    tasks = AddFood.query.all()
    return render_template('add_foodview.html',tasks=tasks)

@app.route('/add_fooddelete/<int:id>')
def add_fooddelete(id):
    task_to_delete = AddFood.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/add_foodview')
    except:
        return 'There was a problem deleting that task'


@app.route('/add_foodupdate/<int:id>', methods=['GET', 'POST'])
def add_foodupdate(id):
    task = AddFood.query.get_or_404(id)

    if request.method == 'POST':
        task.itemtype = request.form['itemtype']
        task.timeinterval = request.form['timeinterval']
        task.category = request.form['category']
        task.foodname = request.form['foodname']
        task.amount = request.form['amount']

        try:
            db.session.commit()
            return redirect('/add_foodview')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('add_foodupdate.html', task=task)




@app.route('/uindex')
def uindex():
    return render_template("uindex.html")

@app.route('/umenu')
def umenu():
    return render_template("umenu.html")



@app.route('/admin')
def admin():
    return render_template("admin.html")