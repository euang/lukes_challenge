# notify_classes (default: resource, software)

The list of error classes that are reported to the postmaster. These
postmaster notifications do not replace user notifications. The
default is to report only the most serious problems. The paranoid
may wish to turn on the policy (UCE and mail relaying) and protocol
error (broken mail software) reports.



 NOTE: postmaster notifications may contain confidential information
such as SASL passwords or message content. It is the system
administrator's responsibility to treat such information with care.




The error classes are:




**bounce** (also implies **2bounce**)
Send the postmaster copies of the headers of bounced mail, and
send transcripts of SMTP sessions when Postfix rejects mail. The
notification is sent to the address specified with the
bounce\_notice\_recipient configuration parameter (default: postmaster).

**2bounce**
Send undeliverable bounced mail to the postmaster. The notification
is sent to the address specified with the 2bounce\_notice\_recipient
configuration parameter (default: postmaster). 
**data**
Send the postmaster a transcript of the SMTP session with an
error because a critical data file was unavailable. The notification
is sent to the address specified with the error\_notice\_recipient
configuration parameter (default: postmaster).   
 This feature
is available in Postfix 2.9 and later. 
**delay**
Send the postmaster copies of the headers of delayed mail (see
delay\_warning\_time). The
notification is sent to the address specified with the
delay\_notice\_recipient configuration parameter (default: postmaster).

**policy**
Send the postmaster a transcript of the SMTP session when a
client request was rejected because of (UCE) policy. The notification
is sent to the address specified with the error\_notice\_recipient
configuration parameter (default: postmaster). 
**protocol**
Send the postmaster a transcript of the SMTP session in case
of client or server protocol errors. The notification is sent to
the address specified with the error\_notice\_recipient configuration
parameter (default: postmaster). 
**resource**
Inform the postmaster of mail not delivered due to resource
problems. The notification is sent to the address specified with
the error\_notice\_recipient configuration parameter (default:
postmaster). 
**software**
Inform the postmaster of mail not delivered due to software
problems. The notification is sent to the address specified with
the error\_notice\_recipient configuration parameter (default:
postmaster). 


Examples:




```

notify\_classes = bounce, delay, policy, protocol, resource, software
notify\_classes = 2bounce, resource, software

```

