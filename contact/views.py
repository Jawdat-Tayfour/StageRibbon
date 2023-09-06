from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
def contact_view(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            content = form.cleaned_data["content"]

            html = render_to_string('contactform.html',
                                    {'name':name,
                                     'email':email,
                                     'content':content})
            send_mail(
                'Message from StageRibbon,',
                "This Is the message",
                "noreply@StageRibbon.com",
                ["18jwdat@gmail.com","tajwdat3@gmail.com"],
                html_message=html,
                fail_silently=False,
                )
                
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,"contact.html",{"form":form})