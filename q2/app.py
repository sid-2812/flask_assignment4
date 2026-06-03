from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://admin:admin123@cluster0.rcgjvcs.mongodb.net/?appName=Cluster0")
db = client["mydatabase"]
collection = db["students"]

# Existing Form Route
@app.route("/")
def form():
    return render_template("form.html", error=None)

# Existing Submit Route
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    try:
        collection.insert_one({
            "name": name,
            "email": email
        })
        return redirect(url_for("success"))
    except Exception as e:
        return render_template("form.html", error=str(e))

# Existing Success Route
@app.route("/success")
def success():
    return render_template("success.html")

# Assignment Route
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return "Todo Item Saved Successfully"

if __name__ == "__main__":
    app.run(debug=True)