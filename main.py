#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import cgi

def checkusername(username):
    if username == None or username =="":
        return error
    #check if username box is left blank
    #return error message if blank
    return username

def checkpasswords(password1, password2):
    #check if both passwords are equal
    #return error message if not equal
    return password1==password2

def checkemail(email):
    #if anything written check for valid email
    #blank is okay
    return email

class MainHandler(webapp2.RequestHandler):
    def get(self):
        error = self.request.get("error")
        if error:
            error_esc = cgi.escape(error, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        else:
            error_element = ''

        header = "<h1>Signup</h1>"
        username = "Username: <form method = 'post'><input name=username></input></form>"
        password = "Password: <form method = 'post'><input type=password name=password1></input></form>"
        repassword ="Retype Password: <form method = 'post'><input type=password name=repassword></input></form>"
        email = "Email (optional): <form method = 'post'><input type=email name=email></input></form>"
        submitbutton = "<input type='submit' value='Submit' name='submit'/>"
        self.response.write(header + username + error_element + password + repassword + email + submitbutton)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        repassword = self.request.get('repassword')
        email = self.request.get('email')
        submitbutton = self.request.get('submit')
        self.response.write(username +  password + repassword + email + submitbutton)
        if username =="":
            username_error = "Please enter a username"

            self.redirect("/?error=" + username_error)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
