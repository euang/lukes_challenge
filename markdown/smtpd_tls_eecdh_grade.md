# smtpd_tls_eecdh_grade (default: see "postconf -d" output)
 The Postfix SMTP server security grade for ephemeral elliptic-curve
Diffie-Hellman (EECDH) key exchange. As of Postfix 3.6, the value of
this parameter is always ignored, and Postfix behaves as though the
**auto** value (described below) was chosen.



 The available choices are: 



**auto**  Use the most preferred curve that is
supported by both the client and the server. This setting requires
Postfix ≥ 3.2 compiled and linked with OpenSSL ≥ 1.0.2. This
is the default setting under the above conditions (and the only
setting used with Postfix ≥ 3.6). 
**none**  Don't use EECDH. Ciphers based on EECDH key
exchange will be disabled. This is the default in Postfix versions
2.6 and 2.7. 
**strong**  Use EECDH with approximately 128 bits of
security at a reasonable computational cost. This is the default in
Postfix versions 2.8–3.5. 
**ultra**  Use EECDH with approximately 192 bits of
security at computational cost that is approximately twice as high
as 128 bit strength ECC. 

 If you want to take maximal advantage of ciphers that offer forward secrecy see
the Getting
started section of FORWARD\_SECRECY\_README. The
full document conveniently presents all information about Postfix
"perfect" forward secrecy support in one place: what forward secrecy
is, how to tweak settings, and what you can expect to see when
Postfix uses ciphers with forward secrecy. 


 This feature is available in Postfix 2.6 and later, when it is
compiled and linked with OpenSSL 1.0.0 or later on platforms
where EC algorithms have not been disabled by the vendor. 


