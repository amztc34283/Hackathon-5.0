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

@app.route("/testsidebar")
def testsidebar():
    labels = ["Billy","Michael","Brandon","Tony","Jonah"]
    values = [10,10,10,10,10]
    return render_template('testsidebar.html',values=values,labels=labels)

@app.route("/challenge")
def challenge():
    labels = ["Billy","Michael"]
    values = [0,0]
    return render_template('challenge.html',values=values,labels=labels)

@app.route("/testchallenge")
def testchallenge():
    return render_template('testdoublesidebar.html')

if __name__ == "__main__":
    app.run()
