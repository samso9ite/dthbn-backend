from cmath import log
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, View
from schPortal.models import *
from schPortal.forms import *
from authentication.forms import *
from authentication.models import Ticket, SubTicket
from cities_light.models import Region, Country
from django.urls import reverse_lazy, reverse
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaulttags import register
from adminPortal.models import *
import xlwt, random, sweetify
from django.template.defaulttags import register
# from adminPortal.render import Render
from django_xhtml2pdf.utils import generate_pdf
from django_xhtml2pdf.views import PdfMixin

# API's import 
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User


class Pdf(View):
    def get(self, request, *args, **kwargs):
        slug=self.kwargs['slug']
        if '/school/indexing/pdf' in request.path:
            record = Indexing.objects.get(institution_id=request.user, id=slug)
        elif '/school/exam/pdf' in request.path:
           record = ExamReg.objects.get(institute_id=request.user, id=slug)
        context_dict = {
            'record': record,
            'request': request
        }
        if '/school/indexing/pdf' in request.path:
            return Render.render('school/indexing_pdf.html', context_dict)
        elif '/school/exam/pdf' in request.path:
            return Render.render('school/exam_pdf.html', context_dict)


class SchoolProfile(CreateAPIView):
    try:
        queryset = School.objects.all()
        serializer_class = schUpdateSerializer
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            user = self.request.user
            # form.instance.User = user
            try:
                user = User.objects.get(id=user.id)
                user.profile_update = True
                user.save()
                return Response({"message": "Profile Updated Successfully"}, status= status.HTTP_200_OK)
            except user.DoesNotExist:
                return Response({"message": "User doesn't exist"}, status= status.HTTP_400_BAD_REQUEST)
            # return super().form_valid(form)
    except Exception as e:
        print(e)
        raise e

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Dashboard(request):
    user = request.user
    school_data = ''
    if user.is_school:
        if user.profile_update:
            school_data = School.objects.get(User=user.id)
            school = {
                'id':user.id,
                'sch_id': school_data.id,
                'sch_name':user.username,
                'sch_address': school_data.address,
                'email': school_data.hod_email,
                'hod_name': school_data.hod_name,
                'sch_phone': school_data.phone_number,
                # 'profile_img': school_data.sch_logo,
                'state': school_data.state,
                'region': school_data.region,
                'hod_phone': school_data.hod_phone,
                'hod_email': school_data.hod_email
            }
            exam_reg_stud = ExamRegistration.objects.filter(institute_id=school_data.id).count()
            total_indexed = Indexing.objects.filter(institution_id=request.user).count()
            current_indexing = Indexing.objects.filter(institution_id=request.user, submitted=False).count()
            current_exam_reg = ExamRegistration.objects.filter(institute_id=school_data.id, submitted=False).count()
            notification = Ticket.objects.filter(Q(ticket_status='Answered') & Q(notification=False)).count()
            context = {
                'school_data': school,
                'exam_reg_stud': exam_reg_stud,
                'total_indexed': total_indexed,
                'notification': notification,
                'current_indexing': current_indexing,
                'current_exam_reg': current_exam_reg
            }
            return Response({"data": context, "message":"Request successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User isn't a school"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "User isn't a school"}, status=status.HTTP_404_NOT_FOUND)

 

class AccountUpdateView(UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = schUpdateSerializer 
    permission_classes = [IsAuthenticated]    

class NewIndexingView(CreateAPIView):
    serializer_class = indexingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.id
        indexing_status = closeIndexing.objects.filter(id=1).first()
        
        # Check if indexing is closed
        if indexing_status and indexing_status.access is False:
            return Response({"message": "Indexing Closed"}, status=status.HTTP_400_BAD_REQUEST)

        # Indexing is open
        school_instance = School.objects.get(User_id=user_id)
        year = self.request.data.get('year')

        indexed = Indexing.objects.filter(institution_id=user_id, year=year).count()
        assigned = IndexLimit.objects.filter(school=school_instance.id, year=year).first()
        # Check if not assigned
        if not assigned:
            return Response({"message": "Contact the board, Limit hasn't been set"}, status=status.HTTP_400_BAD_REQUEST)

        assigned_quota = assigned.assigned_limit

        # Check if limit has been reached
        if indexed != 0 and indexed == assigned_quota:
            return Response({"message": "Limit has been reached"}, status=status.HTTP_400_BAD_REQUEST)

        # Continue with the creation of the object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Index created successfully"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Perform any additional actions before saving the object
        serializer.save(institution=self.request.user)



class ExamRegView(CreateAPIView):
    serializer_class = examSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.id
        exam_status = closeExamRegistration.objects.filter(id=1).first()
        
        # Check if indexing is closed
        if exam_status and exam_status.access is False:
            return Response({"message": "Exam Registeration Closed"}, status=status.HTTP_400_BAD_REQUEST)

        # Indexing is open
        school_instance = School.objects.get(User_id=user_id)
        year = self.request.data.get('year')
        exam_record = ExamRegistration.objects.filter(institute_id=user_id, year=year).count()
        print(school_instance.id)
        assigned_quota =  examLimit.objects.values_list('assigned_limit', flat=True).get(school=school_instance.id, year=year)
        # Check if not assigned
        if not assigned_quota:
            return Response({"message": "Contact the board, Limit hasn't been set"}, status=status.HTTP_400_BAD_REQUEST)

        

        # Check if limit has been reached
        if exam_record != 0 and exam_record == assigned_quota:
            return Response({"message": "Limit has been reached"}, status=status.HTTP_400_BAD_REQUEST)

        # Continue with the creation of the object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Exam Record Created Successfully"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Perform any additional actions before saving the object
        serializer.save(institute=self.request.user)
    
class IndexListView(ListAPIView):
    serializer_class = indexingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'year'

    def get_queryset(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        return Indexing.objects.filter(institution=self.request.user.id, year=lookup_value)

class ExamListView(ListAPIView):
    serializer_class = examSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'year'

    def get_queryset(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        return ExamRegistration.objects.filter(institute=self.request.user.id, year=lookup_value)

class UpdateIndexView(UpdateAPIView):
    serializer_class = indexingSerializer
    queryset = Indexing.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateExamView(UpdateAPIView):
    serializer_class = examSerializer
    queryset = ExamRegistration.objects.all()
    permission_classes = [IsAuthenticated]

class IndexingStatusView(RetrieveAPIView):
    queryset = closeIndexing.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    serializer_class = indexingStatusSerializer

class examRegisterationStatusView(RetrieveAPIView):
    queryset = closeExamRegistration.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    serializer_class = examStatusSerializer


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_index_record(request, id):
    try :
        record = Indexing.objects.get(id=id)  
    except Indexing.DoesNotExist:
       return Response({"message":"Record not found"}, status=status.HTTP_404_NOT_FOUND)
    record.delete()
    return Response({"message":"Index record deleted successfully"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_exam_record(request, id):
    try :
        record = ExamRegistration.objects.get(id=id)  
    except ExamRegistration.DoesNotExist:
       return Response({"message":"Record not found"}, status=status.HTTP_404_NOT_FOUND)
    record.delete()
    return Response({"message":"Exam record deleted successfully"}, status=status.HTTP_200_OK) 
 
@api_view(['PATCH'])
@permission_classes([IsAuthenticated]) 
def submit_index_record(request):
    records = ''
    
    try :
        records = Indexing.objects.filter(submitted=False, institution_id=request.user.id)
        if records :
            records.update(submitted=True) 
            return Response({"message":"Indexed students submitted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"An error occured, please contact admin"}, status=status.HTTP_400_BAD_REQUEST)

    except Indexing.DoesNotExist:
        return Response({"message":"Indexing doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def submit_exam_record(request):
    records = ''
    try :
        records = ExamRegistration.objects.filter(submitted=False, institute_id=request.user.id)
        if records :
            records.update(submitted=True) 
            return Response({"message":"Exam record created"}, status=status.HTTP_200_OK)
        else :
            return Response({"message":"An error occured, please contact admin"}, status=status.HTTP_400_BAD_REQUEST)
            
    except ExamRegistration.DoesNotExist:
        return Response({"message":"Exam Registeration doesn't exist"}, status=status.HTTP_404_NOT_FOUND)


class CreateTicket(CreateView, LoginRequiredMixin):
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy("schoolPortal:all_ticket")
    template_name = "school/ticket.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.ticket_status = 'Open'
        random_num = random.randrange(1000, 10000)
        form.instance.ticket_id = random_num
        form.instance.first_created = True
        sweetify.success(self.request, 'Ticket Created', button='Great!')
        return super().form_valid(form)

@login_required
def ticket_list(request):
    if request.user.is_authenticated and request.user.is_school:
        record = ''
        last_updated_status = []
        last_updated_time = []
        if 'school/all_ticket' in request.path:
            record = Ticket.objects.filter(user_id=request.user.id, first_created=True)
            for last in record:
                last_updated_record = Ticket.objects.filter(ticket_id=last.ticket_id).latest('last_updated')
                last_updated_status.append({last.id:last_updated_record.ticket_status})
                last_updated_time.append({last.id:last_updated_record.last_updated})
              
        elif 'school/answeredticket' in request.path:
            record = Ticket.objects.filter(user_id=request.user.id, ticket_status = 'Answered')

        elif 'school/opened_ticket' in request.path:
            record = Ticket.objects.filter(user_id=request.user.id, ticket_status= 'Open')
           
        elif 'school/closed_ticket' in request.path:
            record = Ticket.objects.filter(user_id=request.user.id, ticket_status= 'Closed')
        else :
            pass

        page = request.GET.get('page', 1)
        paginator = Paginator(record, 5)

        try:
            ticket_list = paginator.page(page)
        
        except PageNotAnInteger:
            ticket_list = paginator.page(1)
        except PageNotAnInteger:
            ticket_list = paginator.page(paginator.num_pages)

        context = {'ticket_list': ticket_list, 'last_updated_status': last_updated_status,
                    'last_updated_time': last_updated_time}
        
        return render(request, 'school/ticket_list.html', context)
    
    else:
        return HttpResponseRedirect(reverse("Auth:Register")) 

@register.filter
def get_item(last_updated_status, key):
    for last_record in last_updated_status or last_record in last_updated_time:
        if key in last_record:
            return last_record.get(key)
        

@login_required
def view_a_ticket(request, id):
    get_record = Ticket.objects.get(id=id)
    record = Ticket.objects.filter(ticket_id=get_record.ticket_id).latest('last_updated')
    all_records = Ticket.objects.filter(ticket_id=get_record.ticket_id).order_by('-id')
    if 'school/update_ticket' in request.path:
        if record.ticket_status != 'Closed':
            form = UpdateTicketForm(request.POST or None)
            if form.is_valid:
                form.save(commit=False)
                form.instance.ticket_id =record.ticket_id
                form.instance.user_id = record.user_id
                form.instance.priority = record.priority
                form.instance.department = record.department
                form.instance.subject = record.department
                form.instance.name = record.name
                form.instance.created_date = record
                form.instance.ticket_status = 'Customer Reply'
                form.save()
                sweetify.success(request, 'Ticket Updated', button='Great!')
                return HttpResponseRedirect(reverse('schPortal:view_ticket', kwargs={'id':id}))
            else:
                sweetify.error(request, 'Form is not valid', button='Great!')
        else:
           sweetify.error(request, 'Ticket has been closed', button='Great!') 
    
    elif 'school/close_ticket' in request.path:
        if record.ticket_status !=  'Closed':
            record.ticket_status = 'Closed'
            record.save()
            sweetify.success(request, 'Ticket Closed', button='Great!')
            return HttpResponseRedirect(reverse('adminPortal:view_ticket', kwargs={'id':id}))
        else:
            sweetify.error(request, "Ticket Status is Closed ")
  
    return render(request, 'school/view_ticket.html', {'record': record, 'all_records': all_records})


@login_required
def export_indexed_stu(request):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Schools')
    row_num = 0
   
    font_style = xlwt.XFStyle()
    font_style.font.bold = True   
    if '/school/export_indexed_student/xls/' or '/school/export_approved_student/xls/' in request.path: 
        response = HttpResponse(content_type='applicaton/mx-excel')
        if '/school/export_indexed_student/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Indexed Record.xls"'
        elif '/school/export_approved_student/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Approved Student Record.xls"'
        
        elif '/school/export_current_student/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Current Student Record.xls"'

        columns = ['First Name', 'Middle Name',  'Surname',  'Cadre', 'Permanent Address', 'Phone Number', 'Email', 
                        'Age', 'State Of Origin', 'Religion', 'Nationality', 'Marital Status', 'School Attended(1)', 'Qualification(1)', 'School Attended(2)', 'Qualification(2)',
                        'School Attended(3)', 'Qualification(3)', 'School Attended(4)', 'Qualification(4)', 'Year of Admission', 
                        'Year of Graduation', 'Contact Address', 'Place of Work', 'Referee Name(1)', 'Referee Address(1)', 'Referee Mobile(1)'
                        'Referee Name(2)', 'Referee Address(2)', 'Referee Mobile(2)',]
            
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet Body, remaining rows
        font_style = xlwt.XFStyle()

        if '/school/export_indexed_student/xls/' in request.path:
        
            rows = Indexing.objects.filter(institution_id=request.user.id, submitted=True).values_list('first_name', 'middle_name', 'surname', 'cadre', 'permanent_address', 'telephone', 'email', 
            'age', 'state', 'religion', 'nationality', 'marital_status', 'school_attended1', 'qualification1', 'school_attended2', 'qualification2',
                'school_attended3', 'qualification3', 'admission_year', 'graduation_year', 'contact_address', 'place_of_work', 
                'referee_name1', 'referee_address1', 'referee_phone1', 'referee_name2', 'referee_address2', 'referee_phone2')

        elif '/school/export_approved_student/xls/' in request.path:
            
            rows = Indexing.objects.filter(institution_id=request.user.id, approved=True).values_list('first_name', 'middle_name', 'surname', 'cadre', 'permanent_address', 'telephone', 'email', 
            'age', 'state', 'religion', 'nationality', 'marital_status', 'school_attended1', 'qualification1', 'school_attended2', 'qualification2',
                'school_attended3', 'qualification3', 'admission_year', 'graduation_year', 'contact_address', 'place_of_work', 
                'referee_name1', 'referee_address1', 'referee_phone1', 'referee_name2', 'referee_address2', 'referee_phone2', )
        
        elif '/school/export_current_student/xls/' in request.path:
            
            rows = Indexing.objects.filter(institution_id=request.user.id, submitted=False).values_list('first_name', 'middle_name', 'surname', 'cadre', 'permanent_address', 'telephone', 'email', 
                'age', 'state', 'religion', 'nationality', 'marital_status', 'school_attended1', 'qualification1', 'school_attended2', 'qualification2',
                'school_attended3', 'qualification3', 'admission_year', 'graduation_year', 'contact_address', 'place_of_work', 
                'referee_name1', 'referee_address1', 'referee_phone1', 'referee_name2', 'referee_address2', 'referee_phone2', )

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def export_exam_record(request):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Schools')
    row_num = 0
   
    font_style = xlwt.XFStyle()
    font_style.font.bold = True   
    if '/school/export_submitted_exam_record/xls/' or '/school/export_current_exam_record/xls/' or '/school/export_approved_exam_record/xls/' in request.path: 
        request.user.id = School.objects.values_list('id', flat=True).get(User_id=request.user.id)
        response = HttpResponse(content_type='applicaton/mx-excel')
        if '/school/export_submitted_exam_record/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Submitted Record for Exam.xls"'
        elif '/school/export_current_exam_record/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Current Exam Record.xls"'
        elif '/school/export_approved_exam_record/xls/' in request.path:
            response['Content-Disposition'] = 'attachment; filename=  "Approved Exam Record.xls"'

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

        if '/school/export_submitted_exam_record/xls/' in request.path:
        
            rows = ExamRegistration.objects.filter(institute_id=request.user.id, submitted=True).values_list('title', 'first_name', 'middle_name', 'surname', 'cadre', 'residential_address', 'telephone', 'email', 
                 'date_of_birth', 'state_of_origin', 'religion', 'marital_status', 'maiden_name', 'senatorial_district', 'qualification1', 'qualification2', 'qualification3', 'qualification4', 'prof_qualification1',
                  'prof_qualification2', 'prof_qualification3', 'prof_qualification4', 'institution_attended1', 'institution_attended2', 'institution_attended3', 'institution_attended4', 'hod_name', 'hod_phone', 'hod_email',
                  'employment_status', 'office_name', 'office_address', 'office_country', 'office_lga', 'office_phone', 'office_email', 'sector', 'present_position', 'department' )
    
        elif '/school/export_current_exam_record/xls/' in request.path:
            
            rows = ExamRegistration.objects.filter(institute_id=request.user.id, submitted=False).values_list('title', 'first_name', 'middle_name', 'surname', 'cadre', 'residential_address', 'telephone', 'email', 
                 'date_of_birth', 'state_of_origin', 'religion', 'marital_status', 'maiden_name', 'senatorial_district', 'qualification1', 'qualification2', 'qualification3', 'qualification4', 'prof_qualification1',
                  'prof_qualification2', 'prof_qualification3', 'prof_qualification4', 'institution_attended1', 'institution_attended2', 'institution_attended3', 'institution_attended4', 'hod_name', 'hod_phone', 'hod_email',
                  'employment_status', 'office_name', 'office_address', 'office_country', 'office_lga', 'office_phone', 'office_email', 'sector', 'present_position', 'department' )

        elif '/school/export_approved_exam_record/xls/' in request.path:
            
            rows = ExamRegistration.objects.filter(institute_id=request.user.id, approved=True).values_list('title', 'first_name', 'middle_name', 'surname', 'cadre', 'residential_address', 'telephone', 'email', 
                 'date_of_birth', 'state_of_origin', 'religion', 'marital_status', 'maiden_name', 'senatorial_district', 'qualification1', 'qualification2', 'qualification3', 'qualification4', 'prof_qualification1',
                  'prof_qualification2', 'prof_qualification3', 'prof_qualification4', 'institution_attended1', 'institution_attended2', 'institution_attended3', 'institution_attended4', 'hod_name', 'hod_phone', 'hod_email',
                  'employment_status', 'office_name', 'office_address', 'office_country', 'office_lga', 'office_phone', 'office_email', 'sector', 'present_position', 'department' )
            
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


