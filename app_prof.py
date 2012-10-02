import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template

app = Flask(__name__)   # create our flask app


# SPIRIT ANIMAL CATALOG
animals = {}
animals['Bear']= {
	'image':'bear.gif',
	'spirit':'Hungry or Sleepy',
	'inStock' : True
}

animals['Butterfly'] = {'image':'butterfly.gif', 'spirit':'Flighty', 'inStock' : True}
animals['Camel'] = {'image':'camel.gif', 'spirit':'Funny', 'inStock' : True}
animals['Dinosaur'] = {'image':'dinosaur.gif','spirit':'Loner', 'inStock' : True}
animals['Dolphin'] = {'image':'dolphin.gif','spirit':'Likes water', 'inStock' : True}
animals['Elephant'] = {'image':'elephant.gif','spirit':'Feels too big for body', 'inStock' : True}
animals['Frog'] = {'image':'frog.gif','spirit':'Appears slimy', 'inStock' : False}


# this is our main page
@app.route("/")
def index():
	# render the template, pass in the animals dictionary refer to it as 'animals'
	return render_template("main.html", animals=animals)



# this is the 2nd route - can be access with /page2
@app.route("/rent", methods=["POST"])
def rent():

	# Get the user submitted data
	rentalData = {
		'name' : request.form.get('name'),
		'life_goal' : request.form.get('lifegoal'),
		'rental_time' : request.form.get('rentaltime'),
		'animal_name' : request.form.get('animal')
	}

	# get animal by animal_name
	rentalData['animal'] = animals[rentalData.get('animal_name')]


	# is selected animal in stock?
	if rentalData['animal'].get('inStock') == False:
		return render_template("out_of_stock.html", **rentalData)



	# determine return date, if 'eternity' not selected
	if rentalData['rental_time'] != 'eternity':
		now = datetime.datetime.now()

		if rentalData['rental_time'] == "hour":
			future = datetime.timedelta(hours=1)

		elif rentalData['rental_time'] == "day":
			future = datetime.timedelta(days=1)

		elif rentalData['rental_time'] == "year":
			future = datetime.timedelta(days=365.25)

		rentalData['return_time'] = now + future

	else:
		rentalData['return_time'] = None



	return render_template('rental_confirm.html', **rentalData)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	