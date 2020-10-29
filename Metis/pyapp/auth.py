from flask import abort
from flask_httpauth import HTTPTokenAuth

# Using token authentication
# API Access Tokens
# When calling an API method Bearer token is given as authorization

auth = HTTPTokenAuth(scheme='Bearer')

def parseAuthHeader(token):
    '''
    Extracts the token from a HTTP Authorization header value
    of the form [scheme] [token]

    1st return value: bool - syntactical validity of token/scheme
    2nd return value: token, if valid is true
    '''

    if token is None or len(token) == 0:
        return False, ''

    # atm we only support the Bearer scheme
    parts = token.split(' ', 1)
    if len(parts) != 2 or parts[0] != 'Bearer':
        print("Encountered unsupported auth scheme or token: " + token)
        return False, ''

    return True, parts[1]

@auth.error_handler
def auth_error(status):
    # define a global authentication error handler
    # to avoid that flask-restplus marshals the error response
    # use flask to abort the current request
    abort(status)
