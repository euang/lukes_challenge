# smtp_send_xforward_command (default: no)

Send the non-standard XFORWARD command when the Postfix SMTP server
EHLO response announces XFORWARD support.




This allows a Postfix SMTP delivery agent, used for injecting mail
into
a content filter, to forward the name, address, protocol and HELO
name of the original client to the content filter and downstream
queuing SMTP server. This can produce more useful logging than
localhost[127.0.0.1] etc.




This feature is available in Postfix 2.1 and later.



