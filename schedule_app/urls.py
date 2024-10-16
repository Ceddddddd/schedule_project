from rest_framework.routers import DefaultRouter
from .views import TimeSlotViewSet

router = DefaultRouter()
router.register(r'timeslots', TimeSlotViewSet, basename='timeslots')

urlpatterns = router.urls
