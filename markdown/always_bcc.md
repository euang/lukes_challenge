# always_bcc (default: empty)

Optional address that receives a "blind carbon copy" of each message
that is received by the Postfix mail system.




Note: with Postfix 2.3 and later the BCC address is added as if it
was specified with NOTIFY=NONE. The sender will not be notified
when the BCC address is undeliverable, as long as all down-stream
software implements RFC 3461.




Note: with Postfix 2.2 and earlier the sender will be notified
when the BCC address is undeliverable.



 Note: automatic BCC recipients are produced only for new mail.
To avoid mailer loops, automatic BCC recipients are not generated
after Postfix forwards mail internally, or after Postfix generates
mail itself. 


