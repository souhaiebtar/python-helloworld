from flask import Flask
from flask import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s endpoint was reached', level=logging.DEBUG)
logging.warning('This will get logged to a file')


app = Flask(__name__)


@app.route("/status")
def healthcheck():
    logging.debug('status')
    response = app.response_class(
        response=json.dumps({"result": "OK - healty"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":12}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request successsfull')

    return "AsalamBro, i mean peace!"


if __name__ == "__main__":

    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')
