from django.db import models


# 用户学习的主题.
class Topic(models.Model):
	text = models.CharField(max_length=200)
	data_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
