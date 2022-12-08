import smtplib
from email.mime.text import MIMEText


def send_mail(name, weekday, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '3c17001d96231d'
    password = 'f543f91b34ab95'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {name}</li><li>Dealer: {weekday}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Daily Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())