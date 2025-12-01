from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request): 
    if request.method == "POST": 
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")

            # --- المنطق الذكي للتوجيه ---
            
            # 1. هل المستخدم "مشرف" (Staff)؟ -> وجهه للداشبورد فوراً
            if user.is_staff:
                return redirect('bookings:reviewer_dashboard')
            
            # 2. هل هناك رابط سابق (Next)؟ -> وجهه إليه (للعملاء العاديين)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            
            # 3. غير ذلك -> وجهه للصفحة الرئيسية
            return redirect('main:home') 
        
        else:
            messages.error(request, "Email or Password doesn't match!", "alert-danger")

    return render(request, "accounts/login.html")


def register_view(request): 
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["password2"]

        # 1. التحقق من تطابق كلمة المرور
        if password != password_confirm:
            messages.error(request, "Passwords don't match!", "danger")
            return render(request, "accounts/registration.html")

        # 2. التحقق من أن الإيميل غير مسجل مسبقاً
        if User.objects.filter(username=email).exists():
            messages.error(request, "This email is already registered!", "danger")
            return render(request, "accounts/registration.html")

        try:
            # إنشاء المستخدم
            # ملاحظة: نستخدم الإيميل كـ username لكي يعمل اللوجن
            new_user = User.objects.create_user(
                username=email,  
                email=email,
                password=password,
                first_name=username
            )
            new_user.save()
            
            messages.success(request, "Registration Successful, please login.", "success")
            return redirect("accounts:login")

        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong during registration.", "danger")

    return render(request, "accounts/registration.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Successfully", "success")
    return redirect("main:home") # عدل هذا الرابط لاسم الصفحة الرئيسية عندك