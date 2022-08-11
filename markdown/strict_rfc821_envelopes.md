# strict_rfc821_envelopes (default: no)

Require that addresses received in SMTP MAIL FROM and RCPT TO
commands are enclosed with <>, and that those addresses do
not contain RFC 822 style comments or phrases. This stops mail
from poorly written software.




By default, the Postfix SMTP server accepts RFC 822 syntax in MAIL
FROM and RCPT TO addresses.



