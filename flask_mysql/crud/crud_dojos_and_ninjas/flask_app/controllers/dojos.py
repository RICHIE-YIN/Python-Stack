from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    return render_template("users.html",dojos=Dojo.get_all())

@app.route('/ninjas')
def ninjas():
    return render_template("new.html", dojos=Dojo.get_all(), ninjas=Ninja.get_all())

@app.route('/dojos/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("showdojo.html",dojo=Dojo.get_one_with_ninjas(data))

@app.route('/dojo/new')
def new():
    return render_template("newdojo.html")

@app.route('/dojo/create',methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninja/create',methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save_ninja(request.form)
    return redirect('/dojos')


@app.route('/dojo/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("editdojo.html",dojo=Dojo.get_one(data))



@app.route('/dojo/update',methods=['POST'])
def update():
    Dojo.update(request.form)
    return redirect('/dojos')

@app.route('/dojo/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Dojo.destroy(data)
    return redirect('/dojos')
