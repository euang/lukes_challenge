# non_smtpd_milters (default: empty)
 A list of Milter (mail filter) applications for new mail that
does not arrive via the Postfix smtpd(8) server. This includes local
submission via the sendmail(1) command line, new mail that arrives
via the Postfix qmqpd(8) server, and old mail that is re-injected
into the queue with "postsuper -r". Specify space or comma as a
separator. See the MILTER\_README document for details. 


 This feature is available in Postfix 2.3 and later. 


