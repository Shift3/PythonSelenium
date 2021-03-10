from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
headless = True
selenium = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
selenium.get("https://www.google.com/")

print(selenium.page_source.__contains__('Your username and/or password were incorrect.'))
print(selenium.page_source.__contains__('Google'))

# Two main reasons to use selenium:
# 1. Integration tests. Make sure the user can do all the feature test things from clicking buttons, filling out forms, etc...
# 2. Scrape data off a website without an API (or existing API forthe data you require). Example: Youtrack issues, Gitlab issues, and HIPAA/ACA compliance (change management tracking).
