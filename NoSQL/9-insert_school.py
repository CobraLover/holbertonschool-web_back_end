#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Method that will inserts a new doc in a collection """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
