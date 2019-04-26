SUPPLY CHAIN MANAGEMENT

In this module, CKG will play the part of Purchaser, and communicating with vendors using conventional methods, such as Phones and Emails.

1. CKG will create vendor(s) to send RFQ to. If they already exists, he will select from given vendor list.

2. CKG creates RFQ form, broadcasts email containing RFQ to selected vendors.

3. Vendors replies with CKG with their Quotes.
	3. a. CKG will manually enter the selected ones from those quotes for storage.

4. CKG will start negotiations, with selected vendors. This process will go through Quotation Revisions.

5. CKG will settle with a final Quotation with its revision. *Rejection to rest of the quotation will be handled manually? We will provide an option to automate this to some degree.*

6. Based upon the settled Quotation, auto-fill the Purchase Form for sending to the vendor.

	6. a. Facility of PO revision. *How should it be handled? What happens to the previous PO, on resending the revised PO.*

7. Delivery note along with physical goods are received.
	7. a. On entering the Delivery Form, stocks are INCREMENTED.

8. Rental cases: Will not be handled in Purchase/Supply Module

SALES MANAGEMENT

In thi module, CKG will play the part of Seller, and communication with clients occurs using conventional methods, such as Phones and Emails

1. CKG receives RFQ from clients (say via Email)

2. CKG creates a customer instance

3. Quotation Reply is created based on the RFQ received and stored; and auto reply to the client.

4. If PO is received, CKG creates a Sales Order Form.

5. Based on negotiation steps, SO may go through number of revisions.

6. Once the SO is acknowledged, the Delivery Note is created, and shipped with tangible goods.

7. If Rental Contract was made, Rental Contract is created and afterwards Delivery Note is created to be shipped. This will schedule a Collection Note, to send to client, once the rental period is over.

8. On collection, stock is increased.

SUPPLY CHAIN REPLACEMENT MODULE

1. In cases of damages, CKG receives replacement email.

2. CKG creates Delivery note referencing to the original Delivery note (one with faulty goods).

TERMS AND CONDITIONS OF RENTAL AGREEMENT OF CKG WILL CONTAIN

1. Extension Charges on specified or greater time delay

SALES AND SUPPLY MODULE WILL INTERACT DIRECTLY TO GIVEN COMMON ENTITIES

1. Stock
