#quote_resource.py
import falcon
import json

class QuoteResource:

	def on_get(self, req, resp):

		quote = {
	            'quote': 'I\'ve always been more interested in the future than in the past.',
	            'author': 'Grace Hopper'
				}
		resp.body = json.dumps(quote)


quote = QuoteResource()
api = falcon.API()
api.add_route('/quote', quote)