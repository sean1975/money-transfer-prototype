import webapp2
import os
import jinja2

'''
pages = [
         'index.html',
         'personal_information.html',
         'recipient.html',
         'photocopy.html',
         'consents.html',
         'consents2.html',
         'agreement.html',
         'confirm.html',
         'complete.html'
         ]
'''

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    """Controller for handling user requests"""
    
    def render(self, page):
        template = JINJA_ENVIRONMENT.get_template(page)
        return template.render(self.request.params)
    
    def post(self):
        return self.get()
    
    def get(self):
        page = 'html/index.html'
        if len(self.request.path) > 1:
            page = 'html' + self.request.path
        #param = self.request.params
        self.response.write(self.render(page))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/[^/]*\.html', MainPage),
], debug=True)