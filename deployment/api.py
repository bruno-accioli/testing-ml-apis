import joblib
import json
import logging as log
import flask
from preprocessing import preprocess_input_data


app = flask.Flask(__name__)


@app.route('/invocations', methods = ['POST'])
def invocations():
    """
    Realiza a inferencia de um unico exemplo.
    """

    if flask.request.content_type != 'application/json':
        msg = f'Content type "{flask.request.content_type}" não é suportado. Content type deve ser "application/json".'
        log.error(msg)
        json_output = json.dumps(msg)
        return flask.Response(response=json_output, status=415, mimetype='application/json')

    try:
        input_json = flask.request.get_json(force=True)
        input_data = preprocess_input_data(input_json)

        model = joblib.load('model/model.joblib')
        prediction = model.predict(input_data)

        json_output = json.dumps({"income > 50k": int(prediction[0])})
        status_code = 200
    except Exception as exp:
        msg = "Erro no ao realizar a previsão"
        log.exception(msg)
        json_output = json.dumps(msg)
        status_code = 500
    
    return flask.Response(response=json_output, status=status_code, mimetype='application/json')

if __name__=='__main__':
    app.run()
