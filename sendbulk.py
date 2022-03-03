from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


li = ['johndoe@example.com', 'doejohn@example2.com']

length = len(li)

for i in range(length):

    X = li[i]
    reciver_mail = X

    print(reciver_mail)


SENDER = 'Good name<noreply@johndoe.com>'
SUBJECT = "Hopefulless"

message = MIMEMultipart()
message["from"] = SENDER
message['To'] = reciver_mail
message["subject"] = SUBJECT


HTML = """
<HTML>
<HEAD>
<a href="">
<img src=">
</a> 
</HTML>
"""


part2 = MIMEText(HTML, "html")


message.attach(part2)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("chris@gmail.com", "passisfake")
    smtp.send_message(message)
    print("Sent......")
