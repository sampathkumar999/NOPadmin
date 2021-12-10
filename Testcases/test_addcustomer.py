import pytest
from Pageobjects.Loginpage import Loginpage
from Pageobjects.addcustomerpage import Addcustomer
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.enterusername(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickCustomermenu()
        self.addcust.ClickCustomer()

        self.addcust.ClickAddcustomer()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.EnterEmail(self.email)
        self.addcust.EnterPassword("test123")
        self.addcust.SelectCustomerRoles("Guests")
        self.addcust.SelectManagerOfVendor("Vendor 2")
        self.addcust.SelectGender("Male")
        self.addcust.EnterFirstname("sampath")
        self.addcust.EnterLastname("Kumar")
        self.addcust.EnterDOB("7/05/1994")  # Format: D / MM / YYY
        self.addcust.EnterCompanyname("busyQA")
        self.addcust.EnterAdminContent("This is for testing.........")
        self.addcust.ClickSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))