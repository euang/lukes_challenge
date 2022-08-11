# smtputf8_autodetect_classes (default: sendmail, verify)
 Detect that a message requires SMTPUTF8 support for the specified
mail origin classes. This is a workaround to avoid chicken-and-egg
problems during the initial SMTPUTF8 roll-out in environments with
pre-existing mail flows that contain UTF8. Those mail flows should
not break because Postfix suddenly refuses to deliver such mail
to down-stream MTAs that don't announce SMTPUTF8 support. 


 The problem is that Postfix cannot rely solely on the sender's
declaration that a message requires SMTPUTF8 support, because UTF8
may be introduced during local processing (for example, the client
hostname in Postfix's Received: header, adding @$myorigin or
.$mydomain to an incomplete address, address rewriting, alias
expansion, automatic BCC recipients, local forwarding, and changes
made by header checks or Milter applications). 


 For now, the default is to enable "SMTPUTF8 required" autodetection
only for Postfix sendmail command-line submissions and address
verification probes. This may change once SMTPUTF8 support achieves
world domination. However, sites that add UTF8 content via local
processing (see above) should autodetect the need for SMTPUTF8
support for all email.


 Specify one or more of the following: 



  **sendmail**    Submission with the Postfix
sendmail(1) command. 
  **smtpd**    Mail received with the smtpd(8)
daemon. 
  **qmqpd**    Mail received with the qmqpd(8)
daemon. 
  **forward**    Local forwarding or aliasing. When
a message is received with "SMTPUTF8 required", then the forwarded
(aliased) message always has "SMTPUTF8 required". 
  **bounce**    Submission by the bounce(8) daemon.
When a message is received with "SMTPUTF8 required", then the
delivery status notification always has "SMTPUTF8 required". 
  **notify**    Postmaster notification from the
smtp(8) or smtpd(8) daemon. 
  **verify**    Address verification probe from the
verify(8) daemon. 
  **all**    Enable SMTPUTF8 autodetection for all
mail. 

 This feature is available in Postfix 3.0 and later. 


