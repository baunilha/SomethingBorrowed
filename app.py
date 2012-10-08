import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template, url_for

# import all of mongoengine
# from mongoengine import *
from flask.ext.mongoengine import mongoengine

# import data models
import models

import re
from unidecode import unidecode

connect('mydatabase', host=os.environ.get('MONGOLAB_URI'))

app = Flask(__name__)   # create our flask app


# Create the lists that match the name of the ListField in the models.py
bookType = ['Paperback','Hardcover','PDF','Kindle']
genre = ['Fiction', 'Programming', 'Physical Computing', 'ITP', 'Design', 'Art']
itpStatus = ['Current Student', 'ITP Alumni', 'Faculty', 'Resident', 'ITP Adjunct']


# --------- Routes ----------


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


@app.route("/submit", methods=['GET'])
def submit_form():

	app.logger.debug(request.form.getlist('bookType'))
	app.logger.debug(request.form.getlist('genre'))
	app.logger.debug(request.form.getlist('itpStatus'))

	# get new books items form from models.py
	book_form = models.BookForm(request.form)
	
	if request.method == "POST" and book_form.validate():
	
		# get form data - create new book
		book = models.Book()
		book.title = request.form.get('title','no title')
		book.slug = slugify(book.title)
		book.author = request.form.get('author','anonymous')
		book.description = request.form.get('description','')
		book.bookType = request.form.getlist('bookType')
		book.genre = request.form.getlist('genre')
		book.itpStatus = request.form.getlist('itpStatus')
		
		book.save()

		return redirect('/books/%s' % book.slug)


# pages inside a category
@app.route("/books/<book_slug>")
def book_display(book_slug):
	
	# get book by book_slug
	try:
		book = models.Book.objects.get(slug=book_slug)
	except:
		abort(404)

	# prepare template data
	templateData = {
		'book' : book
	}

	# render and return the template
	return render_template('book_entry.html', **templateData)



# slugify the title 
# via http://flask.pocoo.org/snippets/5/
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
def slugify(text, delim=u'-'):
	"""Generates an ASCII-only slug."""
	result = []
	for word in _punct_re.split(text.lower()):
		result.extend(unidecode(word).split())
	return unicode(delim.join(result))


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	