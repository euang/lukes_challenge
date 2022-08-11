# smtp_per_request_deadline (default: no)
 Change the behavior of the smtp\_\*\_timeout time limits, from a
time limit per plaintext or TLS read or write call, to a combined
time limit for sending a complete SMTP request and for receiving a
complete SMTP response. The deadline limits only the time spent
waiting for plaintext or TLS read or write calls, not time spent
elsewhere. The per-request deadline limits the impact from hostile
peers that trickle data one byte at a time. 


 See smtp\_min\_data\_rate for how the per-request deadline is
managed during the DATA phase. 


 Note: when per-request deadlines are enabled, a short time limit
may cause problems with TLS over very slow network connections. The
reason is that a TLS protocol message can be up to 16 kbytes long
(with TLSv1), and that an entire TLS protocol message must be
transferred within the per-request deadline. 


 This feature is available in Postfix 3.7 and later. A weaker
feature, called smtp\_per\_record\_deadline, is available with Postfix
2.9-3.6. 


 This feature is available in Postfix 3.7 and later. 


