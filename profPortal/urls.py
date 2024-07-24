from django.urls import path
from . import views

app_name = 'profPortal'

urlpatterns = [
    path('add-profile', views.AddProfessionalView.as_view(), name="add_profile"),
    path('update-profile/<int:profuser_id>', views.UpdateProfileView.as_view(), name="update_profile"),
    path('get-profile/<int:profuser>', views.RetrieveProfView.as_view(), name='get-profile'),
    path('list-license/<int:profuser_id>', views.ListLicenseView.as_view(), name="list_license"),

    path('add-license-receipt', views.AddReceiptView.as_view(), name="add_receipt"),
    path('update-license-receipt/<int:profuser_id>', views.UpdateReceiptView.as_view(), name="update_receipt"),
    path('list-license-receipt', views.ListReceiptView.as_view(), name="list_receipt"),

    path('dashboard', views.profDashboard, name="prof_dashboard"),
    path('verify-license/<license_id>/<str:programme>', views.verifyLicense, name="verify_license"),
] 