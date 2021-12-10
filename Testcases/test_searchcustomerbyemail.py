import time
import pytest
from Pageobjects.Loginpage import Loginpage
from Pageobjects.addcustomerpage import Addcustomer
from Pageobjects.searchcustomerpage import SearchCustomer
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen

class Test_SearchCustomerByEmail_005:
    baseURL = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.enterusername(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By email **********")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickCustomermenu()
        self.addcust.ClickCustomer()
        time.sleep(2)

        self.logger.info("************* searching customer by email **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.EnterEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_005 Finished  *********** ")