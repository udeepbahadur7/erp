from collections import namedtuple

PURCHASE_PRIORITY = namedtuple("PURCHASE_PRIORITY", "general urgent")(*range(2))
PAYMENT = namedtuple("PAYMENT", "cash_on_delivery prepaid due_days due_date_next_month due_end_of_month")(*range(5))
CREDIT_STATUS = namedtuple("CREDIT_STATUS", "notify_over hold_over always_halt")(*range(3))
