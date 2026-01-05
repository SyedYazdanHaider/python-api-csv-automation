import smtplib
from email.message import EmailMessage

hostEmailAddress ="sandbox.smtp.mailtrap.io"
hostPort =2525
hostUsername ="f3419e5aa0c751"
hostEmailPassword ="8be18fa70bc907"

message = EmailMessage()
message['Subject'] = "Automated Student Report"
message['From'] = "automation@test.com"
message['To'] = "client@example.com"

message.set_content("This is a test email sent from python.\nfind the attached automated report.\nRegards\nPython Automation Script")

with open("result2.txt","rb") as file:
    message.add_attachment(
        file.read(),
        maintype= "text",
        subtype= "plain",
        filename="result2.txt"
    )

with smtplib.SMTP(hostEmailAddress,hostPort) as server:
    server.login(hostUsername,hostEmailPassword)
    server.send_message(message)

print("Email sent successfully")