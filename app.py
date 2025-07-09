import os
from flask import Flask

app = Flask(__name__)

# Get the secret key from an environment variable named 'FLASK_SECRET_KEY'
# It's good practice to provide a fallback for local development
# but for production, ensure the environment variable is always set.
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

# Optional: Add a check to warn if the key is not set in development
if app.config['SECRET_KEY'] is None and app.debug: # app.debug is True if FLASK_ENV is 'development'
    print("WARNING: FLASK_SECRET_KEY environment variable not set. Using a default (NOT SECURE FOR PRODUCTION).")
    app.config['SECRET_KEY'] = 'a_very_insecure_default_key_for_dev_only'

# ... rest of your Flask app code and routes
from flask import Flask

app = Flask(__name__)


@app.route('/')

def home():

    return "🚀 Hello from Flask deployed using GitHub Actions + EC2!"


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80) 
