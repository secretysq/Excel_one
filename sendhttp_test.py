import requests

def send_requests(url, method, data=None, params=None,headers=None):
    if method == 'get':
        # res = requests.get(url, params, data=data,headers=headers)
        res = requests.request(
            method=method,
            url=url,
            params=params,
            headers=headers
        )
    elif method == 'post':
        res = requests.post(url, data=params,headers=headers)


    return res