from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from user import UserRegister

from security import authenticate, identity
from item import Item, ItemList

app = Flask(__name__)
app.secret_key='lorax' #This should never be shared publicly and is for illustration purposes only.
api = Api(app)

jwt  = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)