# requires Python 3.6 or higher
import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/evaluate",
           methods=['POST'])  # https://tableau.github.io/analytics-extensions-api/docs/ae_api_ref.html#post-evaluate
def evaluate():
    inputdata = json.loads(request.data)
    if inputdata["script"] == "+3":
        #add 3 to every member of array of numbers passed in as _arg1 (first argument)
        output = [z + 3 for z in inputdata['data']['_arg1']]
    else:
        output = 0
    return json.dumps(output)


@app.route("/info")  # https://tableau.github.io/analytics-extensions-api/docs/ae_api_ref.html#get-info
def info():
    return """{
    description: "A live demo of an analytics extension service",
    creation_time: "1613736503",
    state_path: "http://localhost",
    server_version: "0.0.123",
    name: "Tableau Analytics Extensions API Example"
  };"""


if __name__ == '__main__':
    app.run()
