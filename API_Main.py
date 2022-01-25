#########################
#Improting Modules
import flask
from flask.helpers import send_file
import git

#########################
#App Metadata
App_Description = "Program to Create an API for a technical test"
App_Version = "1.0"

#########################
#Defining the flask app instance
app = flask.Flask(__name__)

#########################
#Defining the URL path mapping

#Path: /
@app.route('/')
def api_root():
    return ("hello world")

#Path: /health  
@app.route('/health')
def apipath_health():
    return 'OK', 200

#Path: /metadata
@app.route('/metadata')
def apipath_metadata():
    repo = git.Repo(search_parent_directories=True)

    dict1 = {}
    List1 = []
    dict2 = {}

    dict1['version'] = App_Version
    dict1['description'] = App_Description
    dict1['lastcommit'] = repo.head.object.hexsha
    List1.append(dict1)
    dict2['myapplication'] = List1

    return (dict2)

#ERROR: /NOT FOUND
@app.errorhandler(404) 
def invalid_route(e): 
    return "404 - Not Found - Please check the URL Path",404

#ERROR: Server side issue
@app.errorhandler(500) 
def invalid_route(e): 
    return "Error 500 - Something went wrong on the Server",500

#Path: /easteregg
@app.route('/easteregg')
def apipath_easteregg():
    return send_file("aura.gif", mimetype='image/gif')

if __name__ == "__main__":
    app.run()