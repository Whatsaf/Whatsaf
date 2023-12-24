from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import smtplib
import psutil
import subprocess
import requests
import os

id = "26672558"
number = "+916355853038"
email = "contact@whatsaf.in"
temp_user_data_dir = f"C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {id}"

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

def check_chrome_profile_open():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'] == 'chrome.exe' and ('--user-data-dir='+temp_user_data_dir in process.info['cmdline']):
            return True
    return False

chrome_open = check_chrome_profile_open()
if chrome_open:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:8090")
    options.add_argument("minimize")
    wd = webdriver.Chrome(options=options)
    wd.minimize_window()
    wd.get("https://web.whatsapp.com")
else:
    subprocess.Popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8090 --user-data-dir="C:\Users\A\AppData\Local\Google\Chrome\User Data\Profile 26672558"')
    options = webdriver.ChromeOptions()
    options.add_argument("minimize")
    options.add_experimental_option("debuggerAddress", "localhost:8090")
    wd = webdriver.Chrome(options=options)
    wd.get("https://web.whatsapp.com")

def active():
    time.sleep(30)
    wd.execute_script('document.getElementsByClassName("_3iLTh")[0].click();')
    time.sleep(20)
    wd.execute_script('document.getElementsByClassName("selectable-text g0rxnol2 k2bacm8l g2bpp9au ln8gz9je cc8mgx9x eta5aym1 d9802myq e4xiuwjv thr4l2wc cixrojiy enbbiyaj g33ro0j9 i5tg98hk f9ovudaz przvwfww gx1rr48f")[0].setAttribute("id", "inp");')
    time.sleep(2)
    input_1=wd.find_element(by=By.ID, value= 'inp')
    time.sleep(2)
    for i in range(5):
        input_1.send_keys(Keys.BACKSPACE)
    input_1.send_keys(number)
    input_1.send_keys(Keys.ENTER)
    time.sleep(8)
    otps = wd.execute_script("""let textContent = document.querySelector('div').innerText;
                    return textContent""")
    st = otps.split("\n")
    otp = ""
    for i in st:
        if (i.isnumeric() or i.isupper()) and len(i) == 1:
            otp += i
    sendEmail(email, "Your WhatsApp Code", '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>  <!--[if gte mso 9]><xml>  <o:OfficeDocumentSettings>    <o:AllowPNG/>    <o:PixelsPerInch>96</o:PixelsPerInch>  </o:OfficeDocumentSettings></xml><![endif]-->  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <meta name="x-apple-disable-message-reformatting">  <!--[if !mso]><!-->  <meta http-equiv="X-UA-Compatible" content="IE=edge">  <!--<![endif]-->  <title></title>  <style type="text/css">    @media only screen and (min-width: 620px) {      .u-row {        width: 600px !important;      }      .u-row .u-col {        vertical-align: top;      }      .u-row .u-col-100 {        width: 600px !important;      }    }        @media (max-width: 620px) {      .u-row-container {        max-width: 100% !important;        padding-left: 0px !important;        padding-right: 0px !important;      }      .u-row .u-col {        min-width: 320px !important;        max-width: 100% !important;        display: block !important;      }      .u-row {        width: 100% !important;      }      .u-col {        width: 100% !important;      }      .u-col>div {        margin: 0 auto;      }    }        body {      margin: 0;      padding: 0;    }        table,    tr,    td {      vertical-align: top;      border-collapse: collapse;    }        p {      margin: 0;    }        .ie-container table,    .mso-container table {      table-layout: fixed;    }        * {      line-height: inherit;    }        a[x-apple-data-detectors='true'] {      color: inherit !important;      text-decoration: none !important;    }        table,    td {      color: #000000;    }        #u_body a {      color: #0000ee;      text-decoration: underline;    }        @media (max-width: 480px) {      #u_content_image_1 .v-src-width {        width: auto !important;      }      #u_content_image_1 .v-src-max-width {        max-width: 22% !important;      }    }  </style>  <!--[if !mso]><!-->  <link href="https://fonts.googleapis.com/css?family=Cabin:400,700" rel="stylesheet" type="text/css">  <!--<![endif]--></head><body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f9f9f9;color: #000000">  <!--[if IE]><div class="ie-container"><![endif]-->  <!--[if mso]><div class="mso-container"><![endif]-->  <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f9f9f9;width:100%" cellpadding="0" cellspacing="0">    <tbody>      <tr style="vertical-align: top">        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f9f9f9;"><![endif]-->          <div class="u-row-container" style="padding: 0px;background-color: transparent">            <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">              <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">                  <div style="height: 100%;width: 100% !important;">                    <!--[if (!mso)&(!IE)]><!-->                    <div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">                      <!--<![endif]-->                      <table id="u_content_image_1" style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Cabin',sans-serif;" align="left">                              <table width="100%" cellpadding="0" cellspacing="0" border="0">                                <tr>                                  <td style="padding-right: 0px;padding-left: 0px;" align="center">                                    <img align="center" border="0" src="https://whatsaf.in/static/img/Whatsaficon.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 32%;max-width: 179.2px;"                                      width="179.2" class="v-src-width v-src-max-width" />                                  </td>                                </tr>                              </table>                            </td>                          </tr>                        </tbody>                      </table>                      <!--[if (!mso)&(!IE)]><!-->                    </div>                    <!--<![endif]-->                  </div>                </div>                <!--[if (mso)|(IE)]></td><![endif]-->                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->              </div>            </div>          </div>          <div class="u-row-container" style="padding: 0px;background-color: transparent">            <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #003399;">              <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #003399;"><![endif]-->                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">                  <div style="height: 100%;width: 100% !important;">                    <!--[if (!mso)&(!IE)]><!-->                    <div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">                      <!--<![endif]-->                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:40px 10px 10px;font-family:'Cabin',sans-serif;" align="left">                              <table width="100%" cellpadding="0" cellspacing="0" border="0">                                <tr>                                  <td style="padding-right: 0px;padding-left: 0px;" align="center">                                    <img align="center" border="0" src="https://cdn.templates.unlayer.com/assets/1597218650916-xxxxc.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 26%;max-width: 150.8px;"                                      width="150.8" class="v-src-width v-src-max-width" />                                  </td>                                </tr>                              </table>                            </td>                          </tr>                        </tbody>                      </table>                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 31px;font-family:'Cabin',sans-serif;" align="left">                              <div style="color: #e5eaf5; line-height: 140%; text-align: center; word-wrap: break-word;">                                <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 30px; line-height: 42px;">WHATSAPP CODE - '''+otp+'''</span></strong></p>                              </div>                            </td>                          </tr>                        </tbody>                      </table>                      <!--[if (!mso)&(!IE)]><!-->                    </div>                    <!--<![endif]-->                  </div>                </div>                <!--[if (mso)|(IE)]></td><![endif]-->                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->              </div>            </div>          </div>          <div class="u-row-container" style="padding: 0px;background-color: transparent">            <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">              <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">                  <div style="height: 100%;width: 100% !important;">                    <!--[if (!mso)&(!IE)]><!-->                    <div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">                      <!--<![endif]-->                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:33px 55px;font-family:'Cabin',sans-serif;" align="left">                              <div style="line-height: 160%; text-align: center; word-wrap: break-word;">                                <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 22px; line-height: 35.2px;">Hello there,</span></p>                                <p style="line-height: 160%; font-size: 14px;"><span style="font-size: 18px; line-height: 28.8px;">As part of our ongoing commitment to fortifying communication security, we kindly request your assistance in entering the verification code for WhatsApp. This imperative step will solidify our company's communication channels, ensuring a secure and seamless exchange of information. Your prompt action in entering this code is instrumental in bolstering the trust and reliability of our correspondence through WhatsApp. We prioritize the safeguarding of our communication platforms and greatly value your cooperation in this critical security measure. Should you have any queries or require further clarification regarding this request, please do not hesitate to contact our support team. We appreciate your swift attention to this matter and thank you for your continued trust in our company's communication protocols.</span></p>                              </div>                            </td>                          </tr>                        </tbody>                      </table>                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:33px 55px 60px;font-family:'Cabin',sans-serif;" align="left">                              <div style="line-height: 160%; text-align: center; word-wrap: break-word;">                                <p style="line-height: 160%; font-size: 14px;"><span style="font-size: 18px; line-height: 28.8px;">Regards,</span></p>                                <p style="line-height: 160%; font-size: 14px;"><span style="font-size: 18px; line-height: 28.8px;">Team Whatsaf</span></p>                              </div>                            </td>                          </tr>                        </tbody>                      </table>                      <!--[if (!mso)&(!IE)]><!-->                    </div>                    <!--<![endif]-->                  </div>                </div>                <!--[if (mso)|(IE)]></td><![endif]-->                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->              </div>            </div>          </div>          <div class="u-row-container" style="padding: 0px;background-color: transparent">            <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #e5eaf5;">              <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #e5eaf5;"><![endif]-->                <!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">                  <div style="height: 100%;width: 100% !important;">                    <!--[if (!mso)&(!IE)]><!-->                    <div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">                      <!--<![endif]-->                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:41px 55px 18px;font-family:'Cabin',sans-serif;" align="left">                              <div style="color: #003399; line-height: 160%; text-align: center; word-wrap: break-word;">                                <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 20px; line-height: 32px;"><strong>You are receiving this email from official email address of Whatsaf (no-reply@whatsaf.in).</strong></span></p>                                <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 16px; line-height: 25.6px; color: #000000;">whatsaf.in</span></p>                                <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 16px; line-height: 25.6px; color: #000000;"><a rel="noopener" href="mailto:contact@whatsaf.in" target="_blank">contact@whatsaf.in</a></span></p>                                <p style="font-size: 14px; line-height: 160%;"> </p>                                <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 16px; line-height: 25.6px; color: #000000;"><a rel="noopener" href="https://whatsaf.in/unsubscribe/'''+email+'''" target="_blank">Unsubscribe</a> | <a rel="noopener" href="https://whatsaf.in/blogs/" target="_blank">Blogs</a> | <a rel="noopener" href="https://whatsaf.in" target="_blank">Visit Website</a></span></p>                              </div>                            </td>                          </tr>                        </tbody>                      </table>                      <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">                        <tbody>                          <tr>                            <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 33px;font-family:'Cabin',sans-serif;" align="left">                              <div align="center">                                <div style="display: table; max-width:244px;">                                  <!--[if (mso)|(IE)]><table width="244" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:244px;"><tr><![endif]-->                                  <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 17px;" valign="top"><![endif]-->                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 17px">                                    <tbody>                                      <tr style="vertical-align: top">                                        <td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">                                          <a href="https://www.linkedin.com/company/whatsaf/about/" title="LinkedIn" target="_blank">                                            <img src="https://cdn.tools.unlayer.com/social/icons/circle-black/linkedin.png" alt="LinkedIn" title="LinkedIn" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">                                          </a>                                        </td>                                      </tr>                                    </tbody>                                  </table>                                  <!--[if (mso)|(IE)]></td><![endif]-->                                  <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 17px;" valign="top"><![endif]-->                                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 17px">                                        <tbody>                                          <tr style="vertical-align: top">                                            <td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">                                              <a href="https://www.youtube.com/channel/UCkf9wsUy4pTPv79gy7mAw5Q" title="LinkedIn" target="_blank">                                                <img src="https://cdn.tools.unlayer.com/social/icons/circle-black/youtube.png" alt="YouTube" title="LinkedIn" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">                                              </a>                                            </td>                                          </tr>                                        </tbody>                                      </table>                                      <!--[if (mso)|(IE)]></td><![endif]-->                                      <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 17px;" valign="top"><![endif]-->                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 17px">                                    <tbody>                                      <tr style="vertical-align: top">                                        <td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">                                          <a href="https://twitter.com/WhatsafOfficial" title="LinkedIn" target="_blank">                                            <img src="https://cdn.tools.unlayer.com/social/icons/circle-black/x.png" alt="X" title="LinkedIn" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">                                          </a>                                        </td>                                      </tr>                                    </tbody>                                  </table>                                  <!--[if (mso)|(IE)]></td><![endif]-->                                  <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->                                </div>                              </div>                            </td>                          </tr>                        </tbody>                      </table>                      <!--[if (!mso)&(!IE)]><!-->                    </div>                    <!--<![endif]-->                  </div>                </div>                <!--[if (mso)|(IE)]></td><![endif]-->                <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->              </div>            </div>          </div>          <!--[if (mso)|(IE)]></td></tr></table><![endif]-->        </td>      </tr>    </tbody>  </table>  <!--[if mso]></div><![endif]-->  <!--[if IE]></div><![endif]--></body></html>''')

def check():
    text = wd.execute_script("""let textContent = document.querySelector('div').innerText;
                      return textContent""")
    if text.__contains__("Use WhatsApp on your computer") or text.__contains__("Enter code on phone"):
        return False
    else:
        return True
    
def getData():
    time.sleep(0.3)
    dataDict = {
                "Contacts" : [],
                "ProfilePhoto" : "",
                "Name" : "",
                "About" : "",
                "LastSeenStatus" : "",
                "OnlineSeenStatus" : "",
                "PPStatus" : "",
                "AboutStatus" : "",
                "ReadRecipents" : None,
                "BlockedContacts" : "",
                "ContactPP" : []
            }
    length = wd.execute_script('''var len = document.getElementsByClassName("lhggkp7q ln8gz9je rx9719la").length
                               return len''')
    time.sleep(0.5)
    for i in range(length):
        wd.execute_script(f'document.getElementsByClassName("lhggkp7q ln8gz9je rx9719la")[{i}].setAttribute("id", "chat{i}");')
        chats = wd.find_element(by=By.ID, value= f'chat{i}')
        chats.click()
        wd.execute_script(f'document.getElementsByClassName("_2au8k")[0].setAttribute("id", "info");')
        info = wd.find_element(by=By.ID, value= f'info')
        info.click()
        try:
            name = wd.execute_script(f'''var name = document.getElementsByClassName("l7jjieqr cw3vfol9 _11JPr selectable-text copyable-text")[0].innerText
                            return name''')
            phone = wd.execute_script(f'''var phone = document.getElementsByClassName("enbbiyaj e1gr2w1z hp667wtd")[0].innerText
                            return phone''')
            dataDict.get("Contacts").append(f"{name}|{phone}")
        except Exception:
            continue
    
    # fetching profile photo
    wd.execute_script('document.getElementsByClassName("g0rxnol2 f804f6gw ln8gz9je ppled2lx gfz4du6o r7fjleex g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb jpthtbts lyqpd7li bs7a17vp csshhazd _11JPr")[0].click()')
    ppLink = wd.execute_script('''var ppLink = document.getElementsByClassName("_11JPr")[0].src
                               return ppLink''')
    userName = wd.execute_script('''var name = document.getElementsByClassName("f804f6gw ln8gz9je")[0].innerText
                               return name''')
    about = wd.execute_script('''var about = document.getElementsByClassName("f804f6gw ln8gz9je")[1].innerText
                               return about''')

    r = requests.get(ppLink, stream=True)
    file_path = f"F:\\Whatsaf\\Whatsaf\\RequiredImages\\WhatsAppProfilePhoto\\{id}.enc"
    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
    dataDict["ProfilePhoto"] = f"F:\Whatsaf\Whatsaf\RequiredImages\WhatsAppProfilePhoto\{id}.enc"
    dataDict["Name"] = userName
    dataDict["About"] = about

    wd.execute_script('''
                      document.getElementsByClassName('kk3akd72 dmous0d2 fewfhwl7 ajgl1lbb ltyqj8pj')[0].click();
                      document.getElementsByClassName("_3ndVb fbgy3m38 ft2m32mm oq31bsqd nu34rnf1")[4].click();''')
    wd.execute_script('''document.getElementsByClassName('iWqod _1MZM5 _2BNs3')[4].click();''')
    wd.execute_script('''document.getElementsByClassName('tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 ac2vgrno f8m0rgwh elxb2u3l mx771qyo cm280p3y fbgy3m38 oq31bsqd qmxv8cnq')[1].click();''')
    ariaCheckLabel = {
        1 : "Everyone",
        3 : "MyContacts",
        5 : "Excluded",
        7  : "Nobody"
    }

    # Last Seen
    wd.execute_script("document.getElementsByClassName('daad4uqs p9a4hubg ml4r5409 gndfcl4n p357zi0d')[0].click()")
    for i in range(8):
        if i % 2 != 0:
            vari = wd.execute_script(f"""var vari = document.getElementsByTagName('button')[{i}].ariaChecked;
                              return vari""")
            if vari == "true":
                status = ariaCheckLabel.get(i)
                break
    dataDict["LastSeenStatus"] = status

    # Online Status
    for i in range(8, 12):
        if i % 2 != 0:
            vari = wd.execute_script(f"""var vari = document.getElementsByTagName('button')[{i}].ariaChecked;
                              return vari""")
            if vari == "true":
                if i == 9:
                    status = True
                elif i == 11:
                    status = False
                else:
                    pass
    dataDict["OnlineSeenStatus"] = str(status)

    # Profile Photo Status
    wd.execute_script("document.getElementsByClassName('kk3akd72 dmous0d2 fewfhwl7 ajgl1lbb ltyqj8pj')[0].click();")
    wd.execute_script("document.getElementsByClassName('daad4uqs p9a4hubg ml4r5409 gndfcl4n p357zi0d')[1].click()")
    for i in range(8):
        if i % 2 != 0:
            vari = wd.execute_script(f"""var vari = document.getElementsByTagName('button')[{i}].ariaChecked;
                              return vari""")
            if vari == "true":
                status = ariaCheckLabel.get(i)
                break
    dataDict["PPStatus"] = status

    # About Status
    wd.execute_script("document.getElementsByClassName('kk3akd72 dmous0d2 fewfhwl7 ajgl1lbb ltyqj8pj')[0].click();")
    wd.execute_script("document.getElementsByClassName('daad4uqs p9a4hubg ml4r5409 gndfcl4n p357zi0d')[2].click()")
    for i in range(8):
        if i % 2 != 0:
            vari = wd.execute_script(f"""var vari = document.getElementsByTagName('button')[{i}].ariaChecked;
                              return vari""")
            if vari == "true":
                status = ariaCheckLabel.get(i)
                break
    dataDict["AboutStatus"] = status

    # Read Recipents
    wd.execute_script("document.getElementsByClassName('kk3akd72 dmous0d2 fewfhwl7 ajgl1lbb ltyqj8pj')[0].innerText")
    try:
        wd.execute_script("document.getElementsByClassName('lhggkp7q hdpg1tjz ptatjang dj32rci9 g965lu3b q4zabkcz q0ohlrvj av59jz02 grf4wkbn hir9ny8g bs7a17vp b73q89nx em5jvqoa a21kwdn3 ehl15zf9')[0].innerText")
        status = True
    except Exception:
        status = False
    dataDict["ReadRecipents"] = status

    print(dataDict)

    return dataDict