from os import access
from django.shortcuts import render
from django.views.generic import TemplateView, View
from adminPortal.models import *
from authentication.models import User, Ticket
from schPortal.models import School, Indexing
from adminPortal.views import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from adminPortal.forms import *
from schPortal.forms import UpdateTicketForm
from django.template.defaulttags import register
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.db.models import Q
from profPortal.models import Professional
import sweetify, datetime, xlwt
from adminPortal.render import Render
from django.core.serializers import serialize
from django.template.loader import render_to_string


# API's import 
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import *
from profPortal.serializers import professionalSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from schPortal.serializers import indexingSerializer, examSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User


class Dashboard(TemplateView):
    template_name = 'adminPortal/dashboard.html'
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    all_school = User.objects.filter(is_school=True).order_by('id')
    total_sch_num = User.objects.filter(is_school=True).count()
    total_prof_num = User.objects.filter(is_professional=True).count()
    total_submited_index = Indexing.objects.filter(submitted=True).count() 
    total_exam_reg = ExamRegistration.objects.filter(submitted=True).count()

    serialized_schools = UserSerializer(all_school, many=True).data
 
    context = {
        'all_school':serialized_schools, 
        'total_sch_num':total_sch_num, 
        'total_submited_index':total_submited_index,
        'total_prof_num':total_prof_num,
        'total_exam_reg':total_exam_reg
    }
    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)
    

def school_index(request):
    records = IndexLimit.objects.filter(assigned_limit__gte=0)
  
    return Response({'message': records}, status=status.HTTP_200_OK)

class AccreditedSchools(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_schools(request):
    school_records = User.objects.filter(is_school=True).select_related('user')
    serialized_school_records = UserSerializer(school_records, many=True).data
    accreditedCount = school_records.count()

    context = {'schools':serialized_school_records, 'accreditedCount': accreditedCount}

    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)
   
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professionals(request):
    professional_records = Professional.objects.all()
    serialized_data = professionalSerializer(professional_records, many=True).data
  
    return Response({"data": serialized_data, "message":"Request successful"}, status=status.HTTP_200_OK)
   
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_professional(request, id):
    user_instance = Professional.objects.filter(id=id)
    user_instance.delete()
    return Response({"message": "Account deleted successfully"})

@api_view(['POST'])
def restriction(request, id, restriction_type):
    print(restriction_type)
    try:    
        user_instance = User.objects.get(id=id)
        if restriction_type == 'block':
            user_instance.block = True
            user_instance.save()
            return Response({"message":"User Blockeed Successfully"})

        elif restriction_type == 'unblock':
            user_instance.block = False
            user_instance.save()
            return Response({"message":"User Unblocked Successfully"})

        elif restriction_type == 'suspend':
            user_instance.suspend = True
            user_instance.save()
            return Response({'message':'User Suspended Successfully'})

        elif restriction_type == 'unsuspend':
            user_instance.suspend = False
            user_instance.save()
            return Response({'message':'User Unsuspended Successfully'})
            
        elif restriction_type == 'delete' :
            user_instance.delete()
            return Response({'message':'User Deleted Successfully'})
      
    except User.DoesNotExist:
       return Response({"message": "User Doesn't Exist"})

# Index List Method
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def indexed_list(request, year):
    all_schools = []
    limit = []
    index_year = []
    indexed = School.objects.all()
    access_status = closeIndexing.objects.get(id=1)
   
    for index_record in indexed:
        school_indexed = Indexing.objects.filter(institution_id=index_record.User_id, year=year).count()
        approved_index_count = Indexing.objects.filter(institution=index_record.User_id,  year=year, approved=True).count()
        declined_index_count = Indexing.objects.filter(institution=index_record.User_id,  year=year, unapproved=True).count()
        sch_limit = IndexLimit.objects.filter(school=index_record.id, year=year)

        for sch_indexing_limit in sch_limit:
            limit.append({index_record.id:sch_indexing_limit.assigned_limit})
            index_year.append({index_record.id:sch_indexing_limit.year})
            
            all_schools.append({'id':index_record.id, 'school_id':index_record.User_id, 'school':index_record.User.username, 
                    'index':school_indexed, 'approved':approved_index_count, 
                    'declined':declined_index_count, 
                    'limit':sch_indexing_limit.assigned_limit}
                )
       
        context = {'all_schools':all_schools, 'year':year, 'access_status':access_status.access}
    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)

# @register.filter
# def get_item(limit, index_year, key):
#     for each_limit in limit or index_year:
#         if key in each_limit:
#             return each_limit.get(key)

# @register.filter
# def get_item(all_schools, key):
#     for all_sch in all_schools:
#         if key in all_sch:
#             return all_sch.get(key)

# @register.filter
# def get_item( approved_index, key):
#     for all_approved in  approved_index:
#         if key in all_approved:
#             return all_approved.get(key)

# @register.filter
# def get_item(declined_index, key):
#     for all_declined in declined_index:
#         if key in all_declined:
#             return all_declined.get(key)

# Exam List Method
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exam_record(request, year):
    all_schools = []
    limit = []
    exam_year = []
    exams = School.objects.all()
    access_status = closeExamRegistration.objects.get(id=1)
   
    for exam_record in exams:
        reg_exams = ExamRegistration.objects.filter(institute=exam_record.User_id, year=year).count()
        approved_exam_count = ExamRegistration.objects.filter(institute=exam_record.User_id,  year=year, approved=True).count()
        declined_exam_count = ExamRegistration.objects.filter(institute=exam_record.User_id,  year=year, unapproved=True).count()
        sch_limit = examLimit.objects.filter(school=exam_record.id, year=year)

        for sch_exam_limit in sch_limit:
            limit.append({exam_record.id:sch_exam_limit.assigned_limit})
            exam_year.append({exam_record.id:sch_exam_limit.year})
            
            all_schools.append({'id':exam_record.id, 'school_id':exam_record.User_id, 'school':exam_record.User.username, 
                    'exams':reg_exams, 
                    'approved':approved_exam_count, 
                    'declined':declined_exam_count, 
                    'limit':sch_exam_limit.assigned_limit
                    }
                )
       
        context = {'all_schools':all_schools, 'year':year, 'access_status':access_status.access}
    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sch_exam_rec(request, id, year, type):
    sch_id = id
    record = ''
    declinedCount = ''
    indexedCount = ''
    approvedCount = ''
    if type == 'submitted':
        record = ExamRegistration.objects.filter(institute_id=sch_id, submitted=True, year=year)
        serialized_exam_rec = examSerializer(record, many=True).data
        # indexedCount = record.count()
    elif type == 'approved':
        record = ExamRegistration.objects.filter(institute_id=id, approved=True)
        serialized_exam_rec = examSerializer(record, many=True).data
        # approvedCount = record.count()
    elif type == 'unapproved':
        record = ExamRegistration.objects.filter(institute_id=id, unapproved=True)
        serialized_exam_rec = examSerializer(record, many=True).data
        # declinedCount = record.count()
    else:
        pass

    context = {
        'all_sch_records': serialized_exam_rec, 
        # 'declinedCount':declinedCount,
        # 'indexedCount':indexedCount,
        # 'approvedCount':approvedCount
    }
    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def exam_record(request, year):
#     all_records = []
#     approved_records = []
#     declined_records = []
#     limit = []
#     exam_year = []
#     all_schools = School.objects.all()
#     serialized_school_rec = SchoolSerializer(all_schools, many=True).data
#     exam_status = closeExamRegistration.objects.get(id=1)
#     for each_school in all_schools:
#         total_exam_record = ExamRegistration.objects.filter(institute=each_school.User_id, year=year).count()
#         approved_exam_record = ExamRegistration.objects.filter(institute=each_school.User_id, approved=True, year=year).count()
#         declined_exam_record = ExamRegistration.objects.filter(institute=each_school.User_id, declined=True, year=year).count()
#         all_records.append({each_school.id:total_exam_record})
#         approved_records.append({each_school.id:approved_exam_record})
#         declined_records.append({each_school.id:declined_exam_record})
#         sch_limit = examLimit.objects.filter(school=each_school.id, year=year)
#         for sch_exam_limit in sch_limit:
#             limit.append({each_school.id:sch_exam_limit.assigned_limit})
#             exam_year.append({each_school.id:sch_exam_limit.year})
    
#     context =  {'all_school_record':serialized_school_rec, 'all_records': all_records, 'limit':limit, 'exam_year':exam_year,
#     'approved_records': approved_records, 'declined_records': declined_records, 'year':year, 'exam_status':exam_status.access}
#     return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)

# @register.filter
# def get_item(limit, exam_year, key):
#     for each_limit in limit or exam_year:
#         if key in each_limit:
#             return each_limit.get(key)

# @register.filter
# def get_item(all_records, key):
#     for record in all_records:
#         if key in record:
#             return record.get(key)

# @register.filter
# def get_item(approved_records, key):
#     for record in approved_records:
#         if key in record:
#             return record.get(key)

# @register.filter
# def get_item(declined_records, key):
#     for record in declined_records:
#         if key in record:
#             return record.get(key)

# End of Exam Limit Method

# Indexing Limit Method 
# @api_view(['POST'])
# def create_limit(request, id, year):
#     school_instance = School.objects.get(id=id)
#     form = createLimit(request.POST or None)
    
#     if form.is_valid():
#         form.save(commit=False)
#         form.instance.school = school_instance.id
#         form.instance.year = year
#         form.save()
#         sweetify.success(request, 'Index Limit Assigned', button='Great!')
#         return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#     else:
#         sweetify.error(request, 'Invalid Value', button='Great!')
#         return(HttpResponseRedirect(request.META['HTTP_REFERER']))

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def reset_limit(request, id, year):
#     school_instance = School.objects.get(id=id)
#     sch_data = IndexLimit.objects.filter(school=school_instance.id, year=year).first()
#     if sch_data:
#         form = createLimit(request.POST or None, instance = sch_data) 
#         if form.is_valid():
#             form.save()
#             sweetify.success(request, 'Updated Successfully', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#         else:   
#             sweetify.error(request, 'Invalid Value', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#     else:
#         form = createLimit(request.POST or None)
#         if form.is_valid():
#             form.save(commit=False)
#             form.instance.school = school_instance.id
#             form.instance.year = year
#             form.save()
#             sweetify.success(request, 'Index Limit Assigned', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#         else:
#             sweetify.error(request, 'Invalid Value', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))

class ResetLimitView(UpdateAPIView, CreateAPIView):
    serializer_class = CreateLimitSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        school_instance = School.objects.get(User_id=self.kwargs['id'])
        year = self.kwargs['year']
        obj, created = IndexLimit.objects.get_or_create(school=school_instance.id, year=year)
        return obj
    
    def perform_create(self, serializer):
        school_instance = School.objects.get(id=self.kwargs['id'])
        serializer.save(school=school_instance.id, year=self.kwargs['year'], assigned_limit=self.kwargs['limit'])

    def get_success_message(self, created):
        return "Index Limit Assigned" if created else "Limit Updated Successfully"
    
    def perform_update(self, serializer):
        serializer.save(assigned_limit=self.kwargs['limit']) 

    def post(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        headers = self.get_success_headers(serializer.data)
        response_data = {'message':self.get_success_message(partial)}
        return Response(response_data, status=200, headers=headers)

# Exam Limit Method
# @login_required
# def create_exam_limit(request, id, year):
#     school_instance = School.objects.get(id=id)
#     form = setExamLimit(request.POST or None)
#     if form.is_valid():
#         form.save(commit=False)
#         form.instance.school = school_instance.id
#         form.instance.year = year
#         form.save()
#         sweetify.success(request, 'Exam Limit Assigned', button='Great!')
#         return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#     else:
#         sweetify.error(request, 'Invalid Value', button='Great!')
#         return(HttpResponseRedirect(request.META['HTTP_REFERER']))

# @login_required
# def reset_exam_limit(request, id, year):
#     school_instance = School.objects.get(id=id)
#     sch_data = examLimit.objects.filter(school=school_instance.id, year=year).first()
#     if sch_data:
#         form = setExamLimit(request.POST or None, instance = sch_data) 
#         if form.is_valid():
#             form.save()
#             sweetify.success(request, 'Limit Updated Successfully', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#         else:
#             sweetify.error(request, 'Invalid Value', button='Error!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#     else:
#         form = setExamLimit(request.POST or None)
#         if form.is_valid():
#             form.save(commit=False)
#             form.instance.school = school_instance.id
#             form.instance.year = year
#             form.save()
#             sweetify.success(request, 'Exam Limit Assigned', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))
#         else:
#             sweetify.error(request, 'Invalid Value', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))


class ResetExamLimitView(UpdateAPIView, CreateAPIView):
    serializer_class = CreateExamLimitSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        school_instance = School.objects.get(User_id=self.kwargs['id'])
        year = self.kwargs['year']
        obj, created = examLimit.objects.get_or_create(school=school_instance.id, year=year)
        return obj
    
    def perform_create(self, serializer):
        school_instance = School.objects.get(id=self.kwargs['id'])
        serializer.save(school=school_instance.id, year=self.kwargs['year'], assigned_limit=self.kwargs['limit'])
    
    def perform_update(self, serializer):
        serializer.save(assigned_limit=self.kwargs['limit']) 

    def get_success_message(self, created):
        return "Exam Limit Assigned" if created else "Limit Updated Successfully"
    
    def post(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        headers = self.get_success_headers(serializer.data)
        response_data = {'message':self.get_success_message(partial)}
        return Response(response_data, status=200, headers=headers)
    

@api_view(['PATCH'])
def reverse_index_submission(request, id):
    try:
        school_instance = Indexing.objects.filter(institution_id=id, submitted=True)
        print(school_instance)
        if school_instance:
            school_instance.update(submitted=False, approved=False, unapproved=False)
            return Response({"message":"Submission Reversed Successfully"})
        else:
            return Response({"message":"Indexing hasn't been submitted"}, status=status.HTTP_400_BAD_REQUEST)
    except Indexing.DoesNotExist:
        return Response({"message":"Record Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def reverse_exam_submission(request, id):
    try:
        school_instance = ExamRegistration.objects.filter(institute_id=id, submitted=True)
        if school_instance:
            school_instance.update(submitted=False, approved=False, unapproved=False)
            return Response({"message":"Submission Reversed Successfully"})
        else:
            return Response({"message":"Exam record hasn't been submitted"}, status=status.HTTP_400_BAD_REQUEST)
       
    except Indexing.DoesNotExist:
        return Response({"message":"Record Not Found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_index(request, id):
    record = Indexing.objects.get(id=id, submitted=True)
    record.approved = True
    record.unapproved = False
    record.comment = ''
    
    record.save()
    return Response({"message":"Student Approved"}, status=status.HTTP_200_OK)

class DeclineIndexView(UpdateAPIView):
    queryset = Indexing.objects.all()
    serializer_class = declineIndexSerializer 
    permission_classes = [IsAuthenticated]  
    lookup_field = 'id'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sch_indexed_rec(request, id, year, type):
    sch_id = id
    record = ''
    declinedCount = ''
    indexedCount = ''
    approvedCount = ''
    if type == 'submitted':
        record = Indexing.objects.filter(institution_id=sch_id, submitted=True, year=year)
        serialized_index_rec = indexingSerializer(record, many=True).data
        indexedCount = record.count()
    elif type == 'approved':
        record = Indexing.objects.filter(institution_id=id, approved=True)
        serialized_index_rec = indexingSerializer(record, many=True).data
        approvedCount = record.count()
    elif type == 'unapproved':
        record = Indexing.objects.filter(institution_id=id, unapproved=True)
        serialized_index_rec = indexingSerializer(record, many=True).data
        declinedCount = record.count()
    else:
        pass

    context = {
        'all_sch_records': serialized_index_rec, 'declinedCount':declinedCount,
        'indexedCount':indexedCount, 'approvedCount':approvedCount
    }
    return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)

class Exam(TemplateView):
    template_name = 'adminPortal/Examination_dept.html'

class getIndexingStatus(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = closeIndexing.objects.all()
    serializer_class =  indexStatusSerializer
    lookup_field = 'id'

class getExamStatus(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = closeExamRegistration.objects.all()
    serializer_class =  examStatusSerializer
    lookup_field = 'id'



# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def exam_verification(request, id):
#     if 'admin/approve_student/' in request.path:
#         record = ExamRegistration.objects.get(id=id, submitted=True)
#         record.approved = True
#         record.declined = False
#         record.comment = ''
#         record.save()
#         sweetify.success(request, 'Approved Successfully', button='Great!')
#         return(HttpResponseRedirect(request.META['HTTP_REFERER']))
    
#     elif 'admin/decline_student/' in request.path:
#         record = ExamRegistration.objects.get(id=id, submitted=True)
#         form = UpdateExamStatus(request.POST, instance=record)
#         if form.is_valid():
#             form.save()
#             sweetify.error(request, 'Declined Successfully', button='Great!')
#             return(HttpResponseRedirect(request.META['HTTP_REFERER']))

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_exam(request, id):
    record = ExamRegistration.objects.get(id=id, submitted=True)
    record.approved = True
    record.declined = False
    record.comment = ''
    
    record.save()
    return Response({"message":"Exam Record Approved"}, status=status.HTTP_200_OK)

class DeclineExamView(UpdateAPIView):
    queryset = ExamRegistration.objects.all()
    serializer_class = declineExamSerializer 
    permission_classes = [IsAuthenticated]  
    lookup_field = 'id'

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def decline_exam(request, id):
#     record = ExamRegistration.objects.get(id=id, submitted=True)
#     record.approved = False
#     record.declined = True
#     record.comment = ''
    
#     record.save()
#     return Response({"message":"Exam Registeration Declined"}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def exam_rec(request, id, year, type):
#     declinedCount = ''
#     indexedCount = ''
#     approvedCount = ''
    
#     sch_id = id
#     if type == 'submitted':
#         record = ExamRegistration.objects.filter(institute_id=id, submitted=True, year=year)
#         indexedCount = record.count()

#     elif type == 'approved':
#         record = ExamRegistration.objects.filter(institute_id=id, approved=True, year=year)
#         approvedCount = record.count()

#     elif type == 'declined':
#         record = ExamRegistration.objects.filter(institute_id=id, declined=True, year=year)
#         declinedCount = record.count()
       

#     sch_name = School.objects.get(User_id=id)
    
    # page = request.GET.get('page', 1)
    # paginator = Paginator(record, 10)

    # try:
    #     all_exam_records = paginator.page(page)
    # except PageNotAnInteger:
    #     all_exam_records = paginator.page(1)
    # except EmptyPage:
    #     all_exam_records = paginator.page(paginator.num_pages)
    
    # context = {'all_exam_records': record, 'sch_name':sch_name, 'sch_id': sch_id,
    #             'declinedCount':declinedCount, 'indexedCount':indexedCount, 'approvedCount':approvedCount 
    #         }
        
    # return Response({"data":context, "message":"Record Fetched"}, status=status.HTTP_200_OK)



# @login_required
# def ticket_list(request):
#     if request.user.is_authenticated:
#         schools = []
#         # if 'admin/all_ticket' in request.path:
#         all_schools = User.objects.filter(is_school=True)
#         all_schools_count = Ticket.objects.filter(first_created=True).count()
#         for sch in all_schools:
#             if 'admin/all_ticket' in request.path:
#                 sch_replies = Ticket.objects.filter(user_id=sch.id, ticket_status='School Reply', read=False).count()
#                 open_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Open', read=False).count()
#                 closed_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Closed').count()
#                 answered_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Answered').count()
            
#             elif 'admin/all_indexing_ticket' in request.path:
#                 sch_replies = Ticket.objects.filter(user_id=sch.id, ticket_status='School Reply', read=False, department='Indexing').count()
#                 open_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Open', read=False, department='Indexing').count()
#                 closed_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Closed', department='Indexing').count()
#                 answered_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Answered', department='Indexing').count()
#             elif 'admin/all_examination_ticket' in request.path:
#                 sch_replies = Ticket.objects.filter(user_id=sch.id, ticket_status='School Reply', read=False, department='examination').count()
#                 open_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Open', read=False, department='examination').count()
#                 closed_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Closed', department='examination').count()
#                 answered_ticket = Ticket.objects.filter(user_id=sch.id, ticket_status='Answered', department='examination').count()
            
#             if sch_replies or open_ticket or answered_ticket:
#                 schools.append({'sch_replies':sch_replies, 'sch_details': sch, 'open_ticket': open_ticket, 
#                 'closed_ticket': closed_ticket, 'answered_ticket': answered_ticket})
                
#         context = {'sch_replies': sch_replies, 'schools': schools,  'closed_ticket': closed_ticket, 'answered_ticket':answered_ticket,
#                     'open_ticket': open_ticket}
            
#         return render(request, 'adminPortal/ticket_list.html', context)
#     # else:
#     #     return HttpResponseRedirect(reverse("Auth:Register")) 
        
# @login_required
# def sch_ticket_list(request, id):
#     if request.user.is_authenticated:
        
#         if 'admin/sch_reply_list/' in request.path:
#             query = Ticket.objects.filter(user_id = id, ticket_status='School Reply')
#             query.update(read=True)
#         elif 'admin/answered_ticket_list' in request.path:
#             query = Ticket.objects.filter(user_id=id, ticket_status='Answered')
#             query.update(read=True)
#         elif 'admin/opened_ticket_list' in request.path:
#             query = Ticket.objects.filter(user_id= id, ticket_status='Open')
#             query.update(read=True)
#         elif 'admin/closed_ticket_list' in request.path:
#             query = Ticket.objects.filter(user_id=  id, ticket_status='Closed')

#         elif 'admin/sch_reply_index_list/' in request.path:
#             query = Ticket.objects.filter(user_id = id, ticket_status='School Reply', department='Indexing')
#             query.update(read=True)
#         elif 'admin/answered_ticket_index_list' in request.path:
#             query = Ticket.objects.filter(user_id=id, ticket_status='Answered', department='Indexing')
#             query.update(read=True)
#         elif 'admin/opened_ticket_index_list' in request.path:
#             query = Ticket.objects.filter(user_id= id, ticket_status='Open', department='Indexing')
#             query.update(read=True)
#         elif 'admin/closed_ticket_index_list' in request.path:
#             query = Ticket.objects.filter(user_id=  id, ticket_status='Closed', department='Indexing')

#         elif 'admin/sch_reply_exam_list/' in request.path:
#             query = Ticket.objects.filter(user_id = id, ticket_status='School Reply', department='Examination')
#             query.update(read=True)
#         elif 'admin/answered_ticket_exam_list' in request.path:
#             query = Ticket.objects.filter(user_id=id, ticket_status='Answered', department='Examination')
#             query.update(read=True)
#         elif 'admin/opened_ticket_exam_list' in request.path:
#             query = Ticket.objects.filter(user_id= id, ticket_status='Open', department='Examination')
#             query.update(read=True)
#         elif 'admin/closed_ticket_exam_list' in request.path:
#             query = Ticket.objects.filter(user_id=  id, ticket_status='Closed', department='Examination')
        
       
#         page = request.GET.get('page', 1)
#         paginator = Paginator(query, 10000)

#         try:
#             query_list = paginator.page(page)
#         except PageNotAnInteger:
#             query_list = paginator.page(1)
#         except EmptyPage:
#             query_list = paginator.page(paginator.num_pages)

#         return render(request, 'adminPortal/sch_ticket_list.html', {'query_list':query_list})

# @login_required
# def view_a_ticket(request, id):
#     record = Ticket.objects.get(id=id)

#     latest_record = Ticket.objects.filter(ticket_id=record.ticket_id).latest('last_updated')
#     all_records = Ticket.objects.filter(ticket_id=record.ticket_id).order_by('-id')
 
#     if 'admin/update_ticket' in request.path:
#         if latest_record.ticket_status != 'Closed':
#             form = UpdateTicketForm(request.POST or None)
#             if form.is_valid:
#                 form.save(commit=False)
#                 form.instance.ticket_id =record.ticket_id
#                 form.instance.user_id = record.user_id
#                 form.instance.priority = record.priority
#                 form.instance.department = record.department
#                 form.instance.subject = record.department
#                 form.instance.name = record.name
#                 form.instance.created_date = record
#                 form.instance.ticket_status = 'Answered'
#                 form.save()
#                 sweetify.success(request, 'Ticket Updated', button='Great!')
#                 return HttpResponseRedirect(reverse('adminPortal:view_ticket', kwargs={'id':id}))
#             else:
#                 sweetify.error(request, 'Form is not valid', button='Great!')
#         else:
#            sweetify.error(request, 'Ticket has been closed', button='Great!') 
    
#     elif 'admin/close_ticket' in request.path:
#         if latest_record.ticket_status !=  'Closed':
#             all_answered = Ticket.objects.filter(ticket_status='Answered', ticket_id=record.ticket_id).update(closed=True)
#             latest_record.ticket_status = 'Closed'
#             latest_record.save()
#             sweetify.success(request, 'Ticket Closed', button='Great!')
#             return HttpResponseRedirect(reverse('adminPortal:view_ticket', kwargs={'id':id}))
#         else:
#             sweetify.error(request, "Ticket Status is Closed ")
        
        
#     return render(request, 'adminPortal/view_ticket.html', {'all_records': all_records, 'record': record, 'latest_record': latest_record
#     }) 
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def submit_verified(request, id):
    user_instance = Indexing.objects.filter(Q(approved=True)|Q(unapproved=True), Q(verified=False), Q(institution_id=id))
    
    if user_instance:
        user_instance.update(verified=True)
        # sweetify.success(request, 'Verified Index Submitted', button='Great!')
        # return HttpResponseRedirect(reverse('adminPortal:sch_indexed_rec', kwargs={'id':id}))
        return Response({"message":"Index Record Verified"}, status=status.HTTP_200_OK)
    else:
        # sweetify.error(request, 'Verified Index Already Submitted', button='Great!')
        return Response({"message":"Verified Index Already Submitted"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def submit_exam_verified(request, id):
    user_instance = ExamRegistration.objects.filter(Q(approved=True)|Q(declined=True), Q(verified=False), Q(institute_id=id))
    
    if user_instance:
        user_instance.update(verified=True)
        # sweetify.success(request, 'Verified Record Submitted', button='Great!')
        return Response({"message":"Exam Record Verified"}, status=status.HTTP_200_OK)
    else: 
        # sweetify.error(request, 'Verified Record Already Submitted', button='Great!')
        return Response({"message":"Verified Record Already Submitted"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def close_exam(request):
    exam_instance = closeExamRegistration.objects.update(access=True, date=datetime.datetime.now())
    for obj in exam_instance:
        if obj.access is False:
            exam_instance
            return Response({"message":"Indexing Closed"}, status=status.HTTP_200_OK)
        else:
            exam_instance.update(access=False, date=datetime.datetime.now())
        return Response({"message":"An error occured"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def close_index_registration(request, type):
    if type == 'close' :
        closeIndexing.objects.update(access=False) 
        return Response({"message":"Indexing Closed"}, status=status.HTTP_200_OK)
    elif type == 'open':
        School.objects.update(close_index_reg=True, closed_index_date=datetime.datetime.now())
        closeIndexing.objects.update(access=True) 
        return Response({"message":"Indexing Opened"}, status=status.HTTP_200_OK)
      
@login_required
def close_selected_index_reg(request, id, type):
    index_instance = School.objects.filter(id=id)
    for obj in index_instance:
        if type == 'close':
            index_instance.update(close_index_reg=True, closed_exam_date=datetime.datetime.now())
            return Response({"message":"Indexing Closed"}, status=status.HTTP_200_OK)
        elif type == open:
            index_instance.update(close_index_reg=False, closed_exam_date=datetime.datetime.now())
            return Response({"message":"Indexing Opened"}, status=status.HTTP_200_OK)
        
        return Response({"message":"An error occured"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def close_exam_registeration(request, type):
    if type == 'close' :
        School.objects.update(close_exam_reg=False, closed_exam_date=datetime.datetime.now())
        closeExamRegistration.objects.update(access=False) 
        return Response({"message":"Exam Registeration Closed"}, status=status.HTTP_200_OK)
    elif type == 'open':
        School.objects.update(close_exam_reg=True, closed_exam_date=datetime.datetime.now())
        closeExamRegistration.objects.update(access=True)
        return Response({"message":"Exam Registeration Opened"}, status=status.HTTP_200_OK)
   
@login_required
def close_selected_exam(request, id, type):    
    exam_instance = School.objects.filter(id=id)
    for obj in exam_instance:
        if type == 'close':
            exam_instance.update(close_exam_reg=True, closed_exam_date=datetime.datetime.now())
            return Response({"message":"Exam Registeration Closed"}, status=status.HTTP_200_OK)
            # sweetify.success(request, 'Indexing Closed', button='Great!')

        elif type == 'open':
            exam_instance.update(close_exam_reg=False, closed_exam_date=datetime.datetime.now())
            return Response({"message":"Exam Registeration Opened"}, status=status.HTTP_200_OK)
        
        return Response({"message":"An error occured"}, status=status.HTTP_400_BAD_REQUEST)

# @login_required
# def search_status(request):
#     if request.method == "GET":
#         search_text = request.GET.get('search_text', None)
#     else:
#         search_text = ''
#     accredited_schools_record = User.objects.filter(is_school=True, username__icontains='sam').select_related('user')
#     return render(request, 'adminPortal/accredited.html', {'accredited_schools_record':accredited_schools_record})

# def ajax(request):
#     if request.method == "GET":
#         search_text = request.GET.get('search_text', None)
#     else:
#         search_text = ''
#     accredited_schools_record = serialize('json', User.objects.filter(is_school=True, username__icontains=search_text).select_related('user'))
#     return JsonResponse(accredited_schools_record, safe=False)
    
@login_required
def export_school(request):
    response = HttpResponse(content_type='applicaton/mx-excel')
    response['Content-Disposition'] = 'attachment; filename="Accredited Schools.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Schools')
    # Sheet Header, First Row  
    row_num = 0
   
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['School Name', 'Registration Number', 'Programme', 'School Address', 'Phone Number', 'Email', 
                    'State', 'Postal Address', 'HOD\'s Name', 'HOD\'s Number', 'HOD\'s Email',]
        
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet Body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.filter(is_school=True).values_list('username', 'code', 'programme', 'user__address', 'phone_number', 'email', 'user__region', 
    'user__postal_number', 'user__hod_name', 'user__hod_phone', 'user__hod_email')
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
  

    wb.save(response)
    return response



def export_indexed_stu(request, id):
   

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Schools')

    # Sheet Header, First Row
    row_num = 0
   
    font_style = xlwt.XFStyle()
    font_style.font.bold = True   
    if '/admin/export_indexed_student/xls/' in request.path: 
        sch_name = User.objects.values_list('username', flat=True).get(id=id)  
        response = HttpResponse(content_type='applicaton/mx-excel')
        response['Content-Disposition'] = 'attachment; filename=  "{} Indexing Record.xls"'.format(sch_name)
        columns = ['First Name', 'Middle Name',  'Surname',  'Cadre', 'Permanent Address', 'Phone Number', 'Email', 
                        'Age', 'State Of Origin', 'Religion', 'Nationality', 'Marital Status', 'School Attended(1)', 'Qualification(1)', 'School Attended(2)', 'Qualification(2)',
                        'School Attended(3)', 'Qualification(3)', 'School Attended(4)', 'Qualification(4)', 'Year of Admission', 
                        'Year of Graduation', 'Contact Address', 'Place of Work', 'Referee Name(1)', 'Referee Address(1)', 'Referee Mobile(1)'
                        'Referee Name(2)', 'Referee Address(2)', 'Referee Mobile(2)',]
            
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet Body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Indexing.objects.filter(institution_id=id, submitted=True).values_list('first_name', 'middle_name', 'surname', 'cadre', 'permanent_address', 'telephone', 'email', 
        'age', 'state', 'religion', 'nationality', 'marital_status', 'school_attended1', 'qualification1', 'school_attended2', 'qualification2',
            'school_attended3', 'qualification3', 'admission_year', 'graduation_year', 'contact_address', 'place_of_work', 
            'referee_name1', 'referee_address1', 'referee_phone1', 'referee_name2', 'referee_address2', 'referee_phone2')

    elif '/admin/export_exam_record/' in request.path:
        sch_id = School.objects.values_list('User_id', flat=True).get(id=id)
        sch_name = User.objects.values_list('username', flat=True).get(id=sch_id)


        response = HttpResponse(content_type='applicaton/mx-excel')
        response['Content-Disposition'] = 'attachment; filename=  "{} Exam Record.xls"'.format(sch_name)
        columns = ['Title', 'First Name', 'Middle Name',  'Surname',  'Cadre', 'Address', 'Phone Number', 'Email', 
                    'Date of Birth', 'State of Origin', 'Religion', 'Marital Status', 'Maiden Name', 'Senatorial District', 'Qualification(1)', 'qualification(2)', 'qualification(3)', 'qualification(4)',
                    'Professional Qualification', 'Professional Qualification(2)', 'Professional Qualification(3)', 'Professional Qualification(4)', 'Institution Attended(1)', 'Institution Attended(2)', 'Institution Attended(3)', 'Institution Attended(4)', 'Hod\'s Name', 'Hod\s Phone', 
                    'Hod\s Email','Employment Status', 'Office Name', 'Office Country', 'Office LGA', 
                    'Office Phone Number', 'Office Email', 'Sector', 'Present Position', 'Department', 
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet Body, remaining rows
        font_style = xlwt.XFStyle()
        # sch_id = School.objects.get(id=id)
        sch_id = School.objects.values_list('id', flat=True).get(id=id)
        rows = ExamRegistration.objects.filter(institute_id=sch_id, submitted=True).values_list('title', 'first_name', 'middle_name', 'surname', 'cadre', 'residential_address', 'telephone', 'email', 
                 'date_of_birth', 'state_of_origin', 'religion', 'marital_status', 'maiden_name', 'senatorial_district', 'qualification1', 'qualification2', 'qualification3', 'qualification4', 'prof_qualification1',
                  'prof_qualification2', 'prof_qualification3', 'prof_qualification4', 'institution_attended1', 'institution_attended2', 'institution_attended3', 'institution_attended4', 'hod_name', 'hod_phone', 'hod_email',
                  'employment_status', 'office_name', 'office_address', 'office_country', 'office_lga', 'office_phone', 'office_email', 'sector', 'present_position', 'department' )
    
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
