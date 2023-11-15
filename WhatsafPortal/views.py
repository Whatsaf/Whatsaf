from django.shortcuts import render, redirect, HttpResponse
from WhatsafPortal.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login as authLogin, login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import smtplib
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
from WhatsafPortal.details import country_codes

mainDomain = "http://localhost:8000"
# C:\Users\A\AppData\Local\Google\Chrome\User Data
chromeLoc = "C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {profNum}"


def sendEmail(email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header('Whatsaf')), "no-reply@whatsaf.in"))
    msg['To'] = email
    msg["Subject"] = subject
    html = message
    msg.attach(MIMEText(html, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.starttls()
    s.login("officials.whatsaf@gmail.com", "tmgfumuscnuftwmc")
    s.sendmail("no-reply@whatsaf.in", email, msg.as_string())
    s.quit()
    return None

def otpGen():
    otp = ""
    for OTP in range(6):
        otp += str(random.randint(1, 9))
    return otp

def userid():
    otp = ""
    for OTP in range(6):
        otp += str(random.randint(1, 9))
    return otp

# Casual Coding of Whatsaf
def index(request):
    if request.user.is_authenticated:
        if UserDetail.objects.get(User = request.user).Verification == False:
            dropUser = User.objects.get(username = request.user)
            dropUser.delete()
        return render(request, "index.html", {"faq" : FAQ.objects.all(), "data" : UserDetail.objects.get(User = User.objects.get(username = request.user))})
    return render(request, "index.html", {"faq" : FAQ.objects.all()})

def error(request, exception):
    return render(request, "error.html")

def error500(request):
    return render(request, "error500.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        createContact = Contact(Name = name, Email = email, Subject = subject, Message = message)
        createContact.save()
        messages.success(request, "Thank you for contacting us. We will try to get you back ASAP...")
        return redirect("HomePage")
    return redirect("ErrorPage")

def signin(request):
    if request.user.is_authenticated:
        if UserDetail.objects.get(User = request.user).Verification == False:
            dropUser = User.objects.get(username = request.user)
            dropUser.delete()
    return render(request, "signin.html")

def signup(request):
    if request.user.is_authenticated:
        if UserDetail.objects.get(User = request.user).Verification == False:
            dropUser = User.objects.get(username = request.user)
            dropUser.delete()
    return render(request, "signup.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        country = request.POST["country"]
        phone = request.POST["phone"]
        dob = request.POST["dob"]
        username = request.POST["username"]
        pwd1 = request.POST["pwd1"]
        pwd2 = request.POST["pwd2"]
        eotp = otpGen()
        potp = otpGen()
        if pwd1 != pwd2:
           messages.warning(request, "Passwords not matching. PLease try again.")
           return redirect("SignUP")
        if User.objects.filter(username=username).exists():
            messages.warning(request, "This username is already taken. Please try using our suggested username.")
            suggest = f"{name}{userid()}"
            rndm = ''.join([random.choice(string.ascii_letters) for n in range(12)])
            if User.objects.filter(username = suggest).exists():
                suggest = f"{name}{userid()}{rndm}"
            return render(request, "signup.html", {"username" : suggest})
        if User.objects.filter(email=email).exists():
            messages.warning(request, "This email is already in use. Please try using a different email.")
            return redirect("SignUP")
        creating_user = User.objects.create_user(username=username, password=pwd1)
        creating_user.email = email
        creating_user.first_name = name
        creating_user.save()
        authenticating = authenticate(username=username, password=pwd2)
        if authenticating is not None:
            authLogin(request, authenticating)
            creatingUserDet = UserDetail(User = request.user, Phone = phone, DOB = dob, OTP1 = eotp, OTP2 = potp, Country = country)
            creatingUserDet.save()
            messages.success(request, "Your account has been created successfully. Now please verify yourself.")
            sendEmail(email, "Account Created", f"Thank you {name} for showing your trust and creating an account with us. We really appreciate you. Your OTP for email verification is - {eotp}. Thank you.")
            # Sharing OTP via whatsapp
            try:
                options = webdriver.ChromeOptions()
                options.add_argument(f'--user-data-dir={chromeLoc.format(profNum = "30082006")}')
                wd = webdriver.Chrome(options=options)
                cc = country_codes[country]
                wd.get(f"https://web.whatsapp.com/send?phone={cc}{phone}&text=Your OTP for whatsapp verification is: {potp}")
                time.sleep(10)
                wd.execute_script('document.getElementsByClassName("tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq")[0].click();')
                time.sleep(2)
                wd.close()
            except Exception as e:
                pass

            return redirect("Verification")
    return redirect("ErrorPage")

def verification(request):
    return render(request, "verify.html")

def verify(request):
    if request.method == "POST":
        eotp = request.POST["eotp"]
        potp = request.POST["potp"]
        user = User.objects.get(username = request.user)
        userdet = UserDetail.objects.get(User = user)
        if userdet.OTP1 == eotp and userdet.OTP2 == potp:
            userdet.Verification = True
            userdet.save()
            messages.success(request, "Congratulations! Your account has been verified...")
            return redirect("HomePage")
        else:
            messages.warning(request, "Incorrect OTP")
            return render(request, "verify.html")
    return redirect("ErrorPage")

def resend(request):
    if request.user.is_authenticated:
        userdet = UserDetail.objects.get(User = request.user)
        eotp = userdet.OTP1
        potp = userdet.OTP2

        sendEmail(request.user.email, "Resend OTP", f"On your request your new OTP is {eotp}.")
            
        try:
            options = webdriver.ChromeOptions()
            options.add_argument(f'--user-data-dir={chromeLoc.format(profNum = "30082006")}')
            wd = webdriver.Chrome(options=options)
            cc = country_codes[userdet.Country]
            wd.get(f"https://web.whatsapp.com/send?phone={cc}{userdet.Phone}&text=Your OTP for whatsapp verification is: {potp}")
            time.sleep(20)
            wd.execute_script('document.getElementsByClassName("tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq")[0].click();')
            time.sleep(2)
            wd.close()
        except Exception as e:
            pass
        return redirect("Verification")

    return redirect("ErrorPage")

def buy(request, slug):
    if request.user.is_authenticated:
        return render(request, "buy.html")
    messages.warning(request, "Please SignIN to proceed.")
    return redirect("SignIN")

def dashboard(request):
    return render(request, "dashboard.html", {"features" : Feature.objects.all()})

def signout(request):
    logout(request)
    messages.success(request, "You have been Signed Out.")
    return redirect("HomePage")

def forgotPass(request):
    return render(request, "forgot-password.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email = email).exists() == False:
            messages.success(request, "Please SignUP first.")
            return redirect("SignUP")
        user = User.objects.get(email = email)
        authenticating = authenticate(username=user.username, password=password)
        if authenticating is not None:
            authLogin(request, authenticating)
            messages.success(request, f"You have successfully logged in, {request.user.first_name}.")
        else:
            messages.warning(request, "Please enter the fields correctly.")
            return redirect("SignIN")
        return redirect("Dashboard")
    return redirect("ErrorPage")

def resetPass(request):
    if request.method == "POST":
        email = request.POST["email"]
        if User.objects.filter(email = email).exists:
            otp = otpGen()
            userdet = UserDetail.objects.get(User = User.objects.get(email = email))
            userdet.OTP1 = otp
            userdet.save()
            sendEmail(email, "Reset Password", f"On Your request of reset password. Your OTP {userdet.OTP1}")
            messages.success(request, "An email has been sent. Please checkout that.")
            return redirect("ForgotPassword")
    return redirect("ErrorPage")

def setPass(request):
    if request.method == "POST":
        otp = request.POST["otp"]
        pass1 = request.POST["pwd1"]
        pass2 = request.POST["pwd2"]
        userdet = UserDetail.objects.get(OTP1 = otp)
        if pass1 != pass2:
            return redirect("ForgotPassword")
        if userdet.OTP1 == otp:
            userdet.User.set_password(pass1)
            userdet.User.save()
            sendEmail(userdet.User.email, "Reset Password Successful", f"Your password has been reset successfully.")
            messages.success(request, "Your Password has been reset.")
            return redirect("HomePage")
    return redirect("ErrorPage")

def features(request):
    return render(request, "features.html", {"features" : Feature.objects.all(), "domain" : mainDomain})

def UserProfile(request):
    if request.user.is_authenticated:
        userdet = User.objects.get(username = request.user.username)
        userdet = UserDetail.objects.get(User = userdet)
        return render(request, "user-profile.html", {
            "image" : userdet.ProfilePhoto,
            "data" : userdet,
            "dob" : f"{userdet.DOB}"
        })
    else:
        return redirect("ErrorPage")

def EditUserProfile(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        pwd = request.POST["password"]
        user_details = User.objects.get(username = request.user)
        dob = request.POST["dob"]
        if check_password(pwd, request.user.password):
            userdet = User.objects.get(username=request.user)
            userdet.first_name = name
            userdet.email = email
            userdet.save()
            userDet = User.objects.get(username=request.user)
            user_det = UserDetail.objects.get(User = userDet)
            user_det.DOB = dob
            user_det.Phone = phone
            user_det.save()
            if len(request.FILES) != 0:
                photo = request.FILES["photo"]
                profilephoto = UserDetail.objects.get(User = user_details)
                profilephoto.ProfilePhoto = photo
                profilephoto.save()
            sendEmail(email, "Profile Updated", "This is to inform you that your Whatsaf profile has been updated.")
            messages.success(request, "Your profile has been updated.")
        else:
            messages.warning(request, "Incorrect password.")
        return redirect("UserProfile")
    return redirect("ErrorPage") 

def DeleteAccount(request):
    if request.method == "POST":
        pwd = request.POST["password"]
        if check_password(pwd, request.user.password):
            userdet = User.objects.get(username=request.user.username)
            sendEmail(request.user.email, "Account Deleted", "It is very sorrowful for us to see you go. We will surely improve our service. But for that kindly write us a feedback on our website or reply to this email. We will surely work hard on that. Thank you.")
            userdet.delete()
            messages.success(request, "We are really feeling very bad to see you go.")
            return redirect("HomePage")
        else:
            messages.warning(request, "Incorrect password.")
            return redirect("UserProfile")
    return redirect("ErrorPage")

def ChangePassword(request):
    if request.method == "POST":
        oldpass = request.POST["oldpass"]
        newpass = request.POST["newpass"]
        confpass = request.POST["confpass"]
        if newpass != confpass:
            messages.warning(request, "Passwords Unmatched.")
            return redirect("UserProfile")
        if check_password(oldpass, request.user.password):
            userdet = User.objects.get(username=request.user)
            userdet.set_password(newpass)
            userdet.save()
            userDet = User.objects.get(username=request.user)
            authLogin(request, userDet)
            sendEmail(request.user.email, "Password Changed", "This is to inform you that your Whatsaf account password has been successfully changed. Thank you.")
            messages.success(request, "Your password has been changed successfully.")
        else:
            messages.warning(request, "Incorrect password.")
        return redirect("UserProfile")
    return redirect("ErrorPage")

def TermsConditions(request):
    return render(request, "terms-conditions.html")

def userview(request, slug):
    if User.objects.filter(username = slug).exists() == False:
        return render(request, "user-view.html")
    user = User.objects.get(username = slug)
    userdet = UserDetail.objects.get(User = user)
    return render(request, "user-view.html", {"data" : userdet, "user" : user})
