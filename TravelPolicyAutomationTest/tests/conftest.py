import pytest
from playwright.sync_api import Page, expect
from pages.TravelPolicyPage import TravelPolicyPage

@pytest.fixture
def travel(page: Page):
    t = TravelPolicyPage(page)
    t.navigate()
    return t