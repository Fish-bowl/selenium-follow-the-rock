from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot(): 
	def __init__(self, email, password):
		self.browser = webdriver.Chrome()
		self.email = email
		self.password = password


	def signIn(self): 
		self.browser.get('https://www.instagram.com/accounts/login/')
		emailInput = self.browser.find_element_by_name('username')
		passwordInput = self.browser.find_element_by_name('password')
		emailInput.send_keys(self.email)
		passwordInput.send_keys(self.password)
		passwordInput.send_keys(Keys.ENTER)
		time.sleep(6)


	def followWithUsername(self, username):
		self.browser.get('https://www.instagram.com/'+ username + '/')
		time.sleep(4)
		followButton = self.browser.find_element_by_css_selector('button')
		if (followButton.text != 'Following'):
			followButton.click()
			time.sleep(4)
		else: 
			print("You are already following this user!!!")


	def unfollowWithUsername(self, username):
		self.browser.get('https://instagram.com/' + username + '/')
		time.sleep(2)
		followButton = self.browser.find_element_by_css_selector('button')
		if (followButton.text == 'Following'):
			followButton.click()
			time.sleep(2)
			confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
			confirmButton.click()
		else:
			print("you are not folowing this user")


bot = InstagramBot('Your email', 'your password')
bot.signIn()
bot.followWithUsername('therock')
bot.unfollowWithUsername('therock')
