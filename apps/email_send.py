from django.core.mail import send_mail


def send_email(subject, message, recipients):
    try:
        for recipient in recipients:
            send_mail(subject, message, 'asilbekbahtiyorov340@gmail.com', [recipient])
        return True, 'Email yuborildi'
    except Exception as e:
        return False, str(e)