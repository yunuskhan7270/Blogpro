from django.shortcuts import render
from .models import Blog_Data, Email_msg
from django.http.response import HttpResponse
def blog_view(request):
    if request.method=="POST":
        data=Email_msg()
        data.name=request.POST['Name']
        data.email=request.POST['Email']
        data.subject=request.POST['Subject']
        data.msg=request.POST['Message']
        data.save()
       # return HttpResponse('''Thanks for message''')
        return render(request, "detail.html", {'data': Email_msg.objects.all()})

    else:
        return render(request,"detail.html",{'data':Blog_Data.objects.all()})


