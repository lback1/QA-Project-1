from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Players, Voters

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='bookofsecrets',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        player1 = Players(player_name="Declan Rice")
        voter1 = Voters(voters_name="Luke Back")
        db.session.add(player1)
        db.session.add(voter1)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    