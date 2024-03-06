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

    ### this is link to open a specfic post in a page posts. 
    ### this will simply open the comments commented on this specfic post
    ### this will help to open posts comment by looping from one post comment to another
    comment_opening_link_facebook_PAGE = """/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/div/span"""
    ### differences occures at string possitons 82, 86, 110
    ### all we have to do is changing the number loop itrations on those numbers 1... up to whatever

    ### THIS IS the replay comment link xpath. to replay comments inside a specific posts.
    ### this is to open the replay comment feald
    replaycomment_opening_link_facebook_PAGE = """/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/ul/li[3]/div/div"""
    ### differences occures at string possitons  110,179

    commentLineXpath = ''

    time.sleep(15)

commenter()