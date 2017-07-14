import os
#import call
from bottle import route, run, request, response, parse_auth
import json
@route ('/api/',['GET','POST''PUT','DELETE'])
def hello():
        return "API is RUN"

@route('/api/<name>',method='GET')
def api_get(name = "?"):
                # user = request.get_header('X-user')
        if __auth__()==False:
                return "Deny access"
        else:
                user = request.get_header('X-user')
                return {"success":True,"name":user}

@route('/api/<name>',method='POST')
def api_post(name = "?"):
        return "Metodo Origen POST " + name

def __auth__():
        user = request.get_header('X-user')
