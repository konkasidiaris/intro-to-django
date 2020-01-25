import datetime

from django.db import models
from django.utils import timezone

# the names of the instances are in machine friendly format
# thus the underscore instead of camelcase
# they will be used as column names on database
class Question(models.Model):
    # this is used both in database schema as well as in validation
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # setting the default number of votes
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text