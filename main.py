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
from random import randint
# Import in main.py



the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

question_list = Questions.query().fetch()
TOTAL = 15 #number of questions to ask
CURRENT = 0 #index of current question
question = None
answers = []

#New Main Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        global CURRENT
        global TOTAL
        global question
        global question_list

        if CURRENT < TOTAL:
          CURRENT += 1
          game_template = the_jinja_env.get_template('templates_new/game.html')
          question = question_list[randint(0,14)]
          question_list.remove(question)

          template_dict = {
            "question": question.question,
            "choice1": question.choice1,
            "choice2": question.choice2,
            "choice3": question.choice3,
            "choice4": question.choice4
          }

          self.response.write(game_template.render(template_dict))
        else:
          game_template = the_jinja_env.get_template('templates_new/final.html')
          template_dict = {"total":TOTAL}
          count = 0
          CURRENT = 0

          for i in answers:
            if i == 'correct':
              count += 1

          template_dict["correct"] = count
          if count >= 7:
              template_dict["level"] ="Congratulations you do have what it takes!"
          else:
              template_dict['level'] = "Sorry, Try again if you dare"
          self.response.write(game_template.render(template_dict))
    def post(self):
        self.get()

class ScoreHandler(webapp2.RequestHandler):
  def post(self):
    global question
    global answers

    score_template = the_jinja_env.get_template('templates_new/score.html')

    choices = [self.request.get('choice1'),
      self.request.get('choice2'),
      self.request.get('choice3'),
      self.request.get('choice4')]

    template_dict = {"scores":answers,"solution":question.correct_answer}
    #if question == None:
    #    return self.redirect(url_for('/'))
    for i in choices:
      if i:
        template_dict['choice'] = i
        if i == question.correct_answer:
          answers.append('correct')
        else:
          answers.append('incorrect')
        break


    self.response.write(score_template.render(template_dict))

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
        self.post()
    def post(self):
        welcome_template = the_jinja_env.get_template('templates/SoloChallenge.html')
        self.response.write(welcome_template.render())

class MultiHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/Playwithfriends.html')
        self.response.write(welcome_template.render())

class HowtoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/how-to-play.html')
        self.response.write(welcome_template.render())

class MultiGameHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/Triviagame.html')
        self.response.write(welcome_template.render())

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('done with data store')


#query_result = Questions.query().fetch(5)
#x = [i for i in query_result]
#shuffle(x)


#print x

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/seed-data', LoadDataHandler),
    ('/question', QuestionHandler),
    ('/solo',SoloHandler),
    ('/multi',MultiHandler),
    ('/score',ScoreHandler),
    ('/game',MainHandler),
    ('/multigame', MultiGameHandler),
    ('/how-to-play',HowtoHandler)

], debug=True)
