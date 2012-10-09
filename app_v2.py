import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template, url_for
from mongoengine import *

# import data models
import models

import re
from unidecode import unidecode

connect('mydatabase', host=os.environ.get('MONGOLAB_URI'))

app = Flask(__name__)   # create our flask app


# Create the lists that match the name of the ListField in the models.py
book_type = ['Paperback','Hardcover','PDF','Kindle']
genre = ['Fiction', 'Programming', 'Physical Computing', 'ITP', 'Design', 'Art']
itpStatus = ['Current Student', 'ITP Alumni', 'Faculty', 'Resident', 'ITP Adjunct']


# ITP'S CABINET
books = { }

books['Understanding Comics'] = {
	'title' : 'Understanding Comics',
	'author' : 'Scott McCloud',
	'image' : 'understanding_comics.gif',
	'type' : 'Paperback',
	'genre' : 'Art',
	'description' : """Praised throughout the cartoon industry by such luminaries as Art Spiegelman, 
					Matt Groening, and Will Eisner, this innovative comic book provides a detailed look at the history, 
					meaning, and art of comics and cartooning.""",
	'inStock' : True,
	'owner' : 'Bruna Calheiros',
	'email' : 'bms415@nyu.edu',
	'itpStatus' : 'Current Student'
}

books['Learning Processing'] = { 
	'title' : 'Learning Processing',
	'author' : 'Daniel Shiffman',
	'image' : 'learning_processing.gif',
	'type' : 'Paperback',
	'genre' : 'Programming',
	'description' : """This book teaches you the basic building blocks of programming needed to create cutting-edge graphics applications including 
					interactive art, live video processing, and data visualization.""",
	'inStock' : True,
	'owner' : 'Bruna Calheiros',
	'email' : 'bms415@nyu.edu',
	'itpStatus' : 'Current Student'
	}

books['Getting Started with Arduino'] = { 
	'title' : 'Getting Started with Arduino',
	'author' : 'Massimo Banzi',
	'image' : 'getting_started_with_arduino.gif',
	'type' : 'Paperback',
	'genre' : 'Programming',
	'description' : """Arduino is the open-source electronics prototyping platform that\'s taken the design and hobbyist world by storm. 
					This thorough introduction, updated for Arduino 1.0, gives you lots of ideas for projects and helps you work with them right away.""",
	'inStock' : True,
	'owner' : 'Bruna Calheiros',
	'email' : 'bms415@nyu.edu',
	'itpStatus' : 'Current Student'
	}

books['The Laws of Simplicity'] = { 
	'title' : 'The Laws of Simplicity',
	'author' : 'John Maeda',
	'image' : 'the_laws_of_simplicity.gif',
	'type' : 'Hardcover',
	'genre' : 'Design',
	'description' : """Maeda's concise guide to simplicity in the digital age shows us how this idea can be a cornerstone of 
					organizations and their products - how it can drive both business and technology. We can learn to simplify without sacrificing 
					comfort and meaning.""",
	'inStock' : True,
	'owner' : 'Bruna Calheiros',
	'email' : 'bms415@nyu.edu',
	'itpStatus' : 'Current Student'
	}


# this is our main page
@app.route("/")
def index():
	# render the template, pass in the animals dictionary refer to it as 'animals'
	return render_template("main.html", books=books)


# this is the submit new items form
@app.route("/submit")
def submit_form():
	# render the template, pass in the animals dictionary refer to it as 'animals'
	return render_template("main.html", books=books)



# pages inside a category
@app.route("/books/<title>")
def show_title(title):
	# render the template, pass in the animals dictionary refer to it as 'animals'
	return 'Title %s' % title




# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	