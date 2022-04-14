import asyncio
import os.path
from os import path
from time import sleep
from webbrowser import get
import json
import pytest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_setup import get_webdriver_for

#sel = selenium
#soup = beautiful soup

@pytest.mark.asyncio
async def test_sel_screenshot(test_driver):
    # the docker location is in the service directory already just give file name
    # if file exist remove it and check if its gone
    # send a request in selenium to go to google get screenshot and save in currentdir
    # check if it screenshot exist in current directory
    #testing try block as well
    try:
        pic_location = "screenshot2.png"

        if os.path.isfile(pic_location):
            os.remove(pic_location)

        test_driver.get('https://www.google.com/')
        test_driver.save_screenshot(pic_location)
        test_driver.quit()
        assert path.exists(pic_location) == True
    except AssertionError as ex:
        test_driver.quit()
        assert "Raised Assertion: " == ex
        # this assert ensures the test failed and prints reason...





#this is testing beautiful soup
@pytest.mark.asyncio
async def test_soup_viewsource():
    #this function only testing beautoful soup scraping
    # gets the movie rating and checks if score between 0 and 100
    #-- list of all Json values: for i in json_object['scoreboard']:
    url = "https://www.rottentomatoes.com/m/the_batman"
    req = requests.get(url)
    html = BeautifulSoup(req.text, "html.parser")
    content = html.find(
        "script", attrs={"id": "score-details-json"}
    )
    json_object = json.loads(content.contents[0])
    result = json_object['scoreboard']['audienceScore']

    assert 1 < result
    assert 100 > result


@pytest.mark.skip(reason="only use this for simple selenium testing deprecated")
async def test_screenshot2_sel():
    # this is testing easy connect without chrome image in docker-compose
    # can delete the google image from chrome if want to test with desired cap only
    # wanting more features need the chrome image instance
    driver2 = webdriver.Remote(
        "http://selenium:4444/wd/hub", desired_capabilities2=DesiredCapabilities.CHROME
    )

    driver2.get("https://google.com")
    driver2.save_screenshot("screenshot2.png")
    driver2.quit()
    return "adas'"


