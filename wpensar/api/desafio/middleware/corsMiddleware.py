class corsMiddleware(object):

    def process_response(self, req, resp):
        resp['Access-Control-Allow-Origin'] = '*'
        resp['Access-Control-Allow-Credentials'] = 'true'
        resp['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
        resp['Access-Control-Allow-Headers'] = 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,X-Reference-Levels'

        return resp