import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email():
    # Your email credentials
    sender_email = 'mozzam607@gmail.com'
    sender_password = 'ckcy adna arxr glbm'

    # Recipient email and email details
    to_email = 'careers@coverstack.in'
    subject = 'Django/Nodejs Developer'
    body = 'I have 2 years of hands-on experience in Python and Node.js development, particularly in crafting microservices architectures. Additionally, I hold certifications in AWS Cloud Practitioner and Azure AZ-900, showcasing my understanding of cloud technologies and their operational principles.\n\n Below is my resume for your reference.'

    # Resume attachment
    resume_path = f"Mozzam's Resume.pdf"

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the resume
    with open(resume_path, 'rb') as resume_file:
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
