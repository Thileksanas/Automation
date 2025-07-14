def test_add_post_all_forms(self):
    # Open Add Post Page
    self.home_page.click_plus_button()
    time.sleep(2)

    # -------- Offer Form --------
    self.add_post_page.select_offers_category()
    self.add_post_page.enter_mobile("0771234567")
    self.add_post_page.enter_name("Thileksana QA")
    self.add_post_page.enter_work_position("QA Engineer")
    self.add_post_page.enter_email("qa@example.com")
    self.add_post_page.click_save()
    time.sleep(2)
    self.add_post_page.click_clear()
    time.sleep(2)
    print("✅ Offers form is filled and cleared.")

    # -------- DS Collection Form --------
    self.add_post_page.select_ds_collection_category()
    self.add_post_page.enter_mobile("0772233445")
    self.add_post_page.enter_name("DS Manager")
    self.add_post_page.enter_work_position("Manager")
    self.add_post_page.enter_email("ds@example.com")
    self.add_post_page.click_save()
    time.sleep(2)
    self.add_post_page.click_clear()
    time.sleep(2)
    print("✅ DS Collection form is filled and cleared.")

    # -------- Advertisement Form --------
    self.add_post_page.select_advertisement_category()
    self.add_post_page.enter_mobile("0773344556")
    self.add_post_page.enter_name("Ad Lead")
    self.add_post_page.enter_work_position("Marketing Head")
    self.add_post_page.enter_email("ads@example.com")
    self.add_post_page.click_clear()
    time.sleep(2)
    print("✅ Advertisement form is filled.")
