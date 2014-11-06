import os
from flask import Flask
from flask import request
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route("/")
def listcur():
  mypath = ('.')
  onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
  liststring=(', '.join(onlyfiles))
  print (liststring)
  return 'listcur'

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/")
def index():
    return 'Index Page'

@app.route('/user/<whatuser>')
def show_user_profile(whatuser):
    # show the user profile for that user
    return 'User %s' % whatuser
  
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
