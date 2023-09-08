import responses
import requests

@responses.activate
def test_simple():
    responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
                  json={'error': 'not found'}, status=404)

    resp = requests.get('http://twitter.com/api/1/foobar')

    assert resp.json() == {"error": "not found"}
    print(resp.json())
@responses.activate
def test_mockapi():
    responses.add(responses.GET, 'http://google.com',json={'error':'sorry not available'},status=400)
    r = requests.get('http://google.com')
    print(r.json())
    print(r.status_code)
test_mockapi()



test_simple()