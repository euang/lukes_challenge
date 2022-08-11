# milter_macro_defaults (default: empty)
 Optional list of *name=value* pairs that specify default
values for arbitrary macros that Postfix may send to Milter
applications. These defaults are used when there is no corresponding
information from the message delivery context. 


 Specify *name=value* or *{name=value}* pairs separated
by comma or whitespace. Enclose a pair in "{}" when a value contains
comma or whitespace (this form ignores whitespace after the enclosing
"{", around the "=", and before the enclosing "}"). 


 This feature is available in Postfix 3.1 and later. 


