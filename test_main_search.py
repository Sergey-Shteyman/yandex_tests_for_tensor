from pages.main_page import MainPage


class TestYandexSearch:

    link = "https://yandex.ru/"

    def test_search_pan_has_suggestions_to_text(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_search_pan()

        page.send_tensor_to_search_pan()
        page.should_be_suggestions_to_text()

        page.search_tensor()
        page.should_be_search_results()

        page.check_first_five_results()
