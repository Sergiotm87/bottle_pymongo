# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file, request, redirect, response
import json
import pymongo

@route('/')
def index():

    return template("conexion.tpl")


@route('/login',method='POST')
def login():

    usuario = request.forms.get('UserInput')
    password = request.forms.get('PasswordInput')
    database = request.forms.get('DatabaseInput')
    host = request.forms.get('HostInput')

    uri = 'mongodb://%s:%s@%s/%s' % (usuario, password, host, database)
    client = pymongo.MongoClient(uri)
    try:
        client.admin.command('ismaster')
        response.set_cookie('uri',uri)
        redirect("/menu")
    except pymongo.errors.OperationFailure, e:
        error = "Error. No se puede conectar con mongoDB: %s" % e
        return template("error.tpl",mensaje=error)


@route('/menu')
def menu():

    return template("menu.tpl")

@route('/motogp/<name>',method='POST')
def carreras(name):

    motogp2017=[]
    motogp2017=database_query(name)

    if name == 'carreras':
        return template("carreras.tpl",datos=motogp2017,titulo="Carreras motogp 2017")
    elif name == 'pilotos':
        return template("pilotos.tpl",datos=motogp2017,titulo="Pilotos motogp 2017")
    else:
        error = "Error 404. Recurso no encontrado"
        return template("error.tpl",mensaje=error)


def database_query(query):

    uri = request.get_cookie('uri')

    client = pymongo.MongoClient(uri)
    db=client.motogp
    collection=db[query]
    cursor = collection.find({})
    motogp2017=[]
    for document in cursor:
        motogp2017.append(document)

    return motogp2017

@route('/<filename:path>')
@route('/motogp/<filename:path>')
def send_static(filename):
    return static_file(filename, root='views/')

run(host='localhost', port=8080, debug=True)
