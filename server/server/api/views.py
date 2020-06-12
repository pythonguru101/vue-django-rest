from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http.response import JsonResponse

import json

from .permissions import (
    AdminOrUserCanEdit,
)
from .models import (
    User,
    Shop,
)
from .serializers import (
    UserSerializer,
    ShopSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        IsAuthenticated,
    )

    @detail_route(methods=['get'])
    def shops(self, request, pk=None):
        queryset = Shop.objects.filter(user__pk=pk).order_by('-created')

        context = {'request': request}

        serializer = ShopSerializer(queryset, context=context, many=True)

        return Response(serializer.data)


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.order_by('-created')
    serializer_class = ShopSerializer

    permission_classes = (
        IsAuthenticated,
        # AdminOrUserCanEdit,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super(ShopViewSet, self).perform_create(serializer)


@api_view(('GET',))
def user_info(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    return JsonResponse({
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_superuser': user.is_superuser
    })
