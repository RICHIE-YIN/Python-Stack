from flask_app import app, render_template, redirect, session, request
from flask_app.models.painting import Painting

@app.route('/paintings')
def paintings():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('paintings.html', paintings = Painting.get_all())

@app.route('/paintings/new')
def new_paintings():
    return render_template('new_painting.html')

@app.route('/paintings/create', methods = ['POST'])
def create_painting():
    if not Painting.validate_painting(request.form): #if name, description, and instructions are 3 characters+, redirect
        return redirect ('/paintings/new')
    Painting.save(request.form)
    return redirect('/paintings')

@app.route('/paintings/<int:id>')
def show_painting(id): #pass down id
    data = {'id' : id} #makes sure id in link matches id in data
    return render_template('show_painting.html', painting = Painting.get_one(data)) #pass in painting into html

@app.route('/paintings/edit/<int:id>')
def edit_painting(id): #pass down id
    data = {'id' : id} #makes sure id in link matches id in data
    return render_template('edit_painting.html', painting = Painting.get_one(data)) #pass in painting into html

@app.route('/paintings/update', methods = ['POST'])
def update_painting():
    if not Painting.validate_painting(request.form): #if name, description, and instructions are 3 characters+, redirect
        return redirect (f"/paintings/edit/{request.form['id']}")
    Painting.update(request.form) #else updates
    return redirect ('/paintings')

@app.route('/painting/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Painting.delete(data)
    return redirect('/paintings')