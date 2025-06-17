import allure
from pages.search_issue_page import SearchIssuePage


def test_github_issue_exists(browser):
    repo = "juliSavitskaya/qa_guru_hw_8"
    expected_text = "for test"

    search_page = SearchIssuePage(browser)

    with allure.step("Открываем главную страницу GitHub"):
        search_page.open_github_main_page()

    with allure.step("Кликаем по кнопке поиска"):
        search_page.click_search_button()

    with allure.step("Вводим в поле ввода название репозитория"):
        search_page.search_repository(repo)

    with allure.step("Выбираем нужный репозиторий"):
        search_page.click_repository_link(repo)

    with allure.step("Переходим на вкладку issues"):
        search_page.go_to_issues_tab()

    with allure.step("Проверяем заголовок issue"):
        search_page.verify_issue_title(expected_text)
