from django.contrib import admin
from .models import author, book_list,profile_info


admin.site.register(author)
admin.site.register(book_list)
admin.site.register(profile_info)



