from flask import Flask, render_template,request
import predictions as p

app = Flask(__name__)


@app.route('/', methods = ["POST"])
def home():
    if request.method == "POST":
        G1 = request.form['G1']
        result=predictions(G1)
        pk = result
    return render_template("FORM_HOTEL.html", my_grade = pk)

"""
@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        name=request.form["G1"]
    return render_template("sub.html", n = g1)   

"""
if __name__ == "__main__":
    app.run(debug=True)