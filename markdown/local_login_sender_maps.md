# local_login_sender_maps (default: static:*)
 A list of lookup tables that are searched by the UNIX login name,
and that return a list of allowed envelope sender patterns separated
by space or comma. These sender patterns are enforced by the Postfix
postdrop(1) command. The default is backwards-compatible:
every user may specify any sender envelope address. 


 When no UNIX login name is available, the postdrop(1) command will
prepend "**uid:**" to the numerical UID and use that instead. 


 This feature ignores address extensions in the user-specified
envelope sender address. 


 The following sender patterns are special; these cannot be used
as part of a longer pattern. 



  **\***   This pattern allows any envelope sender address.

  **<>**    This pattern allows the empty
envelope sender address. See the
empty\_address\_local\_login\_sender\_maps\_lookup\_key configuration
parameter. 
  **@***domain*   This pattern allows an
envelope sender address when the '**@**' and *domain* part
match. 

 Examples: 



```

/etc/postfix/main.cf:
    # Allow root and postfix full control, anyone else can only
    # send mail as themselves. Use "uid:" followed by the numerical
    # UID when the UID has no entry in the UNIX password file.
    local\_login\_sender\_maps =
        inline:{ { root = \* }, { postfix = \* } },
        pcre:/etc/postfix/login\_senders

```


```

/etc/postfix/login\_senders:
   # Allow both the bare username and the user@domain forms.
    /(.+)/ $1 $1@example.com

```

 This feature is available in Postfix 3.6 and later. 


