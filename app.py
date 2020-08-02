from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

#Home page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

#Accounts Page
@app.route("/accounts", methods=["POST", "GET"])
def accounts():
    return render_template("accounts.html")

if __name__ == "__main__":
    app.run()