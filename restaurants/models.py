from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	res_id = models.IntegerField()
	res_name = models.CharField(max_length=255)
	star_count = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{0} Review for {1}'.format(self.user.username, self.res_name)
