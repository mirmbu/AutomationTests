from playwright.sync_api import Page, expect
from datetime import datetime, timedelta


class TravelPolicyPage:

    baseUrl = "https://digital.harel-group.co.il/travel-policy"
    startDate = datetime.today() + timedelta(days=7)
    endDate = datetime.today() + timedelta(days=36)

    start_str = startDate.strftime("%dd/%mm/%yyyy")
    end_str = endDate.strftime("%Y-%m-%d")

    def __init__(self, page: Page):
        self._page = page
        self._url = self.baseUrl
        self._buyFirst = page.locator('[data-hrl-bo="purchase-for-new-customer"]')
        self._destination = page.locator('[data-hrl-bo="USA"]')
        self._chooseDates = page.locator('[data-hrl-bo="wizard-next-button"]')
        self._startDate = page.locator('[aria-labelledby="travel_start_date-label"]')
        self._endDate = page.locator(f"button[data-hrl-bo='{self.end_str}']")
        self._totalDays = page.locator('[data-hrl-bo="total-days"]')
        self._passengerDetail = page.locator('[data-hrl-bo="wizard-next-button"]')
        self._passengerUrl = "https://digital.harel-group.co.il/travel-policy/wizard/travelers"
        self._passengerTitle = page.locator('[data-hrl-bo="screen_title"]')


    def navigate(self):
        self._page.goto(self._url, timeout=60000)

    def buyFirst(self):
        self._buyFirst.click()

    def clickDestination(self):
        self._destination.click()

    def chooseDates(self):
        self._chooseDates.click()

    def fillStartDate(self):
        self._startDate.fill(self.start_str)

    def clickEndDate(self):
        self._endDate.click()

    def clickPassengerDetail(self):
        self._passengerDetail.click()


    #Asserts
    def expectTotalDays(self):
        expect(self._totalDays).to_contain_text("30 ימים")

    def expectPassengerDetailPage(self):
        expect(self._page).to_have_url(self._passengerUrl)
        expect(self._passengerTitle).to_have_text("נשמח להכיר את הנוסעים שנבטח הפעם")