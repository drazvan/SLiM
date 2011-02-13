from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


import os
import sys
from StringIO import StringIO

sys.path.append(os.path.dirname(__file__))

import antlr3

import sys

from slim.lang.output.slimParser import slimParser
from slim.lang.output.slimLexer import slimLexer

from slim.core.slimcore import SlimCore
from slim.modules import Ping
from slim.modules.lang import Lang


class MainPage(webapp.RequestHandler):
        
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, {}))
        

class SlimReceivedPage(webapp.RequestHandler):
        
    def get(self):
        self.process()

    def post(self):
        self.process()
        
    def process(self):
        self.response.headers['Content-Type'] = 'text/plain'
        
        waa = SlimCore()
        
        # register required modules
        ping = Ping()
        ping.waa = waa
        waa.register(ping, "mPing")
        
        lang = Lang()
        lang.waa = waa
        waa.register(lang, "mLang")
        
        str_stream = antlr3.ANTLRStringStream(self.request.get('code'))
        lexer = slimLexer(str_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = slimParser(tokens)
        parser.core = waa
        
        old_stdout = sys.stdout
        sys.stdout = myout = StringIO()
        
        parser.start()
        
        sys.stdout = old_stdout
        
        self.response.out.write(myout.getvalue())
        

application = webapp.WSGIApplication([('/', MainPage), 
                                      ('/slim-it', SlimReceivedPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
