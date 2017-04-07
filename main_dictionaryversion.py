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
# distributed under  the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import webapp2
import cgi
import re

page_header ="""
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
    <title>User Sign-Up</title>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
"""
UserForm = """
<h1>Join The Party! Sign Up Here</h1>
<form action="/welcome" method="post">
<table>
    <tbody>
        <tr>
            <td>
                <label for="username">Username</label>
            </td>
            <td>
                <input name="username" type="text" value= "{username}"required>
            </td>
            <td class="error">
            <div>{error_username}</div>
        </tr>
        <tr>
            <td>
                <label for="password">Password</label>
            </td>
            <td>
                <input name="password" type="password" value required>
            </td>
            <td class="error">
            <div>{error_password}</div>
        </tr>
        <tr>
            <td>
                <label for="verify">Verify Password</label>
            </td>
            <td>
                <input name="verify" type="password" value required>
            </td>
            <td class="error">
            <div>{error_verify}</div>
        </tr>
        <tr>
            <td>
                <label for="email">Email (optional)</label>
            </td>
            <td>
                <input name="email" type="email" value= "{email}">
            </td>
            <td class="error">
            <div>{error_email}</div>
        </tr>
    </tbody>
</table>
<input type="submit">
</form>"""

page_footer ="""
</body>
</html>
"""

#validation functions

#validate username
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
   return username and USER_RE.match(username)

#validate password
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

#validate email
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


class Sign_up(webapp2.RequestHandler):
    def WriteForm(self, username="", email="", error_username="", error_password="", error_email="", error_verify=""):
        # #define error messages
        formatted_form = UserForm.format(username=username,
                                        email=email,
                                        error_username=error_username,
                                        error_password=error_password,
                                        error_email=error_email,
                                        error_verify=error_verify)

        self.response.write(formatted_form)

    def get(self):
        #can have default empty form, and create second formatted version in post method
        #other option userform.format(make error messages empty)
        self.WriteForm()

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        form_variables = {}

        form_variables['username'] = username     # { 'username': username }
        form_variables['email'] = email

        if not valid_username(username):
            have_error = True
            form_variables['error_username'] = "Sorry, that's not a valid username."

        if not valid_password(password):
            have_error = True
            form_variables['error_password'] = "Sorry, that wasn't a valid password."

        elif password != verify:
            have_error = True
            form_variables['error_verify'] = "Your passwords didn't match."

        if not valid_email(email):
            have_error = True
            form_variables['error_email'] = "That's not a valid email address."

        if have_error:
            self.WriteForm(**form_variables)

        else:
            self.redirect('/welcome?username=' + username)


class Welcome(Sign_up):
    def get(self):
        username= self.request.get('username')
        self.response.write('Welcome, ' + username)



app = webapp2.WSGIApplication([
    ('/', Sign_up),
    ('/welcome', Welcome)
], debug=True)
