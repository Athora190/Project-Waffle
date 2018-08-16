from google.appengine.ext import ndb


 # define ndb Model
class Questions(ndb.Model):
    question =  ndb.StringProperty(required=True)
    choice1 =  ndb.StringProperty(required=True)
    choice2 =  ndb.StringProperty(required=True)
    choice3 =  ndb.StringProperty(required=True)
    choice4 =  ndb.StringProperty(required=True)
    correct_answer = ndb.StringProperty(required=True)
