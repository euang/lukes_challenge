# postscreen_post_queue_limit (default: $default_process_limit)
 The number of clients that can be waiting for service from a
real Postfix SMTP server process. When this queue is full, all
clients will
receive a 421 response. 


 This feature is available in Postfix 2.8. 


