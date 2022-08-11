# smtpd_etrn_restrictions (default: empty)

Optional restrictions that the Postfix SMTP server applies in the
context of a client ETRN command.
See SMTPD\_ACCESS\_README, section "Delayed evaluation of SMTP access
restriction lists" for a discussion of evaluation context and time.




The Postfix ETRN implementation accepts only destinations that are
eligible for the Postfix "fast flush" service. See the ETRN\_README
file for details.




Specify a list of restrictions, separated by commas and/or whitespace.
Continue long lines by starting the next line with whitespace.
Restrictions are applied in the order as specified; the first
restriction that matches wins.




The following restrictions are specific to the domain name information
received with the ETRN command.




**check\_etrn\_access *type:table***
Search the specified access database for the ETRN domain name
or its parent domains. See the access(5) manual page for details.



Other restrictions that are valid in this context:



* Generic restrictions that can be used
in any SMTP command context, described under smtpd\_client\_restrictions.
* SMTP command specific restrictions described under
smtpd\_client\_restrictions and smtpd\_helo\_restrictions.



Example:




```

smtpd\_etrn\_restrictions = permit\_mynetworks, reject

```

