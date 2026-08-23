def create_app(test_config=None):
    from flask import Flask

    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY="dev-change-me")

    if test_config:
        app.config.update(test_config)

    from .routes import bp
    app.register_blueprint(bp)

    return app
