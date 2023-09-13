from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.post import Post

from datetime import datetime
realdate = '%d-%m-%Y'

@app.route('/post_message', methods = ['POST'])
def post_message():
    if not Post.validate_posts(request.form):
        return redirect('/dashboard')
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    Post.save(data)
    return redirect('/dashboard') 


@app.route ('/delete_post/<int:id>')
def delete_post(id):
    data = {
        'id': id
    }
    Post.delete_post(data)
    return redirect('/dashboard')
