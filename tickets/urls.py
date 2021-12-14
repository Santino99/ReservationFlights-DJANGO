from django.urls import path
from rest_framework.routers import SimpleRouter

from tickets.views import TicketViewSet, GetIdUserLoggedView

router = SimpleRouter()
router.register('', TicketViewSet, basename='tickets')
urlpatterns = router.urls
urlpatterns.append(path('idUserLogged/<str:username>', GetIdUserLoggedView.as_view()))

