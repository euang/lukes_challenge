# smtpd_command_filter (default: empty)
 A mechanism to transform commands from remote SMTP clients.
This is a last-resort tool to work around client commands that break
interoperability with the Postfix SMTP server. Other uses involve
fault injection to test Postfix's handling of invalid commands.



 Specify the name of a "type:table" lookup table. The search
string is the SMTP command as received from the remote SMTP client,
except that initial whitespace and the trailing <CR><LF>
are removed. The result value is executed by the Postfix SMTP
server. 


 There is no need to use smtpd\_command\_filter for the following
cases: 


* Use "resolve\_numeric\_domain = yes" to accept
"*user@ipaddress*".
* Postfix already accepts the correct form
"*user@[ipaddress]*". Use virtual\_alias\_maps or canonical\_maps
to translate these into domain names if necessary.
* Use "strict\_rfc821\_envelopes = no" to accept "RCPT TO:<*User
Name <user@example.com>>*". Postfix will ignore the "*User
Name*" part and deliver to the *<user@example.com>* address.


 Examples of problems that can be solved with the smtpd\_command\_filter
feature: 



```

/etc/postfix/main.cf:
    smtpd\_command\_filter = pcre:/etc/postfix/command\_filter

```


```

/etc/postfix/command\_filter:
    # Work around clients that send malformed HELO commands.
    /^HELO\s\*$/ HELO domain.invalid

```


```

    # Work around clients that send empty lines.
    /^\s\*$/     NOOP

```


```

    # Work around clients that send RCPT TO:<'user@domain'>.
    # WARNING: do not lose the parameters that follow the address.
    /^(RCPT\s+TO:\s\*<)'([^[:space:]]+)'(>.\*)/     $1$2$3

```


```

    # Append XVERP to MAIL FROM commands to request VERP-style delivery.
    # See VERP\_README for more information on how to use Postfix VERP.
    /^(MAIL\s+FROM:\s\*<listname@example\.com>.\*)/   $1 XVERP

```


```

    # Bounce-never mail sink. Use notify\_classes=bounce,resource,software
    # to send bounced mail to the postmaster (with message body removed).
    /^(RCPT\s+TO:\s\*<.\*>.\*)\s+NOTIFY=\S+(.\*)/     $1 NOTIFY=NEVER$2
    /^(RCPT\s+TO:.\*)/                             $1 NOTIFY=NEVER

```

 This feature is available in Postfix 2.7. 


