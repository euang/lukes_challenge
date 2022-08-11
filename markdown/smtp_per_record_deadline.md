# smtp_per_record_deadline (default: no)
 Change the behavior of the smtp\_\*\_timeout time limits, from a
time limit per read or write system call, to a time limit to send
or receive a complete record (an SMTP command line, SMTP response
line, SMTP message content line, or TLS protocol message). This
limits the impact from hostile peers that trickle data one byte at
a time. 


 Note: when per-record deadlines are enabled, a short timeout
may cause problems with TLS over very slow network connections.
The reasons are that a TLS protocol message can be up to 16 kbytes
long (with TLSv1), and that an entire TLS protocol message must be
sent or received within the per-record deadline. 


 This feature is available in Postfix 2.9-3.6. With older
Postfix releases, the behavior is as if this parameter is set to
"no". Postfix 3.7 and later use smtp\_per\_request\_deadline. 


