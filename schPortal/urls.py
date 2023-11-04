from django.urls import re_path as url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'schoolPortal'
urlpatterns = [
    path('indexing/pdf/<slug:slug>', views.Pdf.as_view(), name='pdf_view'),
    path('dashboard', views.Dashboard, name='dashboard'),
    # path('update/(?P<pk>\d+)/edit/', views.AccountUpdate.as_view(), name="update"),
    path('profile_update/<int:pk>/', views.AccountUpdateView.as_view(), name="account_update"),
    path('schoolprofile/', views.SchoolProfile.as_view(), name='schoolProfile'),
    path('new_indexing/', views.NewIndexingView.as_view(), name='new_indexing'),
    path('exam_reg/', views.ExamReg.as_view(), name="exam_reg"),
    path('indexed_record/<str:year>', views.IndexListView.as_view(), name='indexed_record'),
    
    path('exam_record/<str:year>'   , views.ExamListView.as_view(), name='exam_record'),
    path('update_indexing/<int:pk>', views.UpdateIndexView.as_view(), name='update_indexing'),
    path('update_exam_record/<int:pk>/', views.UpdateExamView.as_view(), name='update_exam_record'),
    path('delete_record/<int:id>', views.delete_record, name='delete_record'),
    path('submit_all_index', views.submit_index_record, name='submit_all_index'),
    path('submit_all_exam_record', views.submit_exam_record, name='submit_all_exam_record'),

    # Ticket Urls
    # path('ticket', views.Ticket.as_view(), name='ticket'),  
    # path('view_ticket', views.ViewTicket.as_view(), name='ticket'), 
    path('create_ticket', views.CreateTicket.as_view(), name='create_ticket'),
    path('all_ticket', views.ticket_list, name='all_ticket'),
    path('answered_ticket', views.ticket_list, name='answered_ticket'),
    path('closed_ticket', views.ticket_list, name='closed_ticket'),
    path('opened_ticket/', views.ticket_list, name='opened_ticket'),
    path('view_a_ticket/<int:id>', views.view_a_ticket, name='view_a_ticket'),
    path('update_ticket/<int:id>', views.view_a_ticket, name='update_ticket'),
    path('close_ticket/<int:id>', views.view_a_ticket, name='close_ticket'),
    # path('update_ticket/<int:id>', views.update_ticket, name='update_ticket'),

    path('export_indexed_student/xls/', views.export_indexed_stu, name='export_indexed_stu'),
    path('export_approved_student/xls/', views.export_indexed_stu, name='export_approved_student'),
    path('export_current_student/xls/', views.export_indexed_stu, name='export_current_student'),
    path('export_current_exam_record/xls/', views.export_exam_record, name='export_current_exam_record'),
    path('export_submitted_exam_record/xls/', views.export_exam_record, name='export_submitted_exam_record'),
    path('export_approved_exam_record/xls/', views.export_exam_record, name='export_approved_exam_record'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    