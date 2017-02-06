# resource.py
import falcon


class Resource(object):
    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200

api = falcon.API()
resource = Resource()
api.add_route('/resource', resource)