from selenium import webdriver

def sel(url):

    browser = webdriver.Chrome()

    browser.get(url)#navigates you to the facebook page

    username = browser.find_elements_by_css_selector("input[name=email]")

    username[0].send_keys()#enter your email adress or phone number you must pass it as a string

    password = browser.find_elements_by_css_selector("input[name=pass]")

    password[0].send_keys()#enter your password you must pass it as a string

    loginButton = browser.find_elements_by_css_selector("input[type=submit]")

    loginButton[0].click()#this would click on the login button

sel('https://www.facebook.com/')