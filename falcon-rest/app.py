import falcon
import images


api = application = falcon.API()




images = images.Resource()
api.add_route('/images', images)