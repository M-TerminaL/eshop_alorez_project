from django.contrib import admin
from . import models
from jalali_date import datetime2jalali

# Register your models here.

admin.sites.AdminSite.site_title = 'پنل مدیریت'
admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
admin.sites.AdminSite.index_title = 'مدیریت محتوا'


# ---- Inlines ----
class SliderInline(admin.TabularInline):
    model = models.Slider
    extra = 1


class ProductSpecificationInline(admin.TabularInline):
    model = models.ProductSpecification
    extra = 1


class ProductColorInline(admin.TabularInline):
    model = models.ProductColor
    extra = 1


class ProductSizeInline(admin.TabularInline):
    model = models.ProductSize
    extra = 1


class ProductDescriptionInline(admin.TabularInline):
    model = models.ProductDescription
    extra = 1


class ProductSpecificationDetailsInline(admin.TabularInline):
    model = models.ProductSpecificationDetails
    extra = 1


class StrengthInline(admin.TabularInline):
    model = models.Strength
    extra = 1


class WeakInline(admin.TabularInline):
    model = models.Weak
    extra = 1


# -----------------

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y %H:%M:%S')

    @admin.display(description='تاریخ ویرایش', ordering='updated_at')
    def get_updated_jalali(self, obj):
        return datetime2jalali(obj.updated_at).strftime('%a, %d %b %Y %H:%M:%S')

    list_display = ['fa_title', 'en_title', 'brand', 'off', 'new_price', 'inventory',
                    'get_created_jalali',
                    'get_updated_jalali',
                    'is_active',
                    'is_delete']
    list_filter = ['is_active', 'is_delete', 'off', 'brand']
    list_editable = ['is_active', 'off', 'inventory', 'brand']
    list_per_page = 20
    prepopulated_fields = {
        'slug': ['short_title']
    }
    search_fields = ['fa_title', 'en_title', 'short_title', 'off', 'new_price', 'price']
    inlines = [SliderInline, ProductSpecificationInline, ProductColorInline, ProductSizeInline,
               ProductDescriptionInline, ProductSpecificationDetailsInline]


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['fa_title', 'en_title', 'parent', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    list_editable = ['parent', 'is_active', 'is_delete']
    list_per_page = 15
    prepopulated_fields = {
        'url_title': ['en_title']
    }
    search_fields = ['fa_title', 'en_title']


@admin.register(models.ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['fa_brand', 'en_brand']
    list_per_page = 10
    prepopulated_fields = {
        'url_title': ['en_brand']
    }
    search_fields = ['fa_brand', 'en_brand']


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y %H:%M:%S')

    list_display = ['pk', 'product', 'get_created_jalali']
    list_filter = ['created_at']


@admin.register(models.ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product']


@admin.register(models.ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'color_hex']
    list_editable = ['color_hex']
    list_filter = ['name']
    list_per_page = 20
    search_fields = ['color_hex', 'name']


@admin.register(models.ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product']
    list_per_page = 20
    search_fields = ['product']


@admin.register(models.ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y %H:%M:%S')

    list_display = ['name', 'email', 'product', 'user', 'rating', 'get_created_jalali', 'status']
    search_fields = ['name', 'email']
    list_filter = ['status', 'rating']
    list_per_page = 10
    inlines = [StrengthInline, WeakInline]


@admin.register(models.Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment']
    list_per_page = 20


@admin.register(models.Weak)
class WeakAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment']
    list_per_page = 20


@admin.register(models.ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'description']
    list_per_page = 10


@admin.register(models.ProductSpecificationDetails)
class ProductSpecificationDetailsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product']
    list_per_page = 10


admin.site.register(models.Seller)
