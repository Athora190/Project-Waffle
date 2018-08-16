# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os
from questions_model import Questions
from questions import seed_data
from random import shuffle
# Import in main.py



the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        #seed_data()
        query_result = Questions.query().fetch(15)
        x = [i for i in query_result]
        shuffle(x)
        self.response.write(x[0])

class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/project.html')
        self.response.write(welcome_template.render())

class SoloHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/SoloChallenge.html')
        self.response.write(welcome_template.render())

class MultiHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/Playwithfriends.html')
        self.response.write(welcome_template.render())

class MultiGameHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/Triviagame.html')
        self.response.write(welcome_template.render())

class SoloGameHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/game.html')
        self.response.write(welcome_template.render())

class HowtoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/how-to-play.html')
        self.response.write(welcome_template.render())

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('done with data store')


#print x


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/seed-data', LoadDataHandler),
    ('/question', QuestionHandler),
    ('/solo',SoloHandler),
    ('/multi',MultiHandler),
    ('/sologame',SoloGameHandler),
    ('/multigame',MultiGameHandler),
    ('/how-to-play',HowtoHandler),

], debug=True)
