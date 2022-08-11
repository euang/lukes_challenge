# smtpd_reject_footer (default: empty)
 Optional information that is appended after each Postfix SMTP
server
4XX or 5XX response. 


 The following example uses "\c" at the start of the template
(supported in Postfix 2.10 and later) to suppress the line break
between the reply text and the footer text. With earlier Postfix
versions, the footer text always begins on a new line, and the "\c"
is output literally. 



```

/etc/postfix/main.cf:
    smtpd\_reject\_footer = \c. For assistance, call 800-555-0101.
     Please provide the following information in your problem report:
     time ($localtime), client ($client\_address) and server
     ($server\_name).

```

 Server response: 



```

    550-5.5.1 <user@example> Recipient address rejected: User
    unknown. For assistance, call 800-555-0101. Please provide the
    following information in your problem report: time (Jan 4 15:42:00),
    client (192.168.1.248) and server (mail1.example.com).

```

 Note: the above text is meant to make it easier to find the
Postfix logfile records for a failed SMTP session. The text itself
is not logged to the Postfix SMTP server's maillog file. 


 Be sure to keep the text as short as possible. Long text may
be truncated before it is logged to the remote SMTP client's maillog
file, or before it is returned to the sender in a delivery status
notification. 


 The template text is not subject to Postfix configuration
parameter $name expansion. Instead, this feature supports a limited
number of $name attributes in the footer text. These attributes are
replaced with their current value for the SMTP session. 


 Note: specify $$name in footer text that is looked up from
regexp: or pcre:-based smtpd\_reject\_footer\_maps, otherwise the
Postfix server will not use the footer text and will log a warning
instead. 



 **client\_address**   The Client IP address that
is logged in the maillog file. 
 **client\_port**   The client TCP port that is
logged in the maillog file. 
 **localtime**   The server local time (Mmm dd
hh:mm:ss) that is logged in the maillog file. 
 **server\_name**   The server's myhostname value.
This attribute is made available for sites with multiple MTAs
(perhaps behind a load-balancer), where the server name can help
the server support team to quickly find the right log files. 

 Notes: 


* NOT SUPPORTED are other attributes such as sender, recipient,
or main.cf parameters.
* For safety reasons, text that does not match
$smtpd\_expansion\_filter is censored.


 This feature supports the two-character sequence \n as a request
for a line break in the footer text. Postfix automatically inserts
after each line break the three-digit SMTP reply code (and optional
enhanced status code) from the original Postfix reject message.



 To work around mail software that mis-handles multi-line replies,
specify the two-character sequence \c at the start of the template.
This suppresses the line break between the reply text and the footer
text (Postfix 2.10 and later). 


 This feature is available in Postfix 2.8 and later. 


