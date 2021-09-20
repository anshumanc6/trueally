import csv
import datetime

from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
from flask_sqlalchemy import SQLAlchemy

import insurance
from extensions import cors, db
from settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """

    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""

    from insurance.models import Insurance
    db.init_app(app)
    with app.app_context():
        Insurance.query.delete()
        db.session.commit()
        db.create_all()

        # ins1 = Insurance(1, "20/09/2021", "Petrol", "personal", 1256, False, False, False, False, False,
        #                  920, "Male", "High", "East", "Single")
        #
        # db.session.add(ins1)

        with open("./static/data.csv", "r") as file:
            file_content = csv.reader(file)
            for idx, row in enumerate(file_content):
                if idx != 0:
                    # print(int(row[0]))
                    ins = Insurance(
                        int(row[0], base=10),
                        row[1],
                        row[3],
                        row[4],
                        row[5],
                        True if row[6] == "1" else False,
                        True if row[7] == "1" else False,
                        True if row[8] == "1" else False,
                        True if row[9] == "1" else False,
                        True if row[10] == "1" else False,
                        int(row[2], base=10),
                        row[11],
                        row[12],
                        row[13],
                        row[14],
                    )
                    db.session.add(ins)
                    # print(row)
        db.session.commit()


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(insurance.views.blueprint, origins=origins)

    app.register_blueprint(insurance.views.blueprint)

# if __name__ == '__main__':
#     app.run()
