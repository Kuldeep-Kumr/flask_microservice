from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='Nagarro_user_micorservice',
    )

    from .database import db
    db.configure_app_for_db(app)

    from .backend import routers
    app.register_blueprint(routers.bp)

    return app
