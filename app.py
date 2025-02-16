from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")
  
@app.route('/artikel')
def artikel():
    return render_template("artikel.html")

@app.route('/lagerorte')
def lagerorte():
    return render_template("lagerorte.html") 
  
if __name__ == '__main__':
    app.run(debug=True)