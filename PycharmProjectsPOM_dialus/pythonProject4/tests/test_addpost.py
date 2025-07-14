import pytest
from utils.driver_setup import get_driver
from pages.offer_page import addpostpage


@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_fill_offer(driver):
    offer_page = OfferPage(driver)
    offer_page.fill_offer("Sana", "view the dialus web", "https://dialus")
    offer_page.clear_offer()

def test_fill_ds_collection(driver):
    ds_page = DSCollectionPage(driver)
    ds_page.fill_ds_collection("Festival", "view the dialus web", "https://dialus")

def test_fill_advertisement(driver):
    ad_page = AdvertisementPage(driver)
    ad_page.fill_advertisement("Keels", "https://dialus")
