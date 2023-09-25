from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__CONNECTION_STRING = "mysql+pymysql://new:root@docker_host/microservices_database"


def configure_app_for_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = __CONNECTION_STRING
    db.init_app(app)


def get_db():
    return db
