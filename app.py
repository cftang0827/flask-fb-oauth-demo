from flask import Flask, render_template, request
import os

import requests

app = Flask(__name__)


@app.route("/")
def main():
    return render_template(
        "login_non_js_sdk.html",
        app_id=os.getenv("APP_ID"),
        redirect_uri="https://localhost:5000/redirect",
    )


@app.route("/redirect")
def redirect():

    code = request.values.get("code")

    url = "https://graph.facebook.com/v6.0/oauth/access_token?client_id={app_id}&redirect_uri={redirect_uri}&client_secret={app_secret}&code={code_parameter}".format(
        app_id=os.getenv("APP_ID"),
        redirect_uri="https://localhost:5000/redirect",
        app_secret=os.getenv("APP_SECRET"),
        code_parameter=code,
    )
    r = requests.get(url)

    return r.json()

if __name__ == "__main__":
    app.run(ssl_context=("localhost.pem", "localhost-key.pem"), debug=True)

