from flask import Flask, flash, redirect, render_template, request, session, abort
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
    return render_template('testsidebar.html')

if __name__ == "__main__":
    app.run()
