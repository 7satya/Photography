from django.db import models

# Create your models here.
class photography(models.Model):
	image_id =models.IntegerField()
	file_name =models.CharField(max_length=200)
	description= models.CharField(max_length=1000)
	client_id =models.IntegerField()
	date_uploaded =models.DateTimeField('date up')


class user_clients(models.Model):
	client_id =models.ForeignKey(photography, on_delete=models.CASCADE)
	client_name=models.CharField(max_length=200)
	username =models.CharField(max_length=200)
	password =models.CharField(max_length=16)


class portfolio(models.Model):
	portfolio_id =models.IntegerField()
	portfolio_name =models.CharField(max_length=200)

class portfolioiamges(models.Model):
	p_id =models.IntegerField()
	image_id =models.ForeignKey(photography, on_delete=models.CASCADE)
	portfolio_id=models.ForeignKey(portfolio, on_delete=models.CASCADE)

