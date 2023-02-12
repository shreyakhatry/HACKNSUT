from flask import Flask, render_template, request, json
from flask_cors import CORS

#  using Mongo DB for scale

# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
# db = client["HackNSUT'23"]
# collections = db["authentication"]

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("login.html")


@app.route("/login")
def login_func():
    email = request.args.get("email")
    password = request.args.get("password")
    # if collections.find_one({"email": email, "password": password}): #  Will use this when using MongoDb 
    data = json.loads(open("users.json").read())
    result = [x for x in data if x["email"]== email and x["password"]== password]
    if result:
        return  {"status": 200, "message": "Successfully user login"}
    return {"status": 500, "message": "Failed to find the user"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)


# $ export FLASK_APP=main.py
# $ export FLASK_ENV=development
# $ flask run