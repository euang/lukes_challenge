# smtpd_tls_chain_files (default: empty)
 List of one or more PEM files, each holding one or more private keys
directly followed by a corresponding certificate chain. The file names
are separated by commas and/or whitespace. This parameter obsoletes the
legacy algorithm-specific key and certificate file settings. When this
parameter is non-empty, the legacy parameters are ignored, and a warning
is logged if any are also non-empty. 


 With the proliferation of multiple private key algorithms—which,
as of OpenSSL 1.1.1, include DSA (obsolete), RSA, ECDSA, Ed25519
and Ed448—it is increasingly impractical to use separate
parameters to configure the key and certificate chain for each
algorithm. Therefore, Postfix now supports storing multiple keys and
corresponding certificate chains in a single file or in a set of files.



 Each key must appear **immediately before** the corresponding
certificate, optionally followed by additional issuer certificates that
complete the certificate chain for that key. When multiple files are
specified, they are equivalent to a single file that is concatenated
from those files in the given order. Thus, while a key must always
precede its certificate and issuer chain, it can be in a separate file,
so long as that file is listed immediately before the file that holds
the corresponding certificate chain. Once all the files are
concatenated, the sequence of PEM objects must be: *key1, cert1,
[chain1], key2, cert2, [chain2], ..., keyN, certN, [chainN].* 


 Storing the private key in the same file as the corresponding
certificate is more reliable. With the key and certificate in separate
files, there is a chance that during key rollover a Postfix process
might load a private key and certificate from separate files that don't
match. Various operational errors may even result in a persistent
broken configuration in which the certificate does not match the private
key. 


 The file or files must contain at most one key of each type. If,
for example, two or more RSA keys and corresponding chains are listed,
depending on the version of OpenSSL either only the last one will be
used or a configuration error may be detected. Note that while
"Ed25519" and "Ed448" are considered separate algorithms, the various
ECDSA curves (typically one of prime256v1, secp384r1 or secp521r1) are
considered as different parameters of a single "ECDSA" algorithm, so it
is not presently possible to configure keys for more than one ECDSA
curve. 


 RSA is still the most widely supported algorithm. Presently (late
2018), ECDSA support is common, but not yet universal, and Ed25519 and
Ed448 support is mostly absent. Therefore, an RSA key should generally
be configured, along with any additional keys for the other algorithms
when desired. 



Example (separate files for each key and corresponding certificate chain):




> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     smtpd\_tls\_chain\_files =
>         ${config\_directory}/ed25519.pem,
>         ${config\_directory}/ed448.pem,
>         ${config\_directory}/rsa.pem
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/ed25519.pem:
>     -----BEGIN PRIVATE KEY-----
>     MC4CAQAwBQYDK2VwBCIEIEJfbbO4BgBQGBg9NAbIJaDBqZb4bC4cOkjtAH+Efbz3
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIBKzCB3qADAgECAhQaw+rflRreYuUZBp0HuNn/e5rMZDAFBgMrZXAwFDESMBAG
>     ...
>     nC0egv51YPDWxEHom4QA
>     -----END CERTIFICATE-----
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/ed448.pem:
>     -----BEGIN PRIVATE KEY-----
>     MEcCAQAwBQYDK2VxBDsEOQf+m0P+G0qi+NZ0RolyeiE5zdlPQR8h8y4jByBifpIe
>     LNler7nzHQJ1SLcOiXFHXlxp/84VZuh32A==
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIBdjCB96ADAgECAhQSv4oP972KypOZPNPF4fmsiQoRHzAFBgMrZXEwFDESMBAG
>     ...
>     pQcWsx+4J29e6YWH3Cy/CdUaexKP4RPCZDrPX7bk5C2BQ+eeYOxyThMA
>     -----END CERTIFICATE-----
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/rsa.pem:
>     -----BEGIN PRIVATE KEY-----
>     MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDc4QusgkahH9rL
>     ...
>     ahQkZ3+krcaJvDSMgvu0tDc=
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIC+DCCAeCgAwIBAgIUIUkrbk1GAemPCT8i9wKsTGDH7HswDQYJKoZIhvcNAQEL
>     ...
>     Rirz15HGVNTK8wzFd+nulPzwUo6dH2IU8KazmyRi7OGvpyrMlm15TRE2oyE=
>     -----END CERTIFICATE-----
> 
> ```
> 
> 



Example (all keys and certificates in a single file):




> 
> 
> ```
> 
> /etc/postfix/main.cf:
>     smtpd\_tls\_chain\_files = ${config\_directory}/chains.pem
> 
> ```
> 
> 



> 
> 
> ```
> 
> /etc/postfix/chains.pem:
>     -----BEGIN PRIVATE KEY-----
>     MC4CAQAwBQYDK2VwBCIEIEJfbbO4BgBQGBg9NAbIJaDBqZb4bC4cOkjtAH+Efbz3
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIBKzCB3qADAgECAhQaw+rflRreYuUZBp0HuNn/e5rMZDAFBgMrZXAwFDESMBAG
>     ...
>     nC0egv51YPDWxEHom4QA
>     -----END CERTIFICATE-----
>     -----BEGIN PRIVATE KEY-----
>     MEcCAQAwBQYDK2VxBDsEOQf+m0P+G0qi+NZ0RolyeiE5zdlPQR8h8y4jByBifpIe
>     LNler7nzHQJ1SLcOiXFHXlxp/84VZuh32A==
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIBdjCB96ADAgECAhQSv4oP972KypOZPNPF4fmsiQoRHzAFBgMrZXEwFDESMBAG
>     ...
>     pQcWsx+4J29e6YWH3Cy/CdUaexKP4RPCZDrPX7bk5C2BQ+eeYOxyThMA
>     -----END CERTIFICATE-----
>     -----BEGIN PRIVATE KEY-----
>     MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDc4QusgkahH9rL
>     ...
>     ahQkZ3+krcaJvDSMgvu0tDc=
>     -----END PRIVATE KEY-----
>     -----BEGIN CERTIFICATE-----
>     MIIC+DCCAeCgAwIBAgIUIUkrbk1GAemPCT8i9wKsTGDH7HswDQYJKoZIhvcNAQEL
>     ...
>     Rirz15HGVNTK8wzFd+nulPzwUo6dH2IU8KazmyRi7OGvpyrMlm15TRE2oyE=
>     -----END CERTIFICATE-----
> 
> ```
> 
> 


 This feature is available in Postfix 3.4 and later. 


