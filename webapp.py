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
@route('/search', method=['POST','OPTIONS'])
def search():
    city  = request.forms.get('city')
    date  = request.forms.get('date')
    state = request.forms.get('state')

    print(city)
    print(date)
    print(state)

    data_source = ds.DataSource()
    db = data_source.getDB()

    city_data = db['city_wise_price']

    if date == "":
        if city == "":
            query = {"state": state}
        else:
            query = {"city": city}
    elif city=="" and state=="":

        query={"date":date}
    else:

        if city == "":
            query = {"state": state, "date": date}
        else:
            query = {"city": city, "date": date}

    results=list(city_data.find(query,{"_id":0}).sort("date", -1))

    res={"results":results}

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    return res

@Cors.enable_cors
@route('/lists', method=['GET','OPTIONS'])
def populate_options():

    data_source = ds.DataSource()
    db = data_source.getDB()

    city_data = db['city_wise_price']

    cities=city_data.distinct("city")
    states=city_data.distinct("state")

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


    return {"cities":cities, "states":states}


@Cors.enable_cors
@route('/latest', method=['GET','OPTIONS'])
def latest():

    data_source = ds.DataSource()
    db = data_source.getDB()

    collection = db['checkLastUpdated']

    updated_on = collection.find_one({"_id":1001})['updated_on']

    city_data = db['city_wise_price']

    query = {"date": updated_on}

    results = list(city_data.find(query, {"_id": 0}))

    res = {"results": results}

    return res

run(server='paste', host='0.0.0.0', port=9000, debug=True, reloader=True)
