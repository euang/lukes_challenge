# allow_mail_to_files (default: alias, forward)

Restrict local(8) mail delivery to external files. The default is
to disallow "/file/name" destinations in :include: files (see
aliases(5) for the text that defines this terminology).




Specify zero or more of: **alias**, **forward** or **include**,
in order to allow "/file/name" destinations in aliases(5), .forward
files and in :include: files, respectively.




Example:




```

allow\_mail\_to\_files = alias,forward,include

```

