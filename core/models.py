from django.db import models


class TimestampedModel(models.Model):
    # auto_now_add 모델이 생성될때 자동으로 시간값 들어감
    # auto_add 모델이 저장될때마다 자동으로 시간값 들어감
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
