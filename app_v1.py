# -*- coding: utf-8 -*-
import os

# Retrieve Flask, our framework
# request module gives access to incoming request data
from flask import Flask, request

app = Flask(__name__)

# Home Page
@app.route('/')
def cabinet():
    return """<h1>Welcome to 'Something Borrowed...'</h1><br/><br/>
    <h2>A place to find and share materials at ITP.</h2><br/>
    <a href='/create'>Create your account</a> or <a href='/login'>Login</a><br>
    <a href='/about'>About us</a>"""

# Create your account page
@app.route('/create', methods=["GET","POST"])
def create():
    # Did the client make a POST request?
	if request.method == "POST":

		# get the form data submitted and store it in a variable
		# the second value is an option for if the user doesn't input any value
		name = request.form.get('name', 'Tim Berners-Lee')
		#email = request.form.get('email', 'tim_berners_lee@gmail.com')
		#user_name = request.form.get('user_name', 'T.B. Lee')

		# return custom HTML using the user submitted data
		return """
		<html><body style=''><h1>Hello %s!</h1><br>
		<h2>Welcome to 'Something Borrowed...'!</br>
		We are excited to have you here!</h2></br></br>
		<a href='/'> -- Back Home -- </a></body><html>""" % (name)

	else:

		# client made a GET request for '/create'
		# return a simple HTML form that POSTs to itself
		return """<html><body>
		<form action="/create" method="POST">
			What's your name? <input type="text" name="name" id="name"/>
			<input type="submit" value="That's it!"/>
		</form>
		</body></html>"""

# Login into your account page
@app.route('/login')
def login():
    return 'Hello World'

# About page
@app.route('/about')
def about():
    return """
    <h2>'Something borrowed…' is a database of useful things that you would lend to other ITPers.</h2></br> 
    <p>It’s an easy way to access ITPers inventory for researches and materials, to find books and movies, or to get prototypes done.</p></br></br></br>
	<ul>
		<li>- Faster Prototypes</li>
		<li>- Economy: less money spent!</li>
		<li>- Community sense: let's help each other!</li> 
		<li>- Networking: interact and meet new people</li>
	</ul>
    """


# start the webserver
if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)