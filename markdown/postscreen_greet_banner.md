# postscreen_greet_banner (default: $smtpd_banner)
 The *text* in the optional "220-*text*..." server
response that
postscreen(8) sends ahead of the real Postfix SMTP server's "220
text..." response, in an attempt to confuse bad SMTP clients so
that they speak before their turn (pre-greet). Specify an empty
value to disable this feature. 


 This feature is available in Postfix 2.8. 


