from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'mailMarketing'

urlpatterns = [
  path('email_form/', TemplateView.as_view(template_name="email_marketing/send.html")),
  path('push_mail/', views.send_email, name="send_mail")]
