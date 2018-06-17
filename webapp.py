from bottle import route, run, response, request
import Config.DataSource as ds
from Config import Cors
import json
from bottle import static_file
from bottle import route, request


@Cors.enable_cors
@route('/test')
def test():
    return "Working...."


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./StaticsWebPages')

@Cors.enable_cors
@route('/search', method=['GET','OPTIONS'])
def search():
    city = request.query['city']
    date = request.query['date']

    data_source = ds.DataSource()
    db = data_source.getDB()

    city_data = db['city_wise_price']

    query = {"city":city, "date":date}
    res=city_data.find_one(query,{"_id":0})

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    return res

@Cors.enable_cors
@route('/cities', method=['GET','OPTIONS'])
def search():

    data_source = ds.DataSource()
    db = data_source.getDB()

    city_data = db['city_wise_price']

    res=city_data.distinct("city")

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


    return {"cities":res}

run(server='paste', host='0.0.0.0', port=9000, debug=True, reloader=True)
