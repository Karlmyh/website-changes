import smtplib

from email.mime.multipart import MIMEMultipart

def send_email():
    smtpemail, smtppass, to, subject="1075288776@qq.com","iliqwvsgcsntfhgj","yma@ruc.edu.cn","new pub!"
   
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = smtpemail
    msg["To"] = to

    
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    #s = smtplib.SMTP("smtp.163.com", "465")
  
   
    s.login(smtpemail, smtppass)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()