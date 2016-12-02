from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=128)
	product_description = models.TextField()
	product_cost = models.PositiveIntegerField()
	product_seller = models.ForeignKey('auth.User')
	product_beyer = models.CharField(blank=True, max_length=128)
	product_active = models.BooleanField(default=True)
	product_image = models.FileField()

	def __str__(self):
		return self.product_name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    balance = models.PositiveIntegerField(default=1000)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()


class MoneyRequest(models.Model):

	money_requester = models.ForeignKey('auth.User')
	money_amount = models.PositiveIntegerField()
	money_request_active = models.BooleanField(default=True)
	money_requester_email = models.EmailField()


	def __str__(self):
		return 'Money Request for: {}'.format(self.money_requester)

class Transaction(models.Model):
	transaction_seller = models.CharField(max_length=128)
	transaction_beyer = models.CharField(max_length=128)
	transaction_product = models.CharField(max_length=128)
	transaction_amount = models.PositiveIntegerField()
	transaction_date = models.DateField(null=True)
	transaction_time = models.TimeField()


	def __str__(self):
		return 'Transaction #: {}'.format(self.id)


