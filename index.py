import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine. I want to create an easy way to host your modest web  
      site on App Engine. My approach is dead simple. All I use is some boilerplate 
      code almost anyone can follow. You can have multiple pages and use template  
      variable features that are part of App Engine's WebApp Framework. Most modest 
      web sites don't do much more than this. Your certainly free to expand on what 
      you find here.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class SuccPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'success.html')
    self.response.out.write(template.render(path, template_values))
	
class GoPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'email.php')
    self.response.out.write(template.render(path, template_values))
	
class ProPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'projects.html')
    self.response.out.write(template.render(path, template_values))	

class WatPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'watershed.html')
    self.response.out.write(template.render(path, template_values))

class HeaPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'health.html')
    self.response.out.write(template.render(path, template_values))

class EduPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'edu.html')
    self.response.out.write(template.render(path, template_values))

class ConPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'const.html')
    self.response.out.write(template.render(path, template_values))

	
class GooglePage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'google338370bc64eaa16b.html')
    self.response.out.write(template.render(path, template_values))
	
class PartPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'participate.html')
    self.response.out.write(template.render(path, template_values))
	
class MissPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'mission.html')
    self.response.out.write(template.render(path, template_values))

	
class VissPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'vision.html')
    self.response.out.write(template.render(path, template_values))

class ContPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine. I want to create an easy way to host your modest web  
      site on App Engine. My approach is dead simple. All I use is some boilerplate 
      code almost anyone can follow. You can have multiple pages and use template  
      variable features that are part of App Engine's WebApp Framework. Most modest 
      web sites don't do much more than this. Your certainly free to expand on what 
      you find here.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'contactus.html')
    self.response.out.write(template.render(path, template_values))
	
class DonatePage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "A DIY primer for deploying to App Engine",
      'message1': """
      <p>The whole idea here is to show how to set up a simple static web site  
      on Google App Engine. I want to create an easy way to host your modest web  
      site on App Engine. My approach is dead simple. All I use is some boilerplate 
      code almost anyone can follow. You can have multiple pages and use template  
      variable features that are part of App Engine's WebApp Framework. Most modest 
      web sites don't do much more than this. Your certainly free to expand on what 
      you find here.</p>""",
      }

    path = os.path.join(os.path.dirname(__file__), 'donate.html')
    self.response.out.write(template.render(path, template_values))
    
class GBodyPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "Deploying Static Sites to App Engine",
      'message1' : "",
      }
      
    path = os.path.join(os.path.dirname(__file__), 'gbody.html')
    self.response.out.write(template.render(path, template_values))
	
class AbtPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title1': "DIY",
      'title2': "Web Guide for App Engine",      
      'slogan': "Deploying Static Sites to App Engine",
      'message1' : "",
      }
      
    path = os.path.join(os.path.dirname(__file__), 'aboutus.html')
    self.response.out.write(template.render(path, template_values))
    
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/index.html', MainPage),
									 ('/contactus.html', ContPage),
									 ('/donate.html', DonatePage),
									 ('/success.html', SuccPage),
									 ('/mission.html', MissPage),
									 ('/email.php', GoPage),
									 ('/aboutus.html', AbtPage),
									 ('/participate.html', PartPage),
									 ('/projects.html', ProPage),
									 ('/watershed.html', WatPage),
									 ('/health.html', HeaPage),
									 ('/const.html', ConPage),
									 ('/edu.html', EduPage),
									 ('/google338370bc64eaa16b.html', GooglePage),
									 ('/vision.html', VissPage),
                                     ('/gbody.html', GBodyPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()