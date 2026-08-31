def validate_transaction(transaction):
	errors = []
	required_fields = ["transaction_id", "amount", "currency", "sender_account", "receiver_account", "merchant_zip"]
	for field in required_fields:
		if field not in transaction:
			errors.append(f"missing required field: {field}")
	if "amount" in transaction and transaction["amount"] <=0:
		errors.append("amount must be greater than zero")
	if "merchant_zip" in transaction and not (len(transaction["merchant_zip"]) == 5 and transaction["merchant_zip"].isdigit()):
		errors.append("invalid merchant zip")
	if "sender_account" in transaction and "receiver_account"in transaction and transaction["sender_account"] == transaction["receiver_account"]:
		errors.append("sender and receiver account numbers match")
	if "currency" in transaction and transaction["currency"] not in ["USD", "GBP", "EUR", "JPY", "CAD", "AUD"]:
		errors.append("currency type invalid")
	if "sender_account" in transaction and not (transaction["sender_account"][:3].isalpha() and transaction["sender_account"][3:].isdigit()):
		errors.append("sender account number is invalid")
	if "receiver_account" in transaction and not (transaction["receiver_account"][:3].isalpha() and transaction["receiver_account"][3:].isdigit()):
		errors.append("receiver account number is invalid")
	if errors:
		raise ValueError(",".join(errors))
	return True

good_transaction = {
    "transaction_id": "NC12345",
    "amount": 20.00,
    "currency": "USD",
    "sender_account": "ACC123",
    "receiver_account": "ACC456",
    "merchant_zip": "12345",
}

bad_transaction_amount= {
    "transaction_id": "NC12346",
    "amount": -5,
    "currency": "USD",
    "sender_account": "ACC123",
    "receiver_account": "ACC456",
    "merchant_zip": "12345"
}

bad_transaction_merchant_zip_digits= {
    "transaction_id": "NC12347",
    "amount": 20.00,
    "currency": "USD",
    "sender_account": "ACC123",
    "receiver_account": "ACC456",
    "merchant_zip": "1235",
}

bad_transaction_merchant_zip_is_digit= {
    "transaction_id": "NC12348",
    "amount": 20.00,
    "currency": "USD",
    "sender_account": "ACC123",
    "receiver_account": "ACC123",
    "merchant_zip": "1234X",
}

bad_transaction_dual_error_amount_zip= {
    "transaction_id": "NC12349",
    "amount": 0,
    "currency": "USD",
    "sender_account": "ACC123",
    "receiver_account": "ACC456",
    "merchant_zip": "1245",
}

bad_transaction_all_fields_error= {
    "transaction_id": "NC22345",
    "amount": 0,
    "currency": "BAT",
    "sender_account": "A1C1B3",
    "receiver_account": "A2C4A6",
    "merchant_zip": "1245",
}
transactions = [good_transaction, bad_transaction_amount, bad_transaction_merchant_zip_digits, bad_transaction_merchant_zip_is_digit, bad_transaction_dual_error_amount_zip, bad_transaction_all_fields_error]

for transaction in transactions:
    try:
        validate_transaction(transaction)
        print(f"Transaction {transaction['transaction_id']} approved")
    except ValueError as error:
        print(f"Transaction {transaction['transaction_id']} rejected: {error}")

