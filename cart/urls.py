from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CartViewSet

router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = router.urls
