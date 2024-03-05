from selenium import webdriver
import time



def commenter():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com") 
    username_xpath ='//*[@id="email"]'
    password_xpath = '//*[@id="pass"]'
    loginbtn = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'

    unxpath = driver.find_element("xpath", username_xpath)
    passxpath = driver.find_element("xpath", password_xpath)
    loginxpath= driver.find_element("xpath", loginbtn)
    unxpath.send_keys("0945233999")
    passxpath.send_keys("Qwe@1234567")
    loginxpath.click()

    commentLineXpath = ''

    time.sleep(15)

commenter()