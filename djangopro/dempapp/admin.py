from django.contrib import admin
from .models import user,transportation,accomodation,package,booking,payment,reviews_and_ratings,pessanger_detail
# Register your models here.
admin.site.register(user)
admin.site.register(accomodation)
admin.site.register(transportation)
admin.site.register(package)
admin.site.register(booking)
admin.site.register(payment)
admin.site.register(reviews_and_ratings)
admin.site.register(pessanger_detail)

# admin.site.site_header = 'MySite Administration'
# admin.site.index_title = 'MySite Site administration'
# admin.site.site_title = 'MySite site admin'