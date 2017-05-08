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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        error = self.request.get("error")

        if error:
            error_esc = cgi.escape(error, quote=True)
            if error_esc == 'Please enter a username':
                username_error = '<p class="error" style="color:red">' + error_esc + '</p>'
                password_error = ''
                email_error = ''
            elif error_esc == 'Username cannot contain spaces':
                username_error = '<p class="error" style="color:red">' + error_esc + '</p>'
                password_error = ''
                email_error = ''
            elif error_esc == 'Please enter a password':
                password_error = '<p class="error" style="color:red">' + error_esc + '</p>'
                username_error = ''
                email_error = ''
            elif error_esc == 'Passwords do not match':
                password_error = '<p class="error" style="color:red">' + error_esc + '</p>'
                username_error = ''
                email_error = ''
            elif error_esc == 'Invalid Email':
                email_error = '<p class="error" style="color:red">' + error_esc + '</p>'
                username_error = ''
                password_error = ''
        else:
            username_error = ''
            password_error = ''
            email_error= ''

        header = "<h1>Signup</h1>"
        signupform = """
            <form method='post'>
                <table>
                    <tr>
                        <td><label>Username: </label></td>
                        <td><input name='username'></input></td>
                        <td><label>{}</label></td>
                    <tr>
                        <td><label>Password: </label></td>
                        <td><input type='password' name='password'></input></td>
                        <td><label>{}</label></td>
                    <tr>
                        <td><label>Retype Password: </label></td>
                        <td><input type='password' name='repassword'></input></td>
                        <td><label>{}</label></td>
                    <tr>
                        <td><label>Email (optional): </label></td>
                        <td><input type='email' name='email' ></td>
                        <td><label>{}</label></td>
                    <tr>
                        <td><input type='submit' value='Submit' name='submit'/></td>
                </table>
            </form>
        """.format(username_error, password_error, password_error, email_error)
        self.response.write(header + signupform)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        repassword = self.request.get('repassword')
        email = self.request.get('email')

        if username =="":
            username_error = "Please enter a username"
            self.redirect("/?error=" + username_error)
        elif " " in username:
            username_error = "Username cannot contain spaces"
            self.redirect("/?error=" + username_error)
        elif password =="" or repassword == "":
            password_error = "Please enter a password"
            self.redirect("/?error=" + password_error)
        elif password != repassword:
            password_error = "Passwords do not match"
            self.redirect("/?error=" + password_error)
        elif email != "" and "@" not in email:
            email_error = "Invalid Email"
            self.redirect("/?error=" + email_error)
        else:
            self.response.write("Hello, " + username + ". Thanks for signing up!")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
