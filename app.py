# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file, request
import json
from pprint import pprint
# from pymongo import MongoClient

@route('/')
def index():
    return template("conexion.tpl")


@route('/login',method='POST')
def login():

    usuario = request.forms.get('UserInput')
    password = request.forms.get('PasswordInput')
    database = request.forms.get('DatabaseInput')
    host = request.forms.get('HostInput')
    # try:
    #     MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

    return 'Hello %s!'%usuario
    #return template('<b>Hello {{name}}</b>!', name=usuario)
    #return template("menu.tpl")

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='views/')


@route('/table')
def table():

## cambiar apertura de fichero json con el obtenido de la base de datos

    with open('carreras2017.json') as data_file:
        data = json.load(data_file)


    motogp2017=[]

    keylist = data.keys()
    titulo = keylist[0]

    claves = data[data.keys()[0]][0].keys() #claves del primer objeto de la primera clave


    for i,elem in enumerate(data[titulo]):
        diccionario=dict.fromkeys(claves)
        diccionario[claves[0]] = elem["nombre"]
        diccionario[claves[1]] = elem["nombreCircuito"]
        diccionario[claves[2]] = elem["pais"]
        motogp2017.insert(i,diccionario)

    return template("table.tpl",datos=motogp2017,titulo=titulo)


run(host='localhost', port=8080, debug=True)

#source /home/sergio/virtualenv/pymongo/bin/activate
