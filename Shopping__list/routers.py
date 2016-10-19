from rest_framework.routers import SimpleRouter

from Shopping__list.product.views import ProductViewSet


router = SimpleRouter()

router.register(r'products', ProductViewSet)
