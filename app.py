from flask import Flask

'''
it creates an instance of the flask class, which will be your WSGI(Web server gateway interface) application.
'''

### Wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask."

@app.route("/index")
def index():
    return "Welcome to the index page."

if __name__=="__main__":
    app.run(debug=True)



