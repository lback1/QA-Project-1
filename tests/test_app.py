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
        player1 = Players(players_name="Declan Rice", position="CDM", shirt_number=41)
        voter1 = Voters(voters_name="James", reason="Rice is our captain", players_id=1)
        db.session.add(player1)
        db.session.add(voter1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_players(self):
        response = self.client.get(url_for('add_players'))
        self.assertEqual(response.status_code, 200)

    def test_players_list(self):
        response = self.client.get(url_for('players_list'))
        self.assertEqual(response.status_code, 200)
      
    def test_update_players(self):
        response = self.client.get(url_for('update_players', id=1))
        self.assertEqual(response.status_code, 200)

    def test_add_voters(self):
        response = self.client.get(url_for('add_voters'))
        self.assertEqual(response.status_code, 200)
        
    def test_voters_list(self):
        response = self.client.get(url_for('voters_list'))
        self.assertEqual(response.status_code, 200)

    def test_update_voters(self):
        response = self.client.get(url_for('update_voters', id=1))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_add_players(self):
        response = self.client.post(url_for('add_players'), data=dict(players_name="test_players_name", position="test_position", shirt_number="test_shirt_number"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'Enter the player name' in response.data.decode()

    def test_add_voters(self):
        response = self.client.post(url_for('add_voters'), data=dict(voters_name="test_voters_name", reason="test_reason", players_id="test_players_id"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'Enter your name' in response.data.decode()    

class TestList(TestBase):
    def test_players_list(self):
        response = self.client.get(url_for('players_list'), data=dict(players_name="test_players_name", position="test_position", shirt_number="test_shirt_number"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'view added players' in response.data.decode() 

    def test_voters_list(self):
        response = self.client.get(url_for('voters_list'), data=dict(voters_name="test_voters_name", reason="test_reason", players_id="test_players_id"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'view added voters' in response.data.decode() 

class TestUpdate(TestBase):
    def test_update_players(self):
        response = self.client.post(url_for('update_players', id=1), data=dict(players_name="test_players_name", position="test_position", shirt_number="test_shirt_number"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'players_list' in response.data.decode()

    def test_update_voters(self):
        response = self.client.post(url_for('update_voters', id=1), data=dict(voters_name="test_voters_name", reason="test_reason", players_id="test_players_id"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'voters_list' in response.data.decode()

class TestDelete(TestBase):
    def test_delete_players(self):
        response = self.client.post(url_for('delete_players', id=1), data=dict(players_name="test_players_name", position="test_position", shirt_number="test_shirt_number"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'players_list' in response.data.decode()

    def test_delete_voters(self):
        response = self.client.post(url_for('delete_voters', id=1), data=dict(voters_name="test_voters_name", reason="test_reason", players_id="test_players_id"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert 'voters_list' in response.data.decode()