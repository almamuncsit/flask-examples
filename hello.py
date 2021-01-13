from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'hello world'


@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s how are you?' % name


@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number %d' % post_id


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_name', name='Admin'))
    else:
        return redirect(url_for('show_blog', post_id=12))


if __name__ == '__main__':
    app.run(debug=True)
