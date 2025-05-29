from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ProductCategory(models.Model):
    fa_title = models.CharField(max_length=50, verbose_name='عنوان دسته بندی به فارسی')
    en_title = models.CharField(max_length=50, verbose_name='عنوان دسته بندی به انگلیسی')
    url_title = models.SlugField(max_length=50, db_index=True, unique=True, null=True, blank=True, allow_unicode=True,
                                 verbose_name='عنوان در url')
    parent = models.ForeignKey(to='ProductCategory', on_delete=models.SET_NULL, verbose_name='دسته بندی والد',
                               null=True, blank=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال', db_index=True)
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده', db_index=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['en_title']
        indexes = [
            models.Index(fields=['is_active', 'is_delete'])
        ]

    def __str__(self):
        return self.en_title


class ProductBrand(models.Model):
    fa_brand = models.CharField(max_length=50, verbose_name='نام برند به فارسی')
    en_brand = models.CharField(max_length=50, verbose_name='نام برند به انگلیسی')
    url_title = models.SlugField(max_length=50, verbose_name='عنوان در url', unique=True, db_index=True,
                                 allow_unicode=True)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
        ordering = ['en_brand']

    def __str__(self):
        return self.fa_brand


class Seller(models.Model):
    name = models.CharField(max_length=60, verbose_name='فروشنده')
    location = models.CharField(max_length=60, verbose_name='شهر')
    card = models.IntegerField(verbose_name='شماره کارت فروشنده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشنده ها'


class Product(models.Model):
    fa_title = models.CharField(max_length=400, verbose_name='نام کالا به فارسی')
    en_title = models.CharField(max_length=400, verbose_name='نام کالا به انگلیسی')
    short_title = models.CharField(max_length=100, verbose_name='عنوان کوتاه')
    slug = models.SlugField(max_length=300, verbose_name='عنوان در url', allow_unicode=True, unique=True,
                                 db_index=True, null=True, blank=True, default='')
    category = models.ManyToManyField(ProductCategory, verbose_name='دسته بندی کالا', related_name='products')
    brand = models.ForeignKey(to=ProductBrand, on_delete=models.CASCADE, verbose_name='برند کالا',
                              related_name='products', null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='فروشنده کالا', related_name='products')
    inventory = models.PositiveIntegerField(default=1, verbose_name='موجودی کالا')
    price = models.IntegerField(verbose_name='قیمت به ریال', help_text='قیمت پیش از تخفیف مد نظر است.')
    off = models.IntegerField(verbose_name='درصد تخفیف', help_text='مقدار عددی وارد شود', default=0)
    new_price = models.IntegerField(verbose_name='قیمت با تخفیف', null=True, blank=True,
                                    help_text='این فیلد به صورت خودکار جنریت میشود.')
    identify = models.CharField(max_length=12, verbose_name='شناسه کالا',
                                help_text='این فیلد به صورت خودکار جنریت میشود.')
    description = models.TextField(verbose_name='توضیحات کالا')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_active', 'is_delete', 'new_price', 'created_at', 'updated_at'])
        ]

    def __str__(self):
        return self.fa_title

    # def save(self, *args, **kwargs):
    #     self.url_title = slugify('short_title')
    #     return super().save(*args, **kwargs)


class Slider(models.Model):
    image = models.ImageField(upload_to='shop/products/product_images/%Y/%m/%d', verbose_name='تصویر محصول')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='محصول', related_name='sliders')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.pk)


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_specifications',
                                verbose_name='کالا')
    key = models.CharField(max_length=50, verbose_name='عنوان مشخصه')
    value = models.CharField(max_length=75, verbose_name='مقدار مشخصه')

    def __str__(self):
        return f'{self.key} : {self.value}'

    class Meta:
        verbose_name = 'ویژگی کالا'
        verbose_name_plural = 'ویژگی های کالا'


class ProductColor(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='product_color', verbose_name='کالا')
    name = models.CharField(max_length=7, verbose_name='نام رنگ')
    color_hex = models.CharField(max_length=14, verbose_name='کد رنگ (hex)')

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ های محصول'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='product_size', verbose_name='کالا')
    name = models.CharField(max_length=4, verbose_name='سایز', help_text='مثال: sm, md, lg, xl')

    class Meta:
        verbose_name = 'سایز محصول'
        verbose_name_plural = 'سایزهای محصول'

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    class CommentStatus(models.TextChoices):
        PENDING = 'DF', 'Pending - (در دست بررسی)'
        PUBLISHED = 'PB', 'Published - (منتشر شده)'
        REJECTED = 'RJ', 'Rejected - (رد شده)'

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='comments')
    parent = models.ForeignKey(to='ProductComment', on_delete=models.CASCADE, verbose_name='پاسخ نظر', null=True,
                               blank=True)
    name = models.CharField(max_length=30, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن نظر')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='امتیاز',
                                 default=0)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    status = models.CharField(max_length=2, choices=CommentStatus.choices, default=CommentStatus.PENDING,
                              verbose_name='وضعیت')

    class Meta:
        verbose_name = 'نظر یا کامنت'
        verbose_name_plural = 'نظرات'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=('status',))
        ]

    def __str__(self):
        return self.name


class Strength(models.Model):
    comment = models.ForeignKey(to=ProductComment, on_delete=models.CASCADE, verbose_name='نظر',
                                related_name='strengths')
    value = models.CharField(max_length=20, verbose_name='نقطه قوت کالا')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'نقطه قوت کالا'
        verbose_name_plural = 'نقاط قوت کالا ها'


class Weak(models.Model):
    comment = models.ForeignKey(to=ProductComment, on_delete=models.CASCADE, verbose_name='نظر',
                                related_name='weak')
    value = models.CharField(max_length=20, verbose_name='نقطه ضعف کالا')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'نقطه ضعف کالا'
        verbose_name_plural = 'نقاط ضعف کالا ها'


class ProductDescription(models.Model):
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE, related_name='product_desc',
                                   verbose_name='کالا')
    title = models.CharField(max_length=50, verbose_name='عنوان', default='معرفی محصول')
    description = models.TextField(verbose_name='معرفی و توضیحات محصول')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توضیحات کالا'
        verbose_name_plural = 'توضیحات کالا'


class ProductSpecificationDetails(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, verbose_name='کالا',
                                related_name='pdc_spc_details')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    text = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='shop/products/product_specification_detail_images/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توضیحات بیشتر مشخصه کالا'
        verbose_name_plural = 'توضیحات بیشتر مشخصات کالا ها'
