from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'adminPortal'
urlpatterns = [
    path('ajaxSearch/', views.search_status, name='ajaxSearch'),
    path('ajax/', views.ajax, name='ajax'),
    path('hboard', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('indexing', views.AccreditedSchools.as_view(), name='indexing'),
    path('school_indexed_record', views.school_index, name='school_indexed_record'),
    path('accredited_schools', views.accredited_schools, name='accredited_schools'),
    path('block_user/<int:id>', views.restriction, name='block_user'),
    path('unblock_user/<int:id>', views.restriction, name='unblock_user'),
    path('suspend_user/<int:id>', views.restriction, name='suspend_user'),
    path('unsuspend_user/<int:id>', views.restriction, name='unsuspend_user'),
    path('delete_user/<int:id>', views.restriction, name='delete_user'),
    path('indexed_list/<str:year>', views.indexed_list, name='indexed_list'),
    path('sch_indexed_rec/<id>/<str:year>', views.sch_indexed_rec, name='sch_indexed_rec'),
    path('approved_indexed_list/<int:id>/<str:year>', views.sch_indexed_rec, name='approved_indexed_list'),
    path('declined_indexed_list/<int:id>/<str:year>', views.sch_indexed_rec, name='declined_indexed_list'),
    path('approve_index/<int:id>', views.verification, name='approve_index'),
    path('decline_index/<int:id>', views.verification, name='decline_index'),
    path('set_limit/<int:id>/<str:year>', views.reset_limit, name='set_limit'),
    path('create_index_limit/<int:id>/<str:year>', views.create_limit, name='create_index_limit'),
    path('exam', views.Exam.as_view()),
    path('exam_record/<str:year>', views.exam_record, name='exam_record'),
    path('sch_exam_rec/<int:id>/<str:year>', views.exam_rec, name='sch_exam_rec'),
    path('approved_exam_rec/<int:id>/<str:year>', views.exam_rec, name='approved_exam_rec'),
    path('declined_exam_rec/<int:id>/<str:year>', views.exam_rec, name='declined_exam_rec'),
    path('approve_student/<int:id>', views.exam_verification, name='approve_student'),
    path('decline_student/<int:id>', views.exam_verification, name='decline_student'),
    path('exam_limit/<int:id>/<str:year>', views.reset_exam_limit, name='exam_limit'),
    path('create_exam_limit/<int:id>/<str:year>', views.create_exam_limit, name='create_exam_limit'),
    path('reverse_index_record/<int:id>', views.reverse_submission, name='reverse_index_record'),
    path('reverse_exam_record/<int:id>', views.reverse_submission, name='reverse_exam_record'),
    # path('close/', views.close_indexing, name='closeIndexing'),
    path('close_exam/', views.close_exam, name='close_exam'),
    path('close_exam_reg/<int:id>', views.close_selected_exam, name='close_exam_reg'),
    path('close_all_exam_reg/', views.close_exam, name='close_all_exam_reg'),
    path('open_all_exam_reg/', views.close_exam, name='open_all_exam_reg'),

    path('close_index_reg/<int:id>', views.close_selected_index_reg, name='close_index_reg'),
    path('close_all_index_reg/', views.close_index_registration, name='close_all_index_reg'),
    path('open_all_index_reg/', views.close_index_registration, name='open_all_index_reg'),
    # path('open_exam_reg/<int:id>', views.open_selected_exam, name='open_exam_reg'),
    
    # Ticket Urls
    path('all_ticket', views.ticket_list, name='all_ticket'),
    path('all_indexing_ticket', views.ticket_list, name='all_indexing_ticket'),
    path('all_examination_ticket', views.ticket_list, name='all_examination_ticket'),
    path('answered_ticket', views.ticket_list, name='answered_ticket'),
    path('closed_ticket', views.ticket_list, name='closed_ticket'),
    path('opened_ticket/', views.ticket_list, name='opened_ticket'),

    # Admin Tickets
    path('sch_reply_list/<int:id>', views.sch_ticket_list, name='sch_reply_list'),
    path('answered_ticket_list/<int:id>', views.sch_ticket_list, name='answered_ticket_list'),
    path('closed_ticket_list/<int:id>', views.sch_ticket_list, name='closed_ticket_list'),
    path('opened_ticket_list/<int:id>', views.sch_ticket_list, name='opened_ticket_list'),
    path('sch_reply_index_list/<int:id>', views.sch_ticket_list, name='sch_reply_index_list'),
    path('answered_ticket_index_list/<int:id>', views.sch_ticket_list, name='answered_ticket_index_list'),
    path('opened_ticket_index_list/<int:id>', views.sch_ticket_list, name='opened_ticket_index_list'),
    path('closed_ticket_index_list/<int:id>', views.sch_ticket_list, name='closed_ticket_index_list'),

    path('sch_reply_exam_list/<int:id>', views.sch_ticket_list, name='sch_reply_exam_list'),
    path('answered_ticket_exam_list/<int:id>', views.sch_ticket_list, name='answered_ticket_exam_list'),
    path('opened_ticket_exam_list/<int:id>', views.sch_ticket_list, name='opened_ticket_exam_list'),
    path('closed_ticket_exam_list/<int:id>', views.sch_ticket_list, name='closed_ticket_exam_list'),

    path('update_ticket/<int:id>', views.view_a_ticket, name='update_ticket'),
    path('view_ticket/<int:id>', views.view_a_ticket, name='view_ticket'),
    path('close_ticket/<int:id>', views.view_a_ticket, name='close_ticket'),
    path('reset_notification', views.dashboard, name='reset_notification'),
    path('submit_verified/<int:id>', views.submit_verified, name='submit_verified'),
    path('submit_exam_verified/<int:id>', views.submit_exam_verified, name='submit_exam_verified'),

    #Professional Records
    path('professionals/', views.professionals, name='professionals'),
    path('delete_professional/<int:id>', views.delete_professional, name='del_professionals'),

    path('export/xls/', views.export_school, name='export_school_xls'),
    path('export_indexed_student/xls/<int:id>', views.export_indexed_stu, name='export_indexed_student'),
    path('export_exam_record/xls/<int:id>', views.export_indexed_stu, name='export_exam_record'),
    
]
