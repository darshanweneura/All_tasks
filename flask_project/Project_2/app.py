from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/user/<uname>/<int:id>')
def user(uname,id):
    return f"User is {uname} and Id is {id}"

@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    return f"Hello, {name}"

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f"Welcome {username}"

@app.route('/form')
def form():
    return render_template('form2.html')

@app.route('/product')
def product():
    name = request.args.get('name')
    price = request.args.get('price')
    return f"product: {name} price:{price}"

if __name__ == '__main__':
    app.run(debug=True)
