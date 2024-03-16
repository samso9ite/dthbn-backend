from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'adminPortal'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('school_indexed_record', views.school_index, name='school_indexed_record'),
    path('all_schools', views.all_schools, name='all_schools'),
    path('accredited_schools', views.AccreditedSchools.as_view(), name='accredited_schools'),
    path('restriction/<int:id>/<str:restriction_type>', views.restriction, name='block_user'),
    path('delete_user/<int:id>', views.restriction, name='delete_user'),
    path('indexed_list/<str:year>', views.indexed_list, name='indexed_list'),
    path('sch_indexed_rec/<id>/<str:year>/<str:type>', views.sch_indexed_rec, name='sch_indexed_rec'),
    path('sch_exam_rec/<id>/<str:year>/<str:type>', views.sch_exam_rec, name='sch_exam_rec'),
  
    path('reverse_index_submission/<int:id>', views.reverse_index_submission, name='reverse_index'),
    path('reverse_exam_submission/<int:id>', views.reverse_exam_submission, name='reverse_exam'),
    path('approve_index/<int:id>', views.approve_index, name="approve_index"),
    path('approve_exam/<int:id>', views.approve_exam, name="approve_exam"),
    path('decline_indexing/<id>', views.DeclineIndexView.as_view(), name="decline_index"),
    path('decline_exam/<id>', views.DeclineExamView.as_view(), name="decline_exam"),
    path('set_index_limit/<int:id>/<str:year>/<int:limit>', views.ResetLimitView.as_view(), name="index_limit"),
    path('set_exam_limit/<int:id>/<str:year>/<int:limit>', views.ResetExamLimitView.as_view(), name="exam_limit"),
    path('exam', views.Exam.as_view()),
    path('exam_record/<str:year>', views.exam_record, name='exam_record'),
    path('indexing_status/<str:id>', views.getIndexingStatus.as_view(), name="indexing_status"),
    path('exam_status/<str:id>', views.getExamStatus.as_view(), name="exam_status"),

    path('exam_reg_switch/<str:type>', views.close_exam_registeration, name='close_exam'),
    path('close_exam_reg/<int:id>', views.close_selected_exam, name='close_exam_reg'),
    path('close_all_exam_reg/', views.close_exam, name='close_all_exam_reg'),
    path('open_all_exam_reg/', views.close_exam, name='open_all_exam_reg'),

    path('close_index_reg/<int:id>', views.close_selected_index_reg, name='close_index_reg'),
    path('index_reg_switch/<str:type>', views.close_index_registration, name='index_reg_switch'),

    path('reset_notification', views.dashboard, name='reset_notification'),
    path('submit_verified/<int:id>', views.submit_verified, name='submit_verified'),
    path('submit_exam_verified/<int:id>', views.submit_exam_verified, name='submit_exam_verified'),

    #Professional Records
    path('all_professionals', views.professionals, name='professionals'),
    path('delete_professional/<int:id>', views.delete_professional, name='del_professionals'),
    path('update-license/<int:id>', views.UpdateLicense.as_view(), name="update-license"),
    path('add-license', views.AddLicense.as_view(), name="add_license"),
    path('list-license/<int:id>', views.ListLicenseView.as_view(), name="list-license"),

    path('export/xls/', views.export_school, name='export_school_xls'),
    path('export_indexed_student/xls/<int:id>', views.export_indexed_stu, name='export_indexed_student'),
    path('export_exam_record/xls/<int:id>', views.export_indexed_stu, name='export_exam_record'),
    
]
