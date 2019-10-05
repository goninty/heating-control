from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

state = {'heating': True}

@app.route('/state', methods=['GET', 'POST'])
@cross_origin()
def get_state():
    global state
    if request.method == 'GET':
        return state
    elif request.method == 'POST':
        state = request.json
        return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')