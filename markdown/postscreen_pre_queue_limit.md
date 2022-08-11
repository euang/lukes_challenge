# postscreen_pre_queue_limit (default: $default_process_limit)
 The number of non-allowlisted clients that can be waiting for
a decision whether they will receive service from a real Postfix
SMTP server
process. When this queue is full, all non-allowlisted clients will
receive a 421 response. 


 This feature is available in Postfix 2.8. 


