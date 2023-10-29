import requests

class Post():

    def PostData(data, url_end):
        form_response = requests.post(
            url = 'http://127.0.0.1:5000/' + url_end,
            data=data ,
            headers= {
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        return form_response

    def PostNoData(url_end):
        form_response = requests.post(
            url = 'http://127.0.0.1:5000/' + url_end,
            headers= {
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        return form_response