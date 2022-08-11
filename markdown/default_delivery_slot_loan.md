# default_delivery_slot_loan (default: 3)

The default value for transport-specific \_delivery\_slot\_loan
settings.




This parameter speeds up the moment when a message preemption can
happen. Instead of waiting until the full amount of delivery slots
required is available, the preemption can happen when
transport\_delivery\_slot\_discount percent of the required amount
plus transport\_delivery\_slot\_loan still remains to be accumulated.
Note that the full amount will still have to be accumulated before
another preemption can take place later.



 Use *transport*\_delivery\_slot\_loan to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.



