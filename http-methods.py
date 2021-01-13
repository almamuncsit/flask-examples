from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/form')
def form():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('http/form.html', result=dict)


@app.route('/success/<name>')
def success(name):
    return 'Welcome to %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return render_template('http/post-info.html', name=user)
    else:
        user = request.args['name']
        return 'Please login %s' % user


if __name__ == '__main__':
    app.run(debug=True)
