from econome.celery import app
from django.core.mail import send_mail
from django.core.mail import EmailMessage


@app.task(bind=True, max_retries=12, default_retry_delay=360)
def send_email(self, subject, message, from_email, to):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[to],
            fail_silently=False
        )
    except Exception as e:
        raise self.retry(exc=e, countdown=360)


def send_mass_email(subject, message, from_email, to):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to,
            fail_silently=False
        )
    except Exception as e:
        print(e)

def send_mass_email_silently(subject, message, from_email, to):
    try:
        email = EmailMessage(
            subject,
            message,
            from_email=from_email,
            bcc=to,
        )
        email.send()
    except Exception as e:
        print(e)

def send_mass_email_silently_html(subject, message, from_email, to):
    try:
        email = EmailMessage(
            subject,
            message,
            from_email=from_email,
            bcc=to,
        )
        email.content_subtype = "html"
        email.send()
    except Exception as e:
        print(e)



@app.task
def send_hmail(subject, message, from_email, to):
    send_mail(
        subject=subject,
        message='',
        from_email=from_email,
        recipient_list=[to],
        fail_silently=False,
        html_message=message
    )


@app.task
def send_fmail(subject, message, from_email, to, path):
    email = EmailMessage(
        subject,
        message,
        from_email,
        [to],
        reply_to=[from_email],
    )
    email.attach_file(path)
    email.send()
