# runs with the base directory as the folder from where files are imported
from flask_assets import Environment
import assets
from webassets.loaders import PythonLoader as PythonAssetsLoader
from flask import Flask, render_template, request, redirect, url_for
import os
import settings

app = Flask(__name__)
assets_env =  Environment(app)
assets_loader = PythonAssetsLoader(assets)
# print ('assets are', help(assets_loader.load_bundles()))
for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)

env = os.environ.get('CURRENT_ENV', 'Prod')
app.config.from_object('settings.{0}Config'.format(env))
app.config['ENV'] = env
from models import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    user = User(request.form['username'], request.form['message'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('message'), username=user.username)

@app.route('/message/<username>')
def message():
    user = User.query.filter_by(username=username).first_or_404() 
    return render_template('message.html', username=user.username,
                                           message=user.message)

if __name__ == '__main__':
    app.run()
