# prepend_delivered_header (default: command, file, forward)
 The message delivery contexts where the Postfix local(8) delivery
agent prepends a Delivered-To: message header with the address
that the mail was delivered to. This information is used for mail
delivery loop detection. 



By default, the Postfix local delivery agent prepends a Delivered-To:
header when forwarding mail and when delivering to file (mailbox)
and command. Turning off the Delivered-To: header when forwarding
mail is not recommended.




Specify zero or more of **forward**, **file**, or **command**.




Example:




```

prepend\_delivered\_header = forward

```

