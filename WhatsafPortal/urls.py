from django.contrib import admin
from django.urls import path, include
from WhatsafPortal.views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("contact", contact, name = "Contact"),
    path("error", error, name = "ErrorPage"),
    path("signin", signin, name = "SignIN"),
    path("signup", signup, name = "SignUP"),
    path("register", register, name = "Register"),
    path("verify", verify, name = "Verify"),
    path("resend-otp", resend, name = "Resend"),
    path("verification", verification, name = "Verification"),
    path("buy/<str:slug>", buy, name = "Buy"),
    path("dashboard", dashboard, name = "Dashboard"),
    path("signout", signout, name = "SignOUT"),
    path("login", login, name = "Login"),
    path("forgot-password", forgotPass, name = "ForgotPassword"),
    path("reset-password", resetPass, name = "resetPass"),
    path("set-password", setPass, name = "setPass"),
    path("features", features, name = "Features"),
    path("user-profile", UserProfile, name = "UserProfile"),
    path("edit-userprofile", EditUserProfile, name = "EditUserProfile"),
    path("delete-account", DeleteAccount, name = "DeleteAccount"),
    path("change-password", ChangePassword, name = "ChangePassword"),
    path("terms-conditions", TermsConditions, name = "TermsConditions"),
    path("user/<str:slug>", userview, name = "UserView"),
]