​from google.appengine.ext import ndb

class Mosay(ndb.Model){
    currentIndex = ndb.IntegerProperty()

class Picture(ndb.Model):
    url = ndb.StringProperty()
    modulus = ndb.IntegerProperty()

