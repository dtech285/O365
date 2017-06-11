#!/usr/bin/env python3
import win32com.client as win32 # pip install pypiwin32

def __Emailer(text, subject, recipient, auto=True):
    #import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    if auto:
        mail.Display(True)
    else:
        mail.open # or whatever the correct code is


if __name__ == "__main__":
    __Emailer("test", "test", "tech285@gmail.com")

