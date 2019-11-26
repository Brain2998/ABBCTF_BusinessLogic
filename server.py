import flask
import configparser
import equations
import base64
from flask_session import Session

app = flask.Flask(__name__)

flag="Abbflagis{[A-z0-9_]*}"

@app.route('/', methods = ['GET', 'POST'])
def root():
    if flask.request.method=='POST':
        formData=flask.request.form
        if (int(formData['x'])==flask.session['solutions'][0] and int(formData['y'])==flask.session['solutions'][1] and int(formData['z'])==flask.session['solutions'][2]):
            flask.session['tasksCount']+=1
            return flask.Response('Right')
        else:
            return flask.Response('Wrong')
    flask.session['tasksCount']=1
    return flask.send_from_directory('.', 'static/index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return flask.send_from_directory('static/css', path)

@app.route('/generateEquation')
def generateEquation():
    system=equations.generateSystem()
    flask.session['solutions']=system['solutions']
    return flask.Response(base64.b64encode(equations.createSystemImageFromText(equations.createSystemTextFromDict(system))))

if __name__ == "__main__":
    parser = configparser.ConfigParser()
    parser.read_file(open("config/config.ini", "r"))
    with open("config/" + parser.get("Crypto", "SESSION_KEY"), 'r') as f:
        sessionKey = f.read()
    app.config['SECRET_KEY']=sessionKey
    app.config['SESSION_TYPE']='filesystem'
    sess = Session()
    sess.init_app(app)
    app.run(host=parser.get("Common", "HOST"), port=parser.get("Common", "PORT"))