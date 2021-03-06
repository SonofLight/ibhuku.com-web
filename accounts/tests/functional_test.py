#!/usr/bin/env python
import hashlib
import os
from datetime import timedelta

from django.core.urlresolvers import resolve
from django.test import TestCase

from django.core.signing import Signer, TimestampSigner
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest

from selenium import webdriver

from accounts.models import IbkUser, Profile
from accounts.views import AccountSignUp


#Testy McTesty is a researcher and hears about a wonderful site he can use to help organize his research better.
#He decideds to check this website out. 

#Testy clicks on the link sent to him by a friend.

#Testy notices he is on the home page. It says for him to sign up
#the title says its the sign up page.

#Testy decides to register with the site. 
#He fills in his name, email and password into the simple site.

#he submits the form and is redirected to a page that confirms and email was sent to him.

#Testy recieves the email and proceeds to confirm his account.
#He clicks on the email link and is informed his account has been veified.
#After a few seconds, the page redirects him to log-in to his account. 





#Browser Test to check for '/accounts/' url and index page title html
class AccountsSignUpTest(StaticLiveServerTestCase):
	"""
	Tests user functionality of registration process for Ibhuku User Accounts.
	"""
	#set up selenium/browser
	def setUp(self):
		#ChromeDriver
		self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
		self.browser.implicitly_wait(10)

	#tear down browser after testing
	def tearDown(self):
		self.browser.quit()

	def test_get_accounts_url(self):
		self.browser.get('http://localhost:8000/accounts/')
		self.assertIn("Sign-Up!", self.browser.title)

	def test_user_signup_creation(self):
		self.browser.get('http://localhost:8000/accounts/register/')
		self.assertIn('Sign-Up', self.browser.title)

		name_input = self.browser.find_element_by_id("signup_name")
		email_input = self.browser.find_element_by_id("signup_email")
		password_input = self.browser.find_element_by_id("signup_password")
		
		self.assertEqual(name_input.get_attribute('placeholder'), 'Name')
		self.assertEqual(email_input.get_attribute('placeholder'), 'Email')
		self.assertEqual(password_input.get_attribute('placeholder'), 'Password')

		name_input.send_keys('Testy McTesty')
		email_input.send_keys('coreygumbs@gmail.com')
		password_input.send_keys('password123')

		self.browser.find_element_by_id("submit-id-submit").submit()
		import time
		time.sleep(3)

	def test_check_success_redirect(self):
		self.browser.get('http://localhost:8000/accounts/')
		self.assertIn('Sign-Up!', self.browser.title)