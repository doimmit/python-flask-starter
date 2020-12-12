from flask_restplus import fields


class ApiModel:
    def __init__(self, api):
        self.getTestModel = api.model('getTest', dict(
            input_value=fields.String(example='Hi')
        ))