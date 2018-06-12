import json
from falcon import API, Request, Response, HTTP_200
from .test_data import GIPHY_SUCCESS_BODY


queryUrl = 'https://api.giphy.com/v1/gifs/search'
queryTemplate = queryUrl + '?api_key=deokzgUjxm6QHQdp3H3aca1LSZcCpucc&q={}&limit=25&offset=0&rating=Y&lang=en'


class SearchController(object):
    def on_get(self, request: Request, response: Response):
        response.status = HTTP_200
        fixed_height_small_still = json.loads(
            GIPHY_SUCCESS_BODY
        )['data'][0]['images']['fixed_height_small_still']
        response.body = json.dumps(
            [
                {

                    "url": fixed_height_small_still["url"].replace("_s", ""),
                    "width": int(fixed_height_small_still["width"]),
                    "height": int(fixed_height_small_still["height"])
                }
            ]
        )


def create_server():
    app = API()
    app.add_route('/search', SearchController())
    return app
