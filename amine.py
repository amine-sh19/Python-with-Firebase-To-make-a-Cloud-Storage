import pyrebase
config ={
	"apiKey": "your config code here ",
    "authDomain": "your config code here ",
    "databaseURL": "your config code here ",
    "projectId": "your config code here ",
    "storageBucket": "your config code here ",
    "messagingSenderId": "your config code here ",
    "appId": "your config code here ",
    "measurementId": "your config code here "
}
firebase = pyrebase.initialize_app(config)    ## Initialize firebase ##
storage = firebase.storage()

### Creating directory in cloud ###

path_on_cloud="Pictures/pic.png"
path_local="Pictures/img.jpg"