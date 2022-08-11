# postscreen_dnsbl_reply_map (default: empty)
 A mapping from an actual DNSBL domain name which includes a secret
password, to the DNSBL domain name that postscreen will reply with
when it rejects mail. When no mapping is found, the actual DNSBL
domain will be used. 


 For maximal stability it is best to use a file that is read
into memory such as pcre:, regexp: or texthash: (texthash: is similar
to hash:, except a) there is no need to run postmap(1) before the
file can be used, and b) texthash: does not detect changes after
the file is read). 


 Example: 



```

/etc/postfix/main.cf:
    postscreen\_dnsbl\_reply\_map = texthash:/etc/postfix/dnsbl\_reply

```


```

/etc/postfix/dnsbl\_reply:
   secret.zen.spamhaus.org      zen.spamhaus.org

```

 This feature is available in Postfix 2.8. 


