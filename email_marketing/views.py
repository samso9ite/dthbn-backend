from django.shortcuts import render
from email_marketing import urls
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from email_marketing.forms import * 

# Create your views here.
def push_emails(request):
    if 'mailMarketing/push_mail'in request.path:
        html_content = render_to_string("email_marketing/email_content.html")
        email = EmailMessage("Great deals on all engineering equipments", html_content, "info@caravellesystems.com", ['samso9ite@gmail.com','richiebaker45@gmail.com','carycastle@btconnect.com','thor@nolta.com','jo@joward.co.uk','paul.degroot@tradition.co.uk','rob@brilliantpromotions.co.uk','yvonneandbrent@singnet.com.sg','kate.davidge@tradition.com','g.fuller@mac.com','osegal@optusnet.com.au','marskonfx@gmail.com','etxcapital@bluegemsolutions.com','tom.fawcett@igindex.co.uk','greg@tradeandtested.com','j-i-white@tiscali.co.uk','iftikhar_9@msn.com','suzannajwoods@hotmail.com','dimpy.pathak@virgin.net','helltojamesmyers@msn.com','christian.maggio@live.com','roger.b@newforestengineering.co.uk','craig.fookes@stirling-house.com','deepak.kotecha@rbs.co.uk','callumcampbell@highlandtreasury.com','simon@masterpolicy.co.uk','mat@mbfmanagement.co.uk','danith@bigpond.net.au','danie@lepaarl.com','amelia@ashelley.freeserve.co.uk','enquiries@holidayhomes4u.com','gahmet@sky.com','timothyhead@virginmedia.com','hira@physics.org','er@rightonproperty.co.uk','info@3dcanvas.co.uk','mail@texttheword.co.uk','behenneberry@gmail.com','andrew.rowe@icap.com','bbiyani@orcim.com','temp.3@ntlworld.com','govind.rudrawar@hotmail.co.uk','hodka@fastmail.fm','aparlour@msn.com'])
        email.content_subtype = "html"
        res = email.send()
        return HttpResponse("Sent Successfully")

#def send_email(request):
   # if request.method == "POST":
        #return HttpResponse("Post request")
       # print("Request is post")
        #form = emails(request.POST)
       # if form.is_valid():
        #     print ("Form is valid")
         #    html_content = render_to_string("email_marketing/email_content.html")
          #   email = EmailMessage("Great deals on all engineering equipments", html_content, "info@caravellesystems.com", [form.all_emails])
           #  email.content_subtype = "html"
            # res = email.send()
            # return HttpResponse("Sent Successfully")
   # return render(request, "email_marketing/send.html")
    #else:
     #   return HttpResponse("Input emails Correctly")

#class send_emailTemplateView):
    

def send_email(request):
    if request.method == "POST":
        #return HttpResponse("Post request")
        print("Request is post")
        form = emails(request.POST)
        #print(form.all_emails)
        if form.is_valid():
             mass_emails = form.cleaned_data['all_emails']
             print(mass_emails)
             html_content = render_to_string("email_marketing/email_content.html")
             email = EmailMessage("Great deals on all engineering equipments", html_content, "info@caravellesystems.com", [mass_emails])
             email.content_subtype = "html"
             res = email.send()
             return HttpResponse("Sent Successfully")
    return HttpResponse("Email Sent Successfully")
    #else:
     #   return HttpResponse("Input emails Correctly")
