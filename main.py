import flask
import flask_restx


app = flask.Flask(__name__)
api = flask_restx.Api(app, doc='/docs')
ns = api.namespace('api', description='API operations')


input_model = api.model('InputModel', {
    'number1': flask_restx.fields.Integer(required=True, description='First number'),
    'number2': flask_restx.fields.Integer(required=True, description='Second number'),
    'description': flask_restx.fields.String(required=True, description='Description text')
})


@ns.route('/calculator/tube1')
class CalculateResource1(flask_restx.Resource):
    @api.expect(input_model)
    def post(self):
        data = flask.request.json

        number1 = data['number1']
        number2 = data['number2']
        description = data['description']

        result_str = f"{number1 * number2} {description}"

        return flask.jsonify({"result": result_str})


@ns.route('/calculator/tube2')
class CalculateResource2(flask_restx.Resource):
    @api.expect(input_model)
    def post(self):
        data = flask.request.json

        number1 = data['number1']
        number2 = data['number2']
        description = data['description']

        result_str = f"{number1 / number2} {description}"

        return flask.jsonify({"result": result_str})


if __name__ == '__main__':
    app.run(debug=True)
