from lib2to3.pgen2 import driver
from turtle import tilt
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ..app.main import app
from ..app.app_models.movie_model import Movie
import sys
sys.path.append("../app/app")

from starlette.testclient import TestClient

@pytest.fixture(scope="function")
def test_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)
    driver.set_page_load_timeout(5)
    return driver

@pytest.fixture(scope="function")
def test_movie():
    def _test_movie(title, url, data):
        movie = Movie(title=title, url=url, data=data)
        return movie    
    
    return _test_movie

@pytest.fixture(scope='session', autouse=True)
def tear_down():
    # Will be executed before the first test
    yield 
    # Will be executed after the last test
    print('finished test')

@pytest.fixture(scope="module")
def test_app():
    # set up
    return app