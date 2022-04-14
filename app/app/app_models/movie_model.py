from attr import field
from tortoise import fields, models

class Movie(models.Model):
    data = fields.TextField()
    title = fields.TextField()
    url = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url
