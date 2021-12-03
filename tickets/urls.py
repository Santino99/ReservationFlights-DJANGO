from django.urls import path
from rest_framework.routers import SimpleRouter

from tickets.views import TicketViewSet

'''
urlpatterns = [
    path('<int:pk>/', TicketDetail.as_view()),
    path('', TicketList.as_view()),
]'''

router = SimpleRouter()
router.register('', TicketViewSet, basename='tickets')

urlpatterns = router.urls

