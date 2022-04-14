import asyncio
import os
import time
from time import sleep
from typing import Optional
import aiohttp
import requests
from fastapi import Depends, FastAPI
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import MovieIn_Pydantic, Movie_Pydantic, Movies
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from typing import List


#creating a json object to send to api
class Movie(BaseModel):
    url: str   #this field is required  
    title: Optional[str] = None
    data: Optional[str] = None


app = FastAPI()


register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"), #    db_url="sqlite://:memory:", if 405 error testing.
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def single_request():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:

        url= "https://api.github.com/users/1"
        async with session.get(url) as resp:
            user = await resp.json()  #json obj can query user["name"]
        return f'speed: {time.time() - start_time}: {user}'




async def get_users(session, url):
    async with session.get(url) as resp:
        user = await resp.json()
        return user['name']


@app.get("/loop")
async def multiple_request():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:

        jobs = []
        for i in range(1,20):
            url = f'https://api.github.com/users/{i}'
            jobs.append(asyncio.ensure_future(get_users(session, url)))

        f_users = await asyncio.gather(*jobs)
        for u in f_users:
            print(u)

@app.post("/movies/", response_model=Movie_Pydantic)
async def create_movie(movie: MovieIn_Pydantic):
    movie_obj = await Movies.create(**movie.dict(exclude_unset=True))
    return await Movie_Pydantic.from_tortoise_orm(movie_obj)

@app.get("/movies/", response_model= List[Movie_Pydantic])
async def get_movies():
    return await Movie_Pydantic.from_queryset(Movies.all())
@app.get(
    "/movie/{movie_id}", response_model=Movie_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_movie(movie_id: int):
    return await Movie_Pydantic.from_queryset_single(Movies.get(id=movie_id))
@app.put(
    "/movie/{movie_id}", response_model=Movie_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_movie_data(movie_id: int, movie: Movie_Pydantic):
    await Movies.filter(id=movie_id).update(**movie.dict(exclude_unset=True))
    return await Movie_Pydantic.from_queryset_single(Movies.get(id=movie_id))

