# Email Sender Script

This Python script allows you to send emails with attachments using the Gmail SMTP server. It's a simple and customizable solution for sending job applications or any other emails with attachments.

## Features

- **Easy to Use:** Customize the recipient email, subject, and body of the email easily.
- **Attachment Support:** Attach your resume or any other document to your email.
- **Secure:** Uses the Gmail SMTP server with TLS encryption for secure email transmission.

## Prerequisites

Before using the script, make sure you have the following:

- [Python](https://www.python.org/) installed on your machine.
- A Gmail account for sending emails.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/email-sender-script.git
    cd email-sender-script
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Open `main.py` and update the following variables:

    ```python
    sender_email = 'your-email@gmail.com'
    sender_password = 'your-email-password'
    to_email = 'recipient-email@example.com'
    subject = 'Your Email Subject'
    body = 'Your email body goes here.'
    file_path = 'path/to/your/file'
    ```

4. Run the script:

    ```bash
    python main.py
    ```

## Note

- Ensure that "Less secure app access" is enabled for your Gmail account. You can enable it [here](https://myaccount.google.com/lesssecureapps).
- Use this script responsibly and avoid sending spam.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

