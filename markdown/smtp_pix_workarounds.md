# smtp_pix_workarounds (default: disable_esmtp, delay_dotcrlf)
 A list that specifies zero or more workarounds for CISCO PIX
firewall bugs. These workarounds are implemented by the Postfix
SMTP client. Workaround names are separated by comma or space, and
are case insensitive. This parameter setting can be overruled with
per-destination smtp\_pix\_workaround\_maps settings. 



**delay\_dotcrlf** Insert a delay before sending
".<CR><LF>" after the end of the message content. The
delay is subject to the smtp\_pix\_workaround\_delay\_time and
smtp\_pix\_workaround\_threshold\_time parameter settings. 
**disable\_esmtp** Disable all extended SMTP commands:
send HELO instead of EHLO. 

 This feature is available in Postfix 2.4 and later. The default
settings are backwards compatible with earlier Postfix versions.



