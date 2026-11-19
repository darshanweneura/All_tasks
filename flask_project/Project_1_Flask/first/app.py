from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():

    name = 'Darshan'
    age = 20
    course = "Python Programming"

    return render_template('about.html',
                            name = name,
                            age = age,
                            course = course)

@app.route('/contact')
def contact():
    return render_template('contact.html',
                           peoples = [
                               {
                                   "name": "Darshan" , "passed": True
                               },
                               {
                                   "name": "Rahul" , "passed":True
                               },
                               {
                                   "name": "Krishna" , "passed":False
                               }
                                ])

@app.route('/result')
def result():
    return render_template('result.html',
                           name = 'Darshan',
                           marks = 60)

@app.route('/students')
def students():
    return render_template('students.html',
                           names = range(1,25,2))

@app.route('/image')
def image():
    return render_template('image.html')

if __name__=='__main__':
    app.run(debug=True)