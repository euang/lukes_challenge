# soft_bounce (default: no)

Safety net to keep mail queued that would otherwise be returned to
the sender. This parameter disables locally-generated bounces,
changes the handling of negative responses from remote servers,
content filters or plugins,
and prevents the Postfix SMTP server from rejecting mail permanently
by changing 5xx reply codes into 4xx. However, soft\_bounce is no
cure for address rewriting mistakes or mail routing mistakes.




Note: "soft\_bounce = yes" is in some cases implemented by modifying
server responses. Therefore, the response that Postfix logs may
differ from the response that Postfix actually sends or receives.




Example:




```

soft\_bounce = yes

```

