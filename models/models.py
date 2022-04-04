from django.db import models


class TelegramUser(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    full_name = models.CharField(max_length=56, default=str)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_action_date = models.DateTimeField(auto_now=True)
    login = models.CharField(max_length=56, default=str)
    password = models.CharField(max_length=56, default=str)
    cookies = models.JSONField(default=list)

    def __str__(self) -> str:
        return "%d" % self.id
