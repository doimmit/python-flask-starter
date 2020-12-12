import os
from flask import Flask, request
from flask_cors import CORS
from flask_restplus import Api, Resource
from app.const.api_model import ApiModel

from app.routes.module import get_test
from app.const.config import app_config

app = Flask(__name__)
CORS(app)

api = Api(title='Flask API Server', description='')
ns_module = api.namespace('module')

config_name = os.environ.get('FLASK_ENV') or 'local'
os.environ['FLASK_ENV'] = config_name
config = app_config[config_name]

api.init_app(app)
apiModel = ApiModel(api)


@ns_module.errorhandler(Exception)
def handle_exception(error):
    return {'request': request.get_json()}

@ns_module.route('/get_test')
class DetectorInferenceImage(Resource):
    @ns_detector.expect(apiModel.detectInferenceModel)
    def get(self):
        request_body = request.get_json()
        input_value = request_body['input_value']
        return get_test(input_value)


if __name__ == '__main__':
    app.run(debug=config.DEBUG_MODE, host='0.0.0.0', port=5000)