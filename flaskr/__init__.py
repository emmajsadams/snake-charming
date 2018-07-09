import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from . import db
    
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/view')
    def view():
        username = request.args.get('username') or 'anon'
        db.insert('view', [None, username])
        return jsonify({
          'count': db.query_db('SELECT COUNT(*) as Count FROM view;', (), True)['Count'],
          'views': db.query_db('SELECT * FROM view;')
        })

    db.init_app(app)

    CORS(app)
    
    return app