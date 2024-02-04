import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email():
    # Your email credentials
    sender_email = 'Enter your mail'
    sender_password = 'Enter your password'

    # Recipient email and email details
    to_email = 'Email to whom you want to send'
    subject = 'Subject of the mail'
    body = 'Body message of the mail'

    # file attachment
    file_path = 'path/to/your/file'


    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the resume
    with open(file_path, 'rb') as resume_file:
        resume_attachment = MIMEApplication(resume_file.read(), Name='resume.pdf')

    resume_attachment['Content-Disposition'] = f'attachment; filename=resume.pdf'
    message.attach(resume_attachment)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

    print('Email sent successfully!')

# Call the function to send the email
send_email()
