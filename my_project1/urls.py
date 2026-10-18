from django.contrib import admin
from django.urls import path
from my_project1 import views

urlpatterns = [

    # =========================
    # MAIN WEBSITE
    # =========================

    path("", views.index, name="my_project1"),
    
# path of userse
    path("complain", views.complain, name="complain"),

    path("status", views.status, name="status"),

    path("contact", views.contact, name="contact"),

    path("profile", views.profile, name="profile"),

    path("emergency", views.emergency, name="emergency"),

    path("court", views.court, name="court"),

    path("about", views.about, name="about"),

    path(
        "term&condition",
        views.terms,
        name="terms"
    ),


    # =========================
    # USER AUTHENTICATION
    # =========================

    path(
        "login",
        views.login,
        name="user_login"
    ),

    path(
        "register",
        views.register,
        name="user_register"
    ),

    path(
        "forget",
        views.forget,
        name="user_forgot"
    ),
    
    path(
    "verify-otp",
    views.verify_otp,
    name="verify_otp"
    ),

    path(
        "new-password",
        views.new_password,
        name="new_password"
    ),
    path(
        "logout",
        views.logoutUser,
        name="logout"
    ),


    # =========================
    # STAFF
    # =========================

    path(
        "staff/login",
        views.staff_login,
        name="staff_login"
    ),

    path(
        "staff/profile",
        views.staff_profile,
        name="staff_profile"
    ),

    path(
        "staff/complaints",
        views.staff_complaints,
        name="staff_complaints"
    ),

    path(
        "staff/complaint/<str:complaint_id>",
        views.complaint_detail,
        name="complaint_detail"
    ),
]


# =========================
# DJANGO ADMIN
# =========================

admin.site.site_header = "ePolice Seva admin"

admin.site.site_title = "ePolice Seva Admin Portal"

admin.site.index_title = "Welcome to ePolice Seva Researcher Portal"