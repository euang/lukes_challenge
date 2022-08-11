# smtp_tls_mandatory_protocols (default: see "postconf -d" output)
 TLS protocols that the Postfix SMTP client will use with mandatory
TLS encryption. In main.cf the values are separated by whitespace,
commas or colons. In the policy table "protocols" attribute (see
smtp\_tls\_policy\_maps) the only valid separator is colon. An empty value
means allow all protocols. 


 The valid protocol names (see SSL\_get\_version(3)) are "SSLv2",
"SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2" and "TLSv1.3". Starting with
Postfix 3.6, the default value is ">=TLSv1", which sets TLS 1.0 as
the lowest supported TLS protocol version (see below). Older releases
use the "!" exclusion syntax, also described below. 


 As of Postfix 3.6, the preferred way to limit the range of
acceptable protocols is to set a lowest acceptable TLS protocol version
and/or a highest acceptable TLS protocol version. To set the lower
bound include an element of the form: ">=*version*" where
*version* is a either one of the TLS protocol names listed above,
or a hexadecimal number corresponding to the desired TLS protocol
version (0301 for TLS 1.0, 0302 for TLS 1.1, etc.). For the upper
bound, use "<=*version*". There must be no whitespace between
the ">=" or "<=" symbols and the protocol name or number. 


 Hexadecimal protocol numbers make it possible to specify protocol
bounds for TLS versions that are known to OpenSSL, but might not be
known to Postfix. They cannot be used with the legacy exclusion syntax.
Leading "0" or "0x" prefixes are supported, but not required.
Therefore, "301", "0301", "0x301" and "0x0301" are all equivalent to
"TLSv1". Hexadecimal versions unknown to OpenSSL will fail to set the
upper or lower bound, and a warning will be logged. Hexadecimal
versions should only be used when Postfix is linked with some future
version of OpenSSL that supports TLS 1.4 or later, but Postfix does not
yet support a symbolic name for that protocol version. 


Hexadecimal example (Postfix ≥ 3.6):



> 
> 
> ```
> 
> # Allow only TLS 1.2 through (hypothetical) TLS 1.4, once supported
> # in some future version of OpenSSL (presently a warning is logged).
> smtp\_tls\_mandatory\_protocols = >=TLSv1.2, <=0305
> # Allow only TLS 1.2 and up:
> smtp\_tls\_mandatory\_protocols = >=0x0303
> 
> ```
> 
> 


 With Postfix < 3.6 there is no support for a minimum or maximum
version, and the protocol range is configured via protocol exclusions.
To require at least TLS 1.0, set "smtp\_tls\_mandatory\_protocols = !SSLv2,
!SSLv3". Listing the protocols to include, rather than the protocols to
exclude, is supported, but not recommended. The exclusion syntax more
accurately matches the underlying OpenSSL interface. 


 When using the exclusion syntax, take care to ensure that the range
of protocols supported by the Postfix SMTP client is contiguous. When
a protocol version is enabled, disabling any higher version implicitly
disables all versions above that higher version. Thus, for example: 



> 
> 
> ```
> 
> smtp\_tls\_mandatory\_protocols = !SSLv2, !SSLv3, !TLSv1.1
> 
> ```
> 
> 


 also disables any protocol versions higher than TLSv1.1 leaving
only "TLSv1" enabled. 


 Support for "TLSv1.3" was introduced in OpenSSL 1.1.1. Disabling
this protocol via "!TLSv1.3" is supported since Postfix 3.4 (or patch
releases ≥ 3.0.14, 3.1.10, 3.2.7 and 3.3.2). 


 While the vast majority of SMTP servers with DANE TLSA records now
support at least TLS 1.2, a few still only support TLS 1.0. If you use
"dane" or "dane-only" it is best not to disable TLSv1, except perhaps
via the policy table for destinations which you are sure will support
"TLSv1.2". 


 See the documentation of the smtp\_tls\_policy\_maps parameter and
TLS\_README for more information about security levels. 


 Example: 



```

# Preferred syntax with Postfix ≥ 3.6:
smtp\_tls\_mandatory\_protocols = >=TLSv1.2, <=TLSv1.3
# Legacy syntax:
smtp\_tls\_mandatory\_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1

```

 This feature is available in Postfix 2.3 and later. 


