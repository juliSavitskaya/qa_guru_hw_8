import allure
from allure_commons.types import Severity
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title('Проверка существования issue в репозитории')
@allure.description(
    'Тест проверяет наличие issue с заголовком "for test" в репозитории '
    'juliSavitskaya/qa_guru_hw_8 через пользовательский UI GitHub')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "juliSavitskaya")
@allure.feature("Issue")
@allure.story("Поиск issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_github_issue_exists(browser):
    repo = "juliSavitskaya/qa_guru_hw_8"
    expected_text = "for test"

    open_github_main(browser)

    search_repository(browser, repo)

    click_repository_link(browser, repo)

    go_to_issues_tab(browser)

    check_issue_title(browser, expected_text)


@allure.step('Открыть главную страницу GitHub')
def open_github_main(browser):
    browser.get("https://github.com")


@allure.step('Поиск репозитория "{repo}"')
def search_repository(browser, repo):
    search_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header-search-button"))
    )
    search_button.click()
    search_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "query-builder-test"))
    )
    search_input.send_keys(repo)
    search_input.send_keys(Keys.RETURN)


@allure.step('Клик на ссылку найденного репозитория "{repo}"')
def click_repository_link(browser, repo):
    repo_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, repo))
    )
    repo_link.click()


@allure.step('Переход на вкладку Issues')
def go_to_issues_tab(browser):
    issues_tab = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "issues-tab"))
    )
    issues_tab.click()


@allure.step('Проверить, что заголовок issue равен "{expected_text}"')
def check_issue_title(browser, expected_text):
    issue_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="issue-pr-title-link"]'))
    )
    assert issue_title.text == expected_text, f'Ожидали: {expected_text}, получили: {issue_title.text}'
