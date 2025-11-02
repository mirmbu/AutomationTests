import pytest

def test_e2e(travel):
    travel.buyFirst()
    travel.clickDestination()
    travel.chooseDates()
    travel.fillStartDate()
    travel.clickEndDate()
    travel.expectTotalDays()
    travel.clickPassengerDetail()
    travel.expectPassengerDetailPage()



