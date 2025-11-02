import pytest
from playwright.sync_api import Page
from TravelPolicyAutomationTest.pages.travel_policy_page import TravelPolicyPage

@pytest.fixture
def travel(page: Page):
    t = TravelPolicyPage(page)
    t.navigate()
    return t