from django.contrib import admin
from web.models import Subscribe,Customer,Feature


admin.site.register(Subscribe)


admin.site.register(Customer)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","icon","icon_background","title","description","testimonial_description","testimonial_author","author_designation","testimonial_logo"]

admin.site.register(Feature)