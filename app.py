# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aashirya" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Rakesh" # write your name
    age = "45" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Manisha" # write your name
    age = "41" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage
# add other routes, if you want
@app.route("/sibling")
def friend():

    name = "Anvi & Vinayak" # write your name
    age = "7" # write your age

    return render_template('sibling.html' , name = name , age = age)





# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
