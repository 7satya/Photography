from django.contrib import admin
from .models import photography, user_clients, portfolio, portfolioiamges

# Register your models here.
admin.site.register(photography)
admin.site.register(user_clients)
admin.site.register(portfolio)
admin.site.register(portfolioiamges)
