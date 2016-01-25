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

#Author:Kartik Jagdale AKA VoidZero

import webapp2

#=====================================================
#Verification Function

def valid_day(self,day):
	if day and day.isdigit():
		day = int(day)
		if(day>=1 and day<=31):
			return day

def valid_year(self,year):
	if year and year.isdigit():
		year = int(year)
		if(year>=1900 and year<=2020):
			return year

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
month_abbrv = dict((m[:3].lower(),m)for m in months)

def valid_month(self,month):
	if month:
		short_month = month[:3].lower()
		return month_abbrv.get(short_month)    

#======================================================


form = """
Hello  Bro
<form method = "post">
<b>What is Your Birthday?</b>
	<br>
	<label>Month
		<input type = "text" name = "month" value="%(month)s">
	</label>
	
	<lable>Day
		<input type = "text" name = "day" value="%(day)s">
	<label>

	<lable>Year
		<input type = "text" name = "year" value="%(year)s">
	</lable>

	<br>
	<div style="color: red">%(error)s</div>
<br>
<input type = "submit">
</form>

"""
class MainHandler(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error})

	def get(self):
		self.write_form()

	def post(self):
		user_month = valid_month(self.request.get('month'))
		print user_month
    	user_day = valid_day(self.request.get('day'))
    	print user_day
    	user_year = valid_year(self.request.get('year'))
    	print user_year
    	if not (user_day and user_month and user_year):
    		self.write_form("Thats Not a valid date!!!",user_month,user_day,user_year)
    	else:
    		self.response.out.write("Thats a Valid Date!!!")
    	


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)


#All Other Junks that we are not using anymore

"""
# We are not using this anymore
class TestHandler(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = "text/plain"
		self.response.out.write(self.request)
		
		q = self.request.get("q")
		self.response.out.write(q)
		#self.response.out.write("\n"+str(2+2)
"""
