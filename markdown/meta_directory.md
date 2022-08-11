# meta_directory (default: see 'postconf -d' output)
 The location of non-executable files that are shared among
multiple Postfix instances, such as postfix-files, dynamicmaps.cf,
and the multi-instance template files main.cf.proto and master.cf.proto.
This directory should contain only Postfix-related files. Typically,
the meta\_directory parameter has the same default as the config\_directory
parameter (/etc/postfix or /usr/local/etc/postfix). 


 For backwards compatibility with Postfix versions 2.6..2.11,
specify "meta\_directory = $daemon\_directory" in main.cf before
installing or upgrading Postfix, or specify "meta\_directory =
/path/name" on the "make makefiles", "make install" or "make upgrade"
command line. 


 This feature is available in Postfix 3.0 and later. 


