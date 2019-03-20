# как добавить циклы (routes.py):

from flask import render_template
from . import app, db
from app.models import Post


# добавлено 20 марта 2019, см.также внизу
from app.forms import PostForm
from flask import redirect

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Александр'}
    #posts = [
    #    {
    #        'author': {'username': 'Марк'},
    #        'body': 'O, hi, Mark!'
    #    },
    #    {
    #        'author': {'username': 'Боб'},
    #        'body': 'Совы не то, чем кажутся'
    #    },
    #    {
    #        'author': {'username': 'Билл'},
    #        'body': 'Помни! Реальность — иллюзия, вселенная — голограмма, скупай золото, пока! '
    #    }
    #]
    posts = Post.query.all()
    return render_template('index.html', title='Home', user=user, posts=posts)

# не забываем добавить импорт
# (20 марта 2019)
# from app.forms import PostForm   (см. выше)
@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
    #if form.validate_on_send():
        p = Post(title=form.title.data, text=form.text.data, )
        #p=Post(title=form.title.data, text=form.text.data,  sender=form.sender.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/index')
    return render_template('create.html', title='Create', form=form)


@app.route('/posts/{post_id}')
def post(post_id):
    post = Post.query.get(post_id)
    render_template('post.html', post=post)