from flask import Flask, request, render_template, session, make_response

app = Flask(__name__)

app.secret_key = "my_secret_key"

@app.route('/login')
def login():
    session['username'] = 'rahul'
    return "Login successfully"

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome {session ['username'] } "
    return "Please login first"

@app.route('/logout')
def logout():
    session.pop('username',None)
    return "Logged Out successfully"


@app.route('/setcookies')
def setcookies():
    response = make_response('Cookies created')
    response.set_cookie('username', 'Rahul')
    return response

@app.route('/getcookies')
def getcookies():
    username = request.cookies.get('username')

    return f"username: {username}"

@app.route('/deletecookies')
def deletecookies():
    response = make_response("Cookies Deleted")

    response.delete_cookie('username')
    return response

@app.route('/test')
def test():
    name = "Rahul"

    print("Debug value:", name)

    return "Check terminal"

if __name__ == '__main__':
    app.run(debug=True)