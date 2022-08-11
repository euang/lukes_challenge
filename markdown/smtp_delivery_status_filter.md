# smtp_delivery_status_filter (default: $default_delivery_status_filter)
 Optional filter for the smtp(8) delivery agent to change the
delivery status code or explanatory text of successful or unsuccessful
deliveries. See default\_delivery\_status\_filter for details. 


 NOTE: This feature modifies Postfix SMTP client error or non-error
messages that may or may not be derived from remote SMTP server
responses. In contrast, the smtp\_reply\_filter feature modifies
remote SMTP server responses only. 


