# contatoResource.py

# Let's get this party started!
import falcon



class ContatoResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
contato_resource = ContatoResource()

# things will handle all requests to the '/things' URL path
app.add_route('/contato', contato_resource)