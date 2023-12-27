from django.contrib import admin
from CRUD_Operations.models import insertDatabase,image_gallary,newsTable

class insertAdmin(admin.ModelAdmin):
    list_display=('id','name','email','topic','describe','field')

admin.site.register(insertDatabase,insertAdmin)

class gallaryAdmin(admin.ModelAdmin):
    list_display=('id','name','image')

admin.site.register(image_gallary,gallaryAdmin)

class newsAdmin(admin.ModelAdmin):
    list_display=('id','name','topic','describe','field')

admin.site.register(newsTable,newsAdmin)