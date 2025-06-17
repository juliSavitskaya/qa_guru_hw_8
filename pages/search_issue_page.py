from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchIssuePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.header-search-button")
    SEARCH_INPUT = (By.ID, "query-builder-test")
    ISSUES_TAB = (By.ID, "issues-tab")
    ISSUE_TITLE_LINK = (By.CSS_SELECTOR, '[data-testid="issue-pr-title-link"]')

    def open_github_main_page(self):
        """Открыть главную страницу GitHub"""
        self.browser.get("https://github.com")
        return self

    def click_search_button(self):
        """Кликнуть по кнопке поиска"""
        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()
        return self

    def search_repository(self, repo_name):
        """Ввести название репозитория в поиск и нажать Enter"""
        search_input = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        search_input.send_keys(repo_name)
        search_input.send_keys(Keys.RETURN)
        return self

    def click_repository_link(self, repo_name):
        """Кликнуть по ссылке репозитория в результатах поиска"""
        repo_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, repo_name))
        )
        repo_link.click()
        return self

    def go_to_issues_tab(self):
        """Перейти на вкладку Issues"""
        issues_tab = self.wait.until(
            EC.element_to_be_clickable(self.ISSUES_TAB)
        )
        issues_tab.click()
        return self

    def get_issue_title_text(self):
        """Получить текст заголовка issue"""
        issue_title = self.wait.until(
            EC.visibility_of_element_located(self.ISSUE_TITLE_LINK)
        )
        return issue_title.text

    def verify_issue_title(self, expected_text):
        """Проверить заголовок issue"""
        actual_text = self.get_issue_title_text()
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        return self
