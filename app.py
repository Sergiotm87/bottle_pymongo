from bottle import redirect, route, run
# from pymongo import MongoClient
# import urllib.parse

@route('/')
def index():
    return template("conexion.tpl")

# username = urllib.parse.quote_plus('user')
# password = urllib.parse.quote_plus('pass/word')
# MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))



run(host='localhost', port=8080, debug=True)

#source /home/sergio/virtualenv/pymongo/bin/activate
