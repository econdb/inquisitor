import os

from httmock import urlmatch, HTTMock, response
import json
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_mock_json(name, return_json_object=False):
    with open(os.path.join(BASE_DIR, "testdata", name + ".json")) as fstream:
        if return_json_object:
            return json.load(fstream)
        else:
            return fstream.read()


def check_auth(request):
    """

    Args:
        request (requests.Request): requests request

    Returns:
        bool: True if token is valid, false otherwise

    """
    return "Authorization" in request.headers and request.headers[
                                                      'Authorization'] == "Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"


def unauthorized_mock():
    return response(401, json.dumps({"detail": "Invalid token"}),
                    {'Content-Type': 'application/json'})


@urlmatch(netloc=r'(.*\.)?inquirim\.com', path='/api/series/')
def series_mock(url, request):
    """

    Args:
        url (str):
        request (requests.Request): requests request

    Returns:

    """
    if not check_auth(request):
        return unauthorized_mock()
    return response(200, load_mock_json("series"))
