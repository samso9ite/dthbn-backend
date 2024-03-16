from django.urls import path
from . import views

app_name = 'profPortal'

urlpatterns = [
    # path('dashboard/', views.Profile.as_view(), name='dashboard'),
    # path('update/', views.Update.as_view(), name='update'),
    # path('create_account/', views.ProfAccntView.as_view(), name='createAccount'),
    # path('update_account/<int:pk>', views.ProfAccntUpdateView.as_view(), name='accountUpdate'),

    path('add-profile', views.AddProfessionalView.as_view(), name="add_profile"),
    path('update-profile', views.UpdateProfileView.as_view(), name="update_profile"),
    path('get-profile/<int:profuser>', views.RetrieveProfView.as_view(), name='get-profile'),
    path('list-license/<int:id>', views.ListLicenseView.as_view(), name="list_license")
] 