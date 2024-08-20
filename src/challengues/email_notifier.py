import smtplib as smtp_lib
import getpass


def send_email(from_email, from_pass, to_email, subject, body):
    message = f"Subject: {subject}\n\n{body}"
    with smtp_lib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(from_email, from_pass)
        server.sendmail(from_email, to_email, message)


if __name__ == "__main__":
    email = input("Enter your email address: ")
    passwd = getpass.getpass("Enter your password: ")

    # For testing purposes, just send the email to yourself
    send_email(email, passwd, email, "Test Email", "This is a test email from Python!")
