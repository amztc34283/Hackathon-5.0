from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

### It is working.
### Use it with something like http://127.0.0.1:5000/test?Type=Personality
@app.route("/test")
def test():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [10,10,10,10,10]
    Type = request.args.get('Type') ### This check which type you are search for, e.g. Personality, Consumer Need or Values
    return render_template(
	'test.html',values=values,labels=labels,Type=Type)

@app.route("/personality/openness")
def openness():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [5,5,5,5,5]
    return render_template('/personality/openness.html',values=values,labels=labels)

@app.route("/personality/conscientiousness")
def conscientiousness():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [6,6,6,6,6]
    return render_template('/personality/conscientiousness.html',values=values,labels=labels)

@app.route("/personality/agreeableness")
def agreeableness():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [4,4,4,4,4]
    return render_template('/personality/agreeableness.html',values=values,labels=labels)

@app.route("/personality/introversion")
def introversion():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [7,7,7,7,7]
    return render_template('/personality/introversion.html',values=values,labels=labels)

@app.route("/personality/emotional_range")
def emotional_range():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [8,8,8,8,8]
    return render_template('/personality/emotional_range.html',values=values,labels=labels)

@app.route("/testchallenge")
def testchallenge():
    return render_template('testdoublesidebar.html')

if __name__ == "__main__":
    app.run()
