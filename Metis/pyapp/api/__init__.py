from flask import Blueprint, url_for
from flask_restx import Api
from pyapp.api.systemstat import api as systemstat_api
from pyapp import config

@property
def specs_url(self):
    return url_for(self.endpoint('specs'), _external=True, _scheme='https')

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

if not config.DEBUG:        
    print("Adjusting specs_url to HTTPS")
    # fix swagger url when serving over https in production
    Api.specs_url = specs_url

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
metis_api = Api(blueprint, title="Metis ReST API",
    security='Bearer Auth', authorizations=authorizations,
    doc='/doc', version='1.0')

# add API endpoints
metis_api.add_namespace(systemstat_api, path='/systemstat')
