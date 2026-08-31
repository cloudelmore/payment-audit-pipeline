Collect-all validation, not fail-fast. Every rule runs regardless of earlier failures; all problems reported in one ValueError. 
Chosen because this is an audit-focused system — an assessor needs proof every field was checked, not just the first failure found.
Missing required fields are checked first, and every other rule is guarded with an "x" in transaction check. 
Prevents a KeyError crash when a field is absent, while still allowing collect-all behavior — a missing field doesn't block other fields from being validated too.

Account number format validated as letter-prefix + digits, not a fixed total length. 
Deliberately avoids assuming all accounts are the same length, since there was no real basis for picking one number.


CVV is never stored in the transaction structure. PCI DSS prohibits storing CVV after authorization; card_details is a placeholder for a tokenized reference, not raw card data.

merchant_zip stored as a string, not a number. 
Preserves leading zeros (e.g. Boston-area ZIPs); also currently assumes 5-digit US ZIP format only — worth flagging as a scope limitation if this project ever needed to handle international merchants.
