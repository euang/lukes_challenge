# smtp_skip_4xx_greeting (default: yes)

Skip SMTP servers that greet with a 4XX status code (go away, try
again later).




By default, the Postfix SMTP client moves on the next mail exchanger.
Specify
"smtp\_skip\_4xx\_greeting = no" if Postfix should defer delivery
immediately.



 This feature is available in Postfix 2.0 and earlier.
Later Postfix versions always skip remote SMTP servers that greet
with a
4XX status code. 


