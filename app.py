import os
from flask import Flask, request, json, abort, session, app, jsonify
from flask_cors import CORS
from datetime import timedelta

import sentry_sdk
from sentry_sdk import set_tag
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://a3bc043ab9b34215b31b7dc3d444f51e@meowlificent.ngrok.io/1", # local
    integrations=[FlaskIntegration()],
    release="12345",
    environment="production",
    # debug=True,
)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)
verification_token = 'ALycD1kFFml3y4CSjpxsYda5'

@app.route("/hi")
def do_nothing():
    return 'hi', 200

@app.route('/inbound', methods=['GET', 'POST'])
def do_something_else():
    if request.method == 'POST':
        sentry_sdk.capture_message("why")
        return 'yoo', 400 
    else: # GET
        set_tag("meow", "cat")
        notifyy_hellboy()
        return 'hi', 400

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=1)

if __name__== '__main__':
    app.run()