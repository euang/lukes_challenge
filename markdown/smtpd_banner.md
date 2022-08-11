# smtpd_banner (default: $myhostname ESMTP $mail_name)

The text that follows the 220 status code in the SMTP greeting
banner. Some people like to see the mail version advertised. By
default, Postfix shows no version.




You MUST specify $myhostname at the start of the text. This is
required by the SMTP protocol.




Example:




```

smtpd\_banner = $myhostname ESMTP $mail\_name ($mail\_version)

```

