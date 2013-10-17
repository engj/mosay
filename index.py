from google.appengine.ext import webapp, ndb
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
import logging

class MainPage(webapp.RequestHandler):
  def get(self):
    template_values={}
    path=os.path.join(os.path.dirname(__file__),'index.html')
    self.response.out.write(template.render(path,template_values))

class putImg(webapp.RequestHandler):
    def post(self):
        #imgUrl = self.request.get("url")
        #imgModulus = int(self.request.get("modulus"))
        #picture = Picture(url = imgUrl, modulus = imgModulus)
        #picture.put()
        return None

class Mosay(ndb.Model):
    currentIndex = ndb.IntegerProperty()

class Picture(ndb.Model):
    url = ndb.StringProperty()
    modulus = ndb.IntegerProperty()


application=webapp.WSGIApplication(
                                    [('/', MainPage),
                                     ('/putImg', putImg)],
                                    debug=False)
                                    
def main():
  run_wsgi_app(application)
  
if __name__=="__main__":
  main()
