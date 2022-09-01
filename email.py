def send_email():
    smtpemail, smtppass, to, subject="mayuhengkarl@gmail.com","myh980510","mayuhengkarl@gmail.com","new pub!"
    img_data = open(imgname, "rb").read()
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = smtpemail
    msg["To"] = to

    text = MIMEText(body)
    msg.attach(text)
    

    s = smtplib.SMTP("smtp.gmail.com", "587")
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(smtpemail, smtppass)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()