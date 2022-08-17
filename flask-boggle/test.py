import json
from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

board = [
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A'],
        ['A','A','A','A','A']]

class FlaskTests(TestCase):
    """ Boggle game integration tests"""

    def test_index(self):
        """tests to make sure that the root html is being delivered"""
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("""<h1 class="text-center col">Boggle!</h1>""", html)
    
    def test_session(self):
        """test for board being properly added to the session on request of /"""
        with app.test_client() as client:
            res = client.get("/")
            self.assertIn('board',session)


    def test_on_board_guess(self):
        """tests that the app responds correctly to finding a word on the board"""
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = board
            res = client.get("/guess?guess=a")
            self.assertIn('board',session)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["result"], "ok")

    def test_not_on_board(self):
        """tests that the app responds correctly to not finding a word on the board"""
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = board
            res = client.get("/guess?guess=b")
            self.assertIn('board',session)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["result"], "not-on-board")
    
    def test_not_a_word(self):
        """tests that the app responds correctly to fan invalid word"""
        with app.test_client() as client:
            client.get("/")
            res = client.get("/guess?guess=thisisntinthedictionary")
            
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.json["result"], "not-word")
    
    def test_score_post(self):
        """tests that the app responds correctly to a new score submission"""
        with app.test_client() as client:
            res = client.post("/score", json={"score":0})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["newhighscore"],False)

    def test_boggle_word_find(self):
        """tests boggle itself to make sure there are no problems with the class"""
        boggle = Boggle()
        self.assertEqual(boggle.check_valid_word(board,"a"),"ok")
        self.assertEqual(boggle.check_valid_word(board,"b"),"not-on-board")
        self.assertEqual(boggle.check_valid_word(board,"qwertyuiop"),"not-word")

    # TODO -- write tests for every view function / feature!
