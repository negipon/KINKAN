# app.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import datetime
import time
import sqlite3 as sql
import requests
import os
# import nfc
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

root = 'http://153.126.134.114'
macAddress = '1234'
apiPassword = '5U0fX3Er'

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
init_json_url = os.path.join(SITE_ROOT, 'static/json', 'init.json')
init = json.load(open(init_json_url))

class CardReader():
	def on_connect(self, tag):
		self.idm = tag.identifier.encode('hex').upper()
		return True

	def read_id(self):
		clf = nfc.ContactlessFrontend('usb')
		try:
			clf.connect(rdwr={'on-connect': self.on_connect})
		finally:
			clf.close()

@app.route('/')
def index():
	title = 'KINKAN'
	return render_template('home.html', init=init, title=title)

@app.route('/attendance')
@app.route('/attendance/')
def data(data = None):
	title = 'Attendance'
	now = datetime.datetime.now()
	time = now.strftime('%Y/%m/%d %H:%M')
	return render_template('attendance.html', init=init, title=title, time=time)

@app.route('/answers', methods = ['POST', 'GET'])
@app.route('/answers/', methods = ['POST', 'GET'])
def answers():
	title = 'Thanks!'
	if request.method == 'POST':
		try:
			# cr = CardReader()
			# cr.read_id()

			now = datetime.datetime.now()
			t = now.strftime('%Y/%m/%d %H:%M')

			url = root + '/api/attendance.json'
			params = {
						'card_id' : '6C34EF0B',
						'base' : request.form['place'],
						'timeAttendance' : request.form['state'],
						'time' : int(time.time()),
						'mac_address' : macAddress,
						'password' : apiPassword
					}

			req = requests.post(url=url, params=params)

			# clf.close()

		except:
			name = ''
			# clf.close()

		finally:
			if req.json()['result'] == 1:
				return render_template('answers.html', init=init, title=title, name=req.json()['staff_name'], place=req.json()['base_name'], state=req.json()['timeAttendance'], time=t)
			else:
				return render_template('answers.html', title=req.json()['result'])

@app.route('/add-employee', methods = ['POST', 'GET'])
def enternew():
	title = 'Add Employee'

	if request.method == 'POST':
		try:
			cr = CardReader()
			cr.read_id()

			clf.close()

		except:
			clf.close()

		finally:
			return render_template('employee.html', card_id=cr.idm, title=title)

	else:
		return render_template('employee.html', init=init, title=title)

@app.route('/employee-list')
def list():
	title = 'Employee List'

	url = root + '/api/staff/list.json'
	params = {
				'mac_address' : macAddress,
				'password' : apiPassword
			}

	req = requests.get(url, params=params)

	if req.json()['result'] == 1:
		return render_template('list.html', init=init, rows = req.json()['staffs'], title=title)
	else:
		return render_template('list.html', init=init, title=req.json()['result'])


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
