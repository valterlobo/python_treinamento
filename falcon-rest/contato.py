# contatoResource.py

# Let's get this party started!
import falcon
import json
from Contato import Contato
from collections import namedtuple
# Middleware
import middlewares


class ContatoResource(object):

    @staticmethod
    def _json_object_hook(d): 
        return namedtuple('X', d.keys())(*d.values())

    @staticmethod
    def json2obj(data):
        return json.loads(data, object_hook=_json_object_hook)

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        contatoValter = Contato(nome="Valter", email="ana@mail.com")
        resp.body = contatoValter.toJSON()

    def on_post(self, req, resp):
        data = req.context['data']
        print(data)
        contato = json.loads(data, object_hook=lambda d: namedtuple('contato', d.keys())(*d.values()))
        #ContatoResource.json2obj(data)
        print(contato.nome)

# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[
    middlewares.JSONTranslator()
])

# Resources are represented by long-lived class instances
contato_resource = ContatoResource()

# things will handle all requests to the '/things' URL path
app.add_route('/contato', contato_resource)
