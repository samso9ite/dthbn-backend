from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from authentication.forms import SignUp, ProfSignUp, LoginForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from authentication.tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from authentication.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from schPortal import urls
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
import sweetify
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def sign_up_view(request):
    serializer = userSerializer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            is_professional = serializer.validated_data['is_professional']
            if is_professional:
                programme = serializer.validated_data['programme']
                codeVar = serializer.validated_data['code']
                code = ''
                if programme == 'Dental Therapist':
                    code = 'RDTH' + codeVar
                    print(code)
                elif programme == 'Dental Nurses':
                    code = 'RDSN' + codeVar
                elif programme == 'Dental Surgery Assistant':
                    code = 'RDSA' + codeVar
                elif programme == 'Dental Surgery Technician':
                    code = 'RDST' + codeVar
                username = code
            current_site = get_current_site(request)
            subject = 'Account Activation Link'
            user = serializer.save(code=code, is_active=False, username=username,)
            print(user)
            message = render_to_string('auth/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return Response({"message": "User created successfully", 'data':serializer.data}, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                # Attempt to get the user by email
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Handle the case where the user does not exist
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Authenticate the user
            user = authenticate(username=user.username, password=password)
            
            if user:
                if user.is_active:
                    if not user.suspend and not user.block:
                        # Login the user
                        login(request, user)
                        refresh = RefreshToken.for_user(user)
                        data = {
                            'refresh' : str(refresh),
                            'access' : str(refresh.access_token)
                        }
                        return Response(data, status=status.HTTP_200_OK)
                    elif user.suspend:
                        return Response({"message": "School Has Been Suspended"}, status=status.HTTP_400_BAD_REQUEST)
                    elif user.block:
                        return Response({"message": "School Has Been Blocked"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "User is not active"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Invalid Username or Password"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def activate(request):
    if request.method == 'POST':
        serializer = accountActivationSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = serializer.validated_data['uidb']
            token = serializer.validated_data['token']
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.reset = True
                if user.is_school:
                    SchoolCode.objects.filter(reg_number=user.code).update(used=True, user_id=user.id)
                    user.save()
                    login(request, user)
                    return Response({"message": "User activated"}, status=status.HTTP_201_CREATED)
                elif user.is_professional:
                    ProfessionalCode.objects.filter(reg_number=user.code).update(used=True, user_id=user.id)
                    user.save()
                    login(request, user)
                    return Response({"message": "User activated"}, status=status.HTTP_201_CREATED)  
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        # Use the logout function to log the user out
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            sweetify.success(request, 'Password Changed Successfully')
                
            if user.is_school:
                return HttpResponseRedirect(reverse("schoolPortal:dashboard"))
            elif user.is_professional:
                return HttpResponseRedirect(reverse("profPortal:dashboard"))
            else:
                return HttpResponseRedirect(reverse("adminPortal:dashboard"))
       
    else:
        form = PasswordChangeForm(request.user)
    if request.user.is_school:
        return render(request, 'school/change_password.html', {"form":form})
    else:
        return render(request, 'adminPortal/change_password.html', {'form':form})

@login_required
def block(request, id):
    try:
        user_instance = User.objects.get(id=id).update(block=True)
    except User.DoesNotExist:
        print("User Does Not Exist")
    return render(request, 'adminPortal/accredited.html')
