# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime


class Book(Document):
    title = StringField(required=True, max_length=120, verbose_name="Title")
    slug = StringField()
    author = StringField(required=True, max_length=120, verbose_name="Author")
    image = StringField(max_length=50)

    # Book type and genre are lists of Strings
    bookType = ListField(StringField(max_length=30))
    genre = ListField(StringField(max_length=30))

    description = StringField(max_length=500)
    owner = StringField(required=True, max_length=120, verbose_name="Owner")

    # Email is another different field
    email = EmailField(required=True, max_length=50, verbose_name="Email")

    # itpStatus is a list of Strings
    itpStatus = ListField(StringField(max_length=30))

BookForm = model_form(Book)