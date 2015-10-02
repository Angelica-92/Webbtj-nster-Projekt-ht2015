# coding utf-8
# Author: <your name>
from bottle import route, run, template, request, static_file
import json
import requests

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
def first_page():
    return template('index')
@route('/')
def start():
    return template('index')
@route('/P1/')
def p1():
    ''' 1: Hämta aktuell låt från API '''

@route('/chanel/<chanel>')
def chanel(chanel):
    r=requests.get('http://api.sr.se/api/v2/playlists/rightnow?channelid='+chanel+'&format=json')
    return r
       
@route('/P2/')
def p2():
    return template('P2')
@route('/P3/')
def p3():
    data3=get_data()
    return data3

def get_data3():
    a=requests.get('http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json')
    return a

@route('/P4/')
def p4():
     data=get_data()
     return data
    
def get_data():
    r=requests.get('http://api.sr.se/api/v2/playlists/rightnow?channelid=p4&format=json')
    return r



@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080)

