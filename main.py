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

class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/project.html')
        self.response.write(welcome_template.render())

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('done with data store')

query_result = Questions.query().fetch(5)
x = [i for i in query_result]
shuffle(x)

print x


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/seed-data', LoadDataHandler)

], debug=True)
