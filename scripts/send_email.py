#!/usr/bin/env python3
from __future__ import annotations
import smtplib
from email.message import EmailMessage

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'bharmon1215@gmail.com'
SMTP_PASS = 'dygwbuvziyepwaka'

def send_email(to_addr: str, subject: str, body: str, html: str | None = None):
    msg = EmailMessage()
    msg['From'] = SMTP_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.set_content(body)
    if html:
        msg.add_alternative(html, subtype='html')

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.ehlo()
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)

if __name__ == '__main__':
    send_email(
        to_addr=SMTP_USER,
        subject='[OOSA] Test delivery',
        body='This is a test email from the OOSA operator.',
    )
    print('sent')
