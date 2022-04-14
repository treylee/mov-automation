import requests
import pytest
import json
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

@pytest.mark.asyncio
@pytest.mark.skip(reason="added tortoise pydantic model")
async def test_movie_model(test_movie):
    #testing movie fixture and modl
    movie = test_movie(title="batman",url="batman.com",data="scores")
    assert "batman" == movie.title
    assert "batman.com" == movie.url
    assert "scores" == movie.data
@pytest.mark.skip(reason="added tortoise pydantic model")
async def test_create_with_badrequest(test_app):
    #check main.py for json class structure
    client = TestClient(test_app)
    #testing to see if optional data passes from main.py json Movieclass structure 
    response = client.post(url='/movies/', json={
        "id":"1",
        "tle":"optional",
        "url":"batman.com",
        "optional":"score"
    })
    assert response.status_code == 200
    #testing non optional data 422 understand syntax but cant process the non-optional url field
    response = client.post(url='/movies/', json={
        "tle":"optional",
        "thisurlfieldchanged":"batman.com",
        "optional":"score"})
    assert response.status_code == 422
@pytest.mark.skip(reason="added tortoise pydantic model")
async def test_create_with_okresponse(test_app):
    client = TestClient(test_app)
    response = client.post(url='/movies/', json={"title":"batman","url":"batman.com","data":"score"})
    assert response.status_code == 200

