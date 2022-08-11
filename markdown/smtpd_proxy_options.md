# smtpd_proxy_options (default: empty)

List of options that control how the Postfix SMTP server
communicates with a before-queue content filter. Specify zero or
more of the following, separated by comma or whitespace. 



**speed\_adjust**
  Do not connect to a before-queue content filter until an entire
message has been received. This reduces the number of simultaneous
before-queue content filter processes. 


 NOTE 1: A filter must not *selectively* reject recipients
of a multi-recipient message. Rejecting all recipients is OK, as
is accepting all recipients. 


 NOTE 2: This feature increases the minimum amount of free queue
space by $message\_size\_limit. The extra space is needed to save the
message to a temporary file. 

 


This feature is available in Postfix 2.7 and later.



