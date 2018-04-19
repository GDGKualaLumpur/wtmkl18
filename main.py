import webapp2

class SlashRedirect(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    self.redirect('//' + self.request.host + '/wtmkl18/')

app = webapp2.WSGIApplication([
    ('/wtmkl18.*', SlashRedirect)
], debug=True)