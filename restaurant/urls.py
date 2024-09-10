from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, CategoryViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls
