from rest_framework import serializers
from . import models


# ------
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductBrand
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slider
        fields = '__all__'


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductSpecification
        fields = '__all__'


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductColor
        fields = '__all__'


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductSize
        fields = '__all__'


class StrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Strength
        fields = '__all__'


class WeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Weak
        fields = '__all__'


class ProductCommentSerializer(serializers.ModelSerializer):
    strengths = StrengthSerializer(read_only=True, many=True)
    weak = WeakSerializer(read_only=True, many=True)

    class Meta:
        model = models.ProductComment
        fields = '__all__'


class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDescription
        fields = '__all__'


class ProductSpecificationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductSpecificationDetails
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    sliders = SliderSerializer(read_only=True, many=True)
    product_specifications = ProductSpecificationSerializer(read_only=True, many=True)
    product_color = ProductColorSerializer(read_only=True, many=True)
    product_size = ProductSizeSerializer(read_only=True, many=True)
    comments = ProductCommentSerializer(read_only=True, many=True)
    product_desc = ProductDescriptionSerializer(read_only=True, many=True)
    pdc_spc_details = ProductSpecificationDetailsSerializer(read_only=True, many=True)

    class Meta:
        model = models.Product
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['sliders'] = SliderSerializer(instance.sliders.all(), many=True, read_only=True).data
    #     rep['product_specifications'] = SliderSerializer(instance.product_specifications.all(), many=True,
    #                                                      read_only=True).data
    #     rep['product_color'] = SliderSerializer(instance.product_color.all(), many=True, read_only=True).data
    #     rep['product_size'] = SliderSerializer(instance.product_size.all(), many=True, read_only=True).data
    #     rep['comments'] = SliderSerializer(instance.comments.all(), many=True, read_only=True).data
    #     rep['product_desc'] = SliderSerializer(instance.product_desc.all(), many=True, read_only=True).data
    #     rep['pdc_spc_details'] = SliderSerializer(instance.pdc_spc_details.all(), many=True, read_only=True).data
    #
    #     return rep
