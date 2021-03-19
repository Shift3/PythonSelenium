from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

# print statements are emulating the pytest unit test.
options = Options()
headless = True
selenium = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
selenium.get("https://duckduckgo.com/")

# This should be False
print(selenium.page_source.__contains__('Your username and/or password were incorrect.'))

# This should be True
print(selenium.page_source.__contains__('duckduckgo'))

# Works well with https://addons.mozilla.org/en-US/firefox/addon/xpath_finder/
duck_search = selenium.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
duck_search.send_keys("test")
duck_search.send_keys(Keys.RETURN)

# This should be False
print(selenium.page_source.__contains__('test'))

# Two main reasons to use selenium:
# 1. Integration tests. Make sure the user can do all the feature test things from clicking buttons, filling out forms, etc...
# 2. Scrape data off a website without an API (or existing API for the data you require). Example: Youtrack issues, Gitlab issues, and HIPAA/ACA compliance (change management tracking).
