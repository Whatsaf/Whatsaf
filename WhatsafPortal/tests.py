from django.test import TestCase

# Create your tests here.
s = "WHATSAPP WEB Enter code on phone Linking WhatsApp account +91 6355 853 038 (edit) Open WhatsApp on your phone Go to settings by tapping on your profile photo, Menu , or Settings Tap Linked devices and then Link a device Tap Link with phone number instead and enter this code on your phone A F 4 X - 7 J T A Link with QR code Tutorial Need help to get started?"
st = s.split(" ")
otp = ""
for i in st:
    if (i.isnumeric() or i.isupper()) and len(i) == 1:
        otp += i
print(otp)