import os
from flask import Flask, request, json, abort, session, app, jsonify
from flask_cors import CORS
from datetime import timedelta

import sentry_sdk
from sentry_sdk import set_tag
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://7c687b03455340d2beec8925b8acafea@o139230.ingest.sentry.io/1232413",
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
def do_something():
    if request.method == 'POST':
        sentry_sdk.capture_message("why")
        return 'yoo', 400 
    else: # GET
        set_tag("meow", "cat")
        release_me()
        return 'hi', 400

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=1)

if __name__== '__main__':
    app.run()