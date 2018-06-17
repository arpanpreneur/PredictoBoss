from bottle import route, run, response, request
import Config.DataSource
from Config import Cors
import json
from bottle import route, request

@route('/login')
def login():
    return '''
        <form action="/login" method="get">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        '''
    

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return "username = "+username+" password = "+password

@route('/post',method='POST')
def post():
    title = request.forms.get('title');
    post_body = request.forms.get('post_body')
    rv = {"title":title, "post_body":post_body}
    return rv

run(server='paste', host='0.0.0.0', port=9000, debug=True, reloader=True)