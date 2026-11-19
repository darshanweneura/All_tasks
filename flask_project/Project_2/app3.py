from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)

app.secret_key="Secret_key"

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123456789':
            session['username'] = username

            return redirect('/dashboard')
        
        return "invalid username or password"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html',username = session['username'])
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)