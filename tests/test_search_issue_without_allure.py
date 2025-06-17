from pages.search_issue_page import SearchIssuePage


def test_github_issue_exists(browser):
    repo = "juliSavitskaya/qa_guru_hw_8"
    expected_text = "for test"

    search_page = SearchIssuePage(browser)

    search_page.open_github_main_page()
    search_page.click_search_button()
    search_page.search_repository(repo)
    search_page.click_repository_link(repo)
    search_page.go_to_issues_tab()
    search_page.verify_issue_title(expected_text)