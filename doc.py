from flask import Flask,url_for,abort,request,render_template,redirect
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "Login"
    else:
        return "Show The Login Form"

@app.route('/user/<username>')
def show_user_profile(username):
   return 'User %s' % escape(username)

@app.route('/hello/')
@app.route('/post/<name>')
def show_post(name=None):
   return render_template('hello.htm',name=name)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
   return 'The Project Page'

@app.route('/about')
def about():
   return 'The About Page'

if __name__ == '__main__':
    app.run(debug=True)

