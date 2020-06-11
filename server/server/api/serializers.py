from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
)

from .models import (
    User,
    Shop,
)


class UserSerializer(ModelSerializer):
    shops = HyperlinkedIdentityField(view_name='user-shops')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'shops',
            'phone',
            'nick_name'
        )


class ShopSerializer(ModelSerializer):
    user = HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    def get_validation_exclusions(self, *args, **kwargs):
        # exclude the user field as we supply it later on in the
        # corresponding view based on the http request
        exclusions = super(ShopSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['user']

    class Meta:
        model = Shop
        fields = '__all__'
