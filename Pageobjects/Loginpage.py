from selenium import webdriver

class Loginpage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"


    def __init__(self, driver):
        self.driver = driver


    def enterusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)


    def enterpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def clicklogout(self):
        self.driver.find_element_by_linktext(self.link_logout_linktext).click()
