# enable_idna2003_compatibility (default: no)
 Enable 'transitional' compatibility between IDNA2003 and IDNA2008,
when converting UTF-8 domain names to/from the ASCII form that is
used for DNS lookups. Specify "yes" for compatibility with Postfix
≤ 3.1 (not recommended). This affects the conversion of domain
names that contain for example the German sz and the Greek zeta.
See http://unicode.org/cldr/utility/idna.jsp for more examples.



 This feature is available in Postfix 3.2 and later. 


