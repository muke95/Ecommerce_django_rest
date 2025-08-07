from django.contrib import admin
from .models import User , products, Cart  , Category

admin.site.site_header = "Ecom Admin"
admin.site.site_title = "MyShop"
admin.site.index_title = "Manage Your Store"
# Register your models here.


# admin.site.register(User)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(products, CustomerAdmin)


class CartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cart, CustomerAdmin)



class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CustomerAdmin)


