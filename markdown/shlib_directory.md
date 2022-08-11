# shlib_directory (default: see 'postconf -d' output)
 The location of Postfix dynamically-linked libraries
(libpostfix-\*.so), and the default location of Postfix database
plugins (postfix-\*.so) that have a relative pathname in the
dynamicmaps.cf file. The shlib\_directory parameter defaults to
"no" when Postfix dynamically-linked libraries and database plugins
are disabled at compile time, otherwise it typically defaults to
/usr/lib/postfix or /usr/local/lib/postfix. 


 Notes: 


* The directory specified with shlib\_directory should contain
only Postfix-related files. Postfix dynamically-linked libraries
and database plugins should not be installed in a "public" system
directory such as /usr/lib or /usr/local/lib. Linking Postfix
dynamically-linked library files or database plugins into non-Postfix
programs is not supported. Postfix dynamically-linked libraries
and database plugins implement a Postfix-internal API that changes
without maintaining compatibility.
* You can change the shlib\_directory value after Postfix is
built. However, you may have to run ldconfig or equivalent to prevent
Postfix programs from failing because the libpostfix-\*.so files are
not found. No ldconfig command is needed if you keep the libpostfix-\*.so
files in the compiled-in default $shlib\_directory location.


 This feature is available in Postfix 3.0 and later. 


