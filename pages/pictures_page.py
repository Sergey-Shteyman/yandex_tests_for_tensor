from selenium.webdriver.common.by import By
from .base_page import BasePage


class PicturesPage(BasePage):

    first_category_picture = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    PAGE_DESCRIPTION = (By.TAG_NAME, "title")
    first_picture_inside_category = (By.CSS_SELECTOR, ".serp-item_pos_0")
    open_picture_container = (By.CSS_SELECTOR, ".MMImageContainer")
    open_picture_link = (By.CSS_SELECTOR, ".MMImage-Preview")
    next_picture_button = (By.CSS_SELECTOR, ".CircleButton_type_next")
    prev_picture_button = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    pictures_link = (By.XPATH, '//div[text()="Картинки"]')

    def check_actual_url(self):
        assert self.browser.current_url[:25] == "https://yandex.ru/images/", "Current URL is wrong"

    def should_be_pictures_link(self):
        assert self.is_element_present(*self.pictures_link), "Pictures link is not presented"

    def go_to_pictures(self):
        self.browser.find_element(*self.pictures_link).click()

    def go_to_first_category(self):
        self.browser.find_element(*self.first_category_picture).click()

    def go_to_first_picture_in_cat(self):
        self.browser.find_element(*self.first_picture_inside_category).click()
        assert self.is_element_present(*self.open_picture_container), "Picture 1 is not open"

    def next_prev_pic(self):
        pic1 = self.browser.find_element(*self.open_picture_link)
        pic1 = pic1.get_attribute("src")

        self.browser.find_element(*self.next_picture_button).click()
        self.browser.find_element(*self.prev_picture_button).click()

        pic2 = self.browser.find_element(*self.open_picture_link)
        pic2 = pic2.get_attribute("src")
        assert pic1 == pic2, "1st pic is not the same as before"

