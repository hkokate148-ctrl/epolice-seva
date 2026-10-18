from django.shortcuts import render , redirect, HttpResponse
from datetime import datetime
from my_project1.models import Contact
from my_project1.models import Complain
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
# forget password
import random
from django.core.mail import send_mail
from django.conf import settings

@login_required(login_url="/login")
def profile(request):
    if request.user.is_staff:
        return redirect("/staff/profile")

    return render(request, "profile.html")

# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request,"Home.html")

@login_required(login_url="/login")
def complain(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        complain_type = request.POST.get("complaint_type")
        location = request.POST.get("location")
        incident_date = request.POST.get("incident_date")
        description = request.POST.get("description")
        evidence = request.FILES.get("evidence")

        # Professional Complaint ID generate karo
        last_complaint = Complain.objects.order_by("-id").first()

        if last_complaint:
            next_number = last_complaint.id + 1
        else:
            next_number = 1

        complaint_id = f"EPS-{datetime.now().year}-{next_number:05d}"

        # Complaint database me save karo
        Complain.objects.create(
            user=request.user,
            complaint_id=complaint_id,
            name=name,
            email=email,
            phone=phone,
            complain_type=complain_type,
            location=location,
            incident_date=incident_date,
            description=description,
            evidence=evidence,
            status="Submitted"
        )

        messages.success(
            request,
            f"✅ Complaint submitted successfully! Your Complaint ID is {complaint_id}"
        )

        return redirect("/complain")

    return render(request, "complain.html")

# Comlain Status    
@login_required(login_url="/login")
def status(request):

    complaint = None

    if request.method == "POST":

        complaint_id = request.POST.get("complaint_id", "").strip()

        try:
            complaint = Complain.objects.get(
                complaint_id=complaint_id,
                user=request.user
            )

        except Complain.DoesNotExist:

            messages.error(
                request,
                "❌ Complaint not found or this complaint does not belong to your account."
            )

    return render(
        request,
        "status.html",
        {
            "complaint": complaint
        }
    )
@login_required(login_url="/login")
def contact(request):                              
    # return HttpResponse("this is contect page") 
    if request.method=="POST":                      
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('description')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        # Success Message
        
        messages.success(request,"✅ Your message has been sent successfully!")
        return redirect("contact")
    
    return render(request,"contact.html")

def login(request):
    if request.method == "POST":

        username_or_email = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        # Pehle username se user dhundo
        user = User.objects.filter(
            username=username_or_email
        ).first()

        # Agar username nahi mila, to email se user dhundo
        if user is None:
            user = User.objects.filter(
                email=username_or_email
            ).first()

        # User mil gaya to authenticate karo
        if user is not None:
            user = authenticate(
                username=user.username,
                password=password
            )

        if user is not None:

            if user.is_staff:
                messages.error(
                    request,
                    "❌ This is a staff account. Please use Staff Login."
                )

                return render(
                    request,
                    "authentication/user/user_login.html"
                )

            auth_login(request, user)

            return redirect("/")

        else:
            messages.error(
                request,
                "❌ Invalid username or password."
            )

    return render(
        request,
        "authentication/user/user_login.html"
    )
        
def register(request):
    if request.method == "POST":                  
                                                
        #return HttpResponse("this is sign_in")    
        firstName = request.POST.get("firstName")
        email = request.POST.get("email")         
        password = request.POST.get("password")  
                                                
        # Username ke liye email use kar rahe hain
        print("Name:", firstName)
        print("Email:", email)

        username = firstName

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already registered.")
            return redirect("/register")

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect("/register")

        # User create karo
        user = User(
            username=username,
            first_name=firstName,
            email=email
        )

        # Password ko safely hash karke save karega
        user.set_password(password)
        user.save()
        print("USER SAVE HO GAYA:", user.id)

        messages.success(request,"✅ Registration successful! Please login.")

        return redirect("/login")

    return render(
        request,
        "authentication/user/user_register.html"
    )
            
def forget(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()

        user = User.objects.filter(email=email).first()

        if user is None:
            messages.error(
                request,
                "❌ This email is not registered."
            )
            return redirect("user_forgot")

        # 6 digit OTP
        otp = str(random.randint(100000, 999999))

        # Session me OTP aur user save
        request.session["reset_otp"] = otp
        request.session["reset_user_id"] = user.id

        # Email send
        send_mail(
            "ePolice Seva - Password Reset OTP",
            f"Your OTP for password reset is: {otp}\n\n"
            "This OTP is valid for password reset.",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        messages.success(
            request,
            "✅ OTP has been sent to your registered email."
        )

        return redirect("verify_otp")

    return render(
        request,
        "authentication/user/user_forgot.html"
    )

def verify_otp(request):

    if "reset_otp" not in request.session:
        messages.error(
            request,
            "❌ Please request OTP first."
        )
        return redirect("user_forgot")

    if request.method == "POST":

        entered_otp = request.POST.get("otp", "").strip()
        saved_otp = request.session.get("reset_otp")

        if entered_otp == saved_otp:

            # OTP correct
            request.session["otp_verified"] = True

            return redirect("new_password")

        else:
            messages.error(
                request,
                "❌ Invalid OTP. Please try again."
            )

    return render(
        request,
        "authentication/user/verify_otp.html"
    )

def new_password(request):

    if not request.session.get("otp_verified"):
        messages.error(
            request,
            "❌ Please verify OTP first."
        )
        return redirect("user_forgot")

    if request.method == "POST":

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "❌ Passwords do not match."
            )

            return redirect("new_password")

        user_id = request.session.get("reset_user_id")

        try:
            user = User.objects.get(id=user_id)

            user.set_password(password)
            user.save()

            # Reset session data
            request.session.pop("reset_otp", None)
            request.session.pop("reset_user_id", None)
            request.session.pop("otp_verified", None)

            messages.success(
                request,
                "✅ Password reset successfully. Please login."
            )

            return redirect("user_login")

        except User.DoesNotExist:

            messages.error(
                request,
                "❌ User not found."
            )

            return redirect("user_forgot")

    return render(
        request,
        "authentication/user/new_password.html"
    )

def logoutUser(request):
    logout(request)
    return redirect("/login")

def emergency(request):
    return render(request,"emergency.html")
def court(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"court.html")

def about(request):
    return render(request, "about&terms_condition/about.html")

def terms(request):
    return render(request, "about&terms_condition/terms.html")

# staff folder
@login_required(login_url="/login") #login karne ke liye kahega
def staff_complaints(request):

    if not request.user.is_staff: # if user not a staff so redirect
        return redirect("/")

    complaints = Complain.objects.all().order_by("-id") # finding All database complain by help hope id

    return render(
        request,
        "staff/complaints.html",
        {"complaints": complaints} # ye complain database me se html ko bhej rahe hai
    )
    
    # Staff folder ke under ka kam 
    
@login_required(login_url="/login")#login karne ke liye kahega
def complaint_detail(request, complaint_id):

    if not request.user.is_staff:
        return redirect("/")

    complaint = Complain.objects.get( # search in database specific complain
        complaint_id=complaint_id
    )

    if request.method == "POST": # check form is submited

        new_status = request.POST.get("status") # HTML form se status naam ki value nikali ja rahi hai.
                                                # exmaple:- investigation
        complaint.status = new_status # Ab jo complaint database se mili thi, uska status change kar rahe hain.
        complaint.save()

        messages.success(
            request,
            "✅ Complaint status updated successfully."
        )

        return redirect(
            "complaint_detail",     #Status update hone ke baad same complaint ke detail page par wapas bhej do.
            complaint_id=complaint.complaint_id
        )

    return render(
        request,
        "staff/complaint_detail.html", # if user only check pages so the page
        {"complaint": complaint}
    )
    
def staff_login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:
                auth_login(request, user)
                return redirect("/")

            else:
                messages.error(
                    request,
                    "You are not authorized as staff."
                )

        else:
            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "authentication/staff/staff_login.html")

@login_required(login_url="/login")
def staff_profile(request):
    if not request.user.is_staff:
        return redirect("/")

    return render(request, "staff/profile.html")
# End staff folder