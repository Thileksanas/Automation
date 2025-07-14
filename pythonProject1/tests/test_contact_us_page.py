def test_contact_us_page(self):
    # Click More
    self.wait.until(EC.presence_of_element_located(HomeLocators.MORE_BUTTON))
    self.home_page.click_more()
    time.sleep(2)

    # Click Contact Us
    self.wait.until(EC.presence_of_element_located(MoreLocators.CONTACT_US_BUTTON))
    self.more_page.click_contact_us()
    time.sleep(2)

    # Verify Contact Us page
    self.wait.until(EC.presence_of_element_located(ContactUsLocators.CONTACT_US_TEXT))
    assert self.contact_us_page.verify_contact_us_text(), "Contact Us page not visible"
    time.sleep(2)

    # Go back to More and Home
    self.driver.back()
    time.sleep(1)
    self.driver.back()
    time.sleep(1)
