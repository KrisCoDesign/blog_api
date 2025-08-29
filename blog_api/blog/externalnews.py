import http.client, urllib.parse

conn = http.client.HTTPSConnection('api.thenewsapi.com')

params = urllib.parse.urlencode({
    'api_token': 'uDTC4U7yWIC4bRC46G1wHTfEScx7KpOg7iNKoE7w',
    'categories': 'global,business,tech',
    'limit': 5,
    })

conn.request('GET', '/v1/news/top?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))