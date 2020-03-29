from flask import Flask,jsonify,request,make_response
from flask_restful import Api,Resource
import pandas as pd
import numpy as np

from pymongo import MongoClient     #To handle mongo db

#Read a tsv file
df = pd.read_csv('Food Survey_141Responses.csv',sep=',')

#Manupilating The dataset
drop_col = ["Timestamp","Food sanctum that doesn't vibes with you"]
df.drop(drop_col,axis=1,inplace=True)
df1 = df.drop(["Preferred choice"],axis = 1).iloc[88:,:]
df1.columns = ["What's your name?", 'Year?', 'Select one?','Prefer, North Indian or South Indian?', 'Vegetarian?',
    'What would you rather prefer?',
    'Preferred place for Breakfast? (except mess :p)',
    'Preferred place for Lunch ?(except mess :P)',
    'Preferred place for Dinner ?(except mess :P)', 'Select One:',
    'Preferred Chinese Place', 'Preferred Italian Place',
    'Preferred North Indian Place', 'Preferred South Indian Place',
    'Preferred Continental Place', 'Tea/Coffee', 'Maggie',
    'Juices/Milkshakes/Lime', 'Rolls', 'Samosa/Puff', 'Pani Puri/Chat',
    'Shawarma', 'Sugar Rush', 'Spicy 🌶️', 'Sweet 🍬',
    'Name the food Sanctum', 'Preferred choice']

df = df.iloc[:88,:]
df.drop(["Preferred choice.1"],axis = 1,inplace = True)
df.columns = ["What's your name?", 'Year?', 'Select one?',
    'Prefer, North Indian or South Indian?', 'Vegetarian?',
    'What would you rather prefer?',
    'Preferred place for Breakfast? (except mess :p)',
    'Preferred place for Lunch ?(except mess :P)',
    'Preferred place for Dinner ?(except mess :P)', 'Select One:',
    'Preferred Chinese Place', 'Preferred Italian Place',
    'Preferred North Indian Place', 'Preferred South Indian Place',
    'Preferred Continental Place', 'Tea/Coffee', 'Maggie',
    'Juices/Milkshakes/Lime', 'Rolls', 'Samosa/Puff', 'Pani Puri/Chat',
    'Shawarma', 'Sugar Rush', 'Preferred choice', 'Spicy 🌶️', 'Sweet 🍬',
    'Name the food Sanctum']


udf = pd.concat([df,df1],ignore_index=True)

cols = ["Name","Year","Hosteller","North-South","Vegetarian","Dine-in","Breakfast","Lunch","Dinner","Cusinies","Chinese","Italain",
    "North","South","Continental","Tea/Coffee","Maggie","Juices","Rolls","Samosa/Puff","Panipuri","Shawarma","Sugar rush",
    "Spicy-Sweet","Spicy","Sweet","All-time"]
udf.columns = cols


#Create a Flask app(api)
app = Flask(__name__)
api = Api(app)

'''
client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users' : 0
})

class Visit(Resource):
    def get(self):
        num = UserNum.find({})[0]['num_of_users']
        num += 1
        UserNum.update({}, {"$set":{"num_of_users":num}})
        return str("Hello user " + str(num))
'''

@app.route('/')
def hello_world():
    return("Hello World!")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


class All_time(Resource):
    def get(self):
        all_time_restro = dict(udf['All-time'].value_counts().sort_values(ascending = False).head(5))
        a = list(all_time_restro.keys())
        result = {
            "All-time" : a
        }
        return make_response(jsonify(result),200)

class Chinese(Resource):
    def get(self):
        chinese_restro = dict(udf['Chinese'].value_counts().sort_values(ascending = False).head(5))
        a = list(chinese_restro.keys())
        result = {
            "Chinese" :a
        }
        return make_response(jsonify(result),200)

class Italain(Resource):
    def get(self):
        italain_restro = dict(udf['Italain'].value_counts().sort_values(ascending = False).head(5))
        a = list(italain_restro.keys())
        result = {
            "Italain" :a
        }
        return make_response(jsonify(result),200)


class North(Resource):
    def get(self):
        north_restro = dict(udf['North'].value_counts().sort_values(ascending = False).head(5))
        a = list(north_restro.keys())
        result = {
            "North" : a
        }
        return make_response(jsonify(result),200)

class South(Resource):
    def get(self):
        south_restro = dict(udf['South'].value_counts().sort_values(ascending = False).head(5))
        a = list(south_restro.keys())
        result = {
            "South" : a
        }
        return make_response(jsonify(result),200)

class Continental(Resource):
    def get(self):
        continental_restro = dict(udf['Continental'].value_counts().sort_values(ascending = False).head(5))
        a = list(continental_restro.keys())
        result = {
            "Continental" :a
        }
        return make_response(jsonify(result),200)



api.add_resource(All_time,"/all-time")
api.add_resource(Chinese,"/chinese")
api.add_resource(Italain,"/italain")
api.add_resource(North,"/north")
api.add_resource(South,"/south")
api.add_resource(Continental,"/continental")
#api.add_resource(Visit,"/hello")

#for example
#Run localhost:5000/all-time to get a json result
#added local host to 0.0.0.0
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
