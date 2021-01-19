# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class email:
    def init(self):
        print('Class email Init...')

    def send_gmail(self, mail_sender, mail_recipient, pwd, subject='제목없음', content='내용없음'):
        ### Send Email with Python ==================================================
        # ref : https://yeolco.tistory.com/93
        ### =========================================================================
        
        s = smtplib.SMTP('smtp.gmail.com', 587) # SMTP Connection, if gmail port = 587
        s.starttls() # Start TLS secure
        
        s.login(mail_sender, pwd) # gmail account, pwd

        msg = MIMEText(str(content)) # Content
        msg['Subject'] = str(subject) # Title
        
        s.sendmail(
            mail_sender,
            mail_recipient,
            msg.as_string()) # Send Email
        print("[ Complete ]: Sending Emails")
        
        s.quit() # Session End
        print("[ Complete ]: Session End")

if __name__ == '__main__':

    from secrets import gmail # gmail account infos
    mail_recipient = input('테스트 메일을 전송받을 이메일 주소를 입력하세요\n')
    mail_subject = '테스트 메일 제목입니다.'
    mail_content = '정상전송이 완료되었습니까?'

    mailing = email()
    mailing.send_gmail(
        mail_sender= gmail.email,
        mail_recipient= mail_recipient,
        pwd= gmail.pwd,
        subject= mail_subject,
        content= mail_content
    )
