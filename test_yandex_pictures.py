
from pages.pictures_page import PicturesPage


class TestYandexPictures:
    link = "https://yandex.ru/"

    def test_yandex_pictures_link(self, browser):
        page = PicturesPage(browser, self.link)
        page.open()
        page.should_be_pictures_link()

        page.go_to_pictures()
        page.switch_tabs_up()
        page.check_actual_url()

        page.go_to_first_category()

        page.go_to_first_picture_in_cat()
        page.next_prev_pic()

