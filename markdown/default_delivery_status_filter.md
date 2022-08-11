# default_delivery_status_filter (default: empty)
 Optional filter to replace the delivery status code or explanatory
text of successful or unsuccessful deliveries. This does not allow
the replacement of a successful status code (2.X.X) with an
unsuccessful status code (4.X.X or 5.X.X) or vice versa. 


 Note: the (smtp|lmtp)\_delivery\_status\_filter is applied only
once per recipient: when delivery is successful, when delivery is
rejected with 5XX, or when there are no more alternate MX or A
destinations. Use smtp\_reply\_filter or lmtp\_reply\_filter to inspect
responses for all delivery attempts. 


 The following parameters can be used to implement a filter for
specific delivery agents: lmtp\_delivery\_status\_filter,
local\_delivery\_status\_filter, pipe\_delivery\_status\_filter,
smtp\_delivery\_status\_filter or virtual\_delivery\_status\_filter. These
parameters support the same filter syntax as described here. 


 Specify zero or more "type:table" lookup table names, separated
by comma or whitespace. For each successful or unsuccessful delivery
to a recipient, the tables are queried in the specified order with
one line of text that is structured as follows: 



> 
> enhanced-status-code SPACE explanatory-text
> 


 The first table match wins. The lookup result must have the
same structure as the query, a successful status code (2.X.X) must
be replaced with a successful status code, an unsuccessful status
code (4.X.X or 5.X.X) must be replaced with an unsuccessful status
code, and the explanatory text field must be non-empty. Other results
will result in a warning. 


 Example 1: convert specific soft TLS errors into hard errors,
by overriding the first number in the enhanced status code. 



> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     smtp\_delivery\_status\_filter = pcre:/etc/postfix/smtp\_dsn\_filter
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/smtp\_dsn\_filter:
>     /^4(\.\d+\.\d+ TLS is required, but host \S+ refused to start TLS: .+)/
>         5$1
>     /^4(\.\d+\.\d+ TLS is required, but was not offered by host .+)/
>         5$1
>     # Do not change the following into hard bounces. They may
>     # result from a local configuration problem.
>     # 4.\d+.\d+ TLS is required, but our TLS engine is unavailable
>     # 4.\d+.\d+ TLS is required, but unavailable
>     # 4.\d+.\d+ Cannot start TLS: handshake failure
> 
> ```
> 
> 


 Example 2: censor the per-recipient delivery status text so
that it does not reveal the destination command or filename
when a remote sender requests confirmation of successful delivery.




> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     local\_delivery\_status\_filter = pcre:/etc/postfix/local\_dsn\_filter
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/local\_dsn\_filter:
>     /^(2\S+ delivered to file).+/    $1
>     /^(2\S+ delivered to command).+/ $1
> 
> ```
> 
> 


 Notes: 


* This feature will NOT override the soft\_bounce safety net.
* This feature will change the enhanced status code and text
that is logged to the maillog file, and that is reported to the
sender in delivery confirmation or non-delivery notifications.


 This feature is available in Postfix 3.0 and later. 


