# delay_logging_resolution_limit (default: 2)
 The maximal number of digits after the decimal point when logging
sub-second delay values. Specify a number in the range 0..6. 


 Large delay values are rounded off to an integral number of seconds;
delay values below the delay\_logging\_resolution\_limit are logged
as "0", and delay values under 100s are logged with at most two-digit
precision. 


 The format of the "delays=a/b/c/d" logging is as follows: 


* a = time from message arrival to last active queue entry
* b = time from last active queue entry to connection setup
* c = time in connection setup, including DNS, EHLO and STARTTLS
* d = time in message transmission


 This feature is available in Postfix 2.3 and later. 


