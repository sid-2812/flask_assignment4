from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin123@cluster0.rcgjvcs.mongodb.net/?appName=Cluster0")
db = client["mydatabase"]
collection = db["students"]

@app.route("/")
def form():
    return render_template("form.html", error=None)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    try:
        collection.insert_one({"name": name, "email": email})
        return redirect(url_for("success"))
    except Exception as e:
        return render_template("form.html", error=str(e))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
