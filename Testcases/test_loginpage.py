import pytest
from selenium import webdriver
from Pageobjects.Loginpage import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen


class Test_loginpage:

    base_url = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()


    def test_loginpagetitle(self, setup):

        self.logger.info('****************test_homepagetitle******************')
        self.logger.info('****************veryfying homepage title******************')
        self.driver = setup
        self.driver.get(self.base_url)
        real_title = self.driver.title
        if real_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info('****************homepage title test passed******************')
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error('****************homepage title test failed******************')
            assert False



        


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)
        self.lp.enterusername(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        logintitle = self.driver.title
        if logintitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info('****************logintest passed******************')
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_loginpage.png")
            self.driver.close()
            self.logger.error('****************logintest failed******************')
            assert False










