from django.shortcuts import render
from .models import ContactMessage

def send_text(request):
    context = {}
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')

        if name and email and message_content:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_content
            )
            # ✅ نمرر المتغير ده عشان نشغل المودال
            context['show_success_modal'] = True
        else:
            context['error'] = "يرجى ملء جميع الحقول المطلوبة."

    return render(request, 'contact/contact.html', context)