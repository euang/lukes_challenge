# unverified_recipient_reject_reason (default: empty)
 The Postfix SMTP server's reply when rejecting mail with
reject\_unverified\_recipient. Do not include the numeric SMTP reply
code or the enhanced status code. By default, the response includes
actual address verification details.



 Example: 



```

unverified\_recipient\_reject\_reason = Recipient address lookup failed

```

 This feature is available in Postfix 2.6 and later. 


