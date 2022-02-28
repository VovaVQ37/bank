from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'profile'

    def __str__(self):
        return self.name + ' ' + self.last_name

    def __unicode__(self):
        return self.name + ' ' + self.last_name


class Account(models.Model):
    account_number = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    total = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'account'

    def __str__(self):
        return str(self.account_number)

    def __unicode__(self):
        return self.account_number


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver')
    total = models.BigIntegerField()
    date_time = models.DateTimeField(default=timezone.now)
    successful = models.BooleanField()

    class Meta:
        verbose_name = 'transaction'

    def __str__(self):
        return str(self.pk)

    def __unicode__(self):
        return self.pk
