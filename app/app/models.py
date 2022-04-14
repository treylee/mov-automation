from attr import field
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Movies(models.Model):
    id = fields.IntField(pk=True)
    data = fields.TextField()
    title = fields.TextField()
    url = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url
Movie_Pydantic = pydantic_model_creator(Movies, name="Movie")
MovieIn_Pydantic = pydantic_model_creator(Movies, name="Moviein", exclude_readonly=True)