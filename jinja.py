###Building dynamic url 
## Variable Rule
## Jinja 2 template Engine

###Jinja 2 template engine
'''
{{}} -> expressions to print output in html

{%...%} conditions,for loop

{#..#} this is for comments

'''
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask.</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Helloo {name} ! '
    return render_template('form.html')

#Variable rule

@app.route('/successres/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='PASSED'
    else:
        res="FAILED"

    exp={'score':score,"res":res}

    return render_template('result1.html',results=exp)

## if condition
@app.route('/successif/<int:score>')
def success1(score):
    return render_template('result.html',results=score)

@app.route('/failed/<int:score>')
def fail(score):

    return render_template('result1.html',results=score)
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0   
    if request.method=='POST':
        science=

if __name__=="__main__":
    app.run(debug=True)