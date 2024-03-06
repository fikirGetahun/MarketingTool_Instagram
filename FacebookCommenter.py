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

    ### this is inside a specfic page list of posts
    comment_field_skeleton_facebook_PAGE = """/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/div/div[1]/div/div[1]/p"""
    ### differences occures at string possitons 28, 46, 64, 92, 110, 128, 158, 176, 194
    ### all we have to do is changing the number loop itrations on those numbers 1... up to whatever

    
    commentLineXpath = ''

    time.sleep(15)

commenter()