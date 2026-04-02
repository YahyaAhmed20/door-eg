from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def send_text(request):
    if request.method == "POST":
        # ✅ 1. Get data and strip whitespace
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_content = request.POST.get('message', '').strip()

        # ✅ 2. Validation
        if name and email and message_content:
            try:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message_content
                )
                # ✅ 3. Use Django Messages Framework for Success
                messages.success(request, "Thank you! Your message has been sent successfully.")
                
                # ✅ 4. Redirect to prevent form resubmission on refresh (PRG Pattern)
                return redirect('contact:contact') # تأكد من اسم الـ URL الخاص بك
                
            except Exception as e:
                messages.error(request, "An error occurred. Please try again later.")
        else:
            messages.error(request, "Please fill in all required fields (Name, Email, Message).")

    # If GET request or after redirect
    return render(request, 'contact/contact.html')