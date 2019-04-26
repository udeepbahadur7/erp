from collections import namedtuple

PRIORITY = namedtuple("PRIORITY", "general new urgent")(*range(3))
REFERENCE = namedtuple("REFERENCE", "sales direct")(*range(2))
PAYMENT_MODE = namedtuple('PAYMENT_MODE', 'cash credit')(*range(2))
SALES_STATUS = namedtuple('SALES_STATUS', 'invoiced packed shipping halt delivered')(*range(5))
SALES_PERSON = namedtuple('SALES_PERSON', 'sales agent driver')(*range(3))
RENTAL = namedtuple("RENTAL", "monthly weekly daily")(*range(3))

PRIORITY_CHOICES = (
    (PRIORITY.general, "general"),
    (PRIORITY.new, "new"),
    (PRIORITY.urgent, "urgent"),
)
REFERENCE_CHOICES = (
    (REFERENCE.sales, "sales"),
    (REFERENCE.direct, "direct"),
)
PAYMENT_MODE_CHOICES = (
    (PAYMENT_MODE.cash, 'cash'),
    (PAYMENT_MODE.credit, 'credit'),
)
SALES_STATUS_CHOICES = (
    (SALES_STATUS.invoiced ,"invoiced"),
    (SALES_STATUS.packed ,"packed"),
    (SALES_STATUS.shipping ,"shipping"),
    (SALES_STATUS.halt ,"halt"),
    (SALES_STATUS.delivered ,"delivered"),
)
SALES_PERSON_CHOICES = (
    (SALES_PERSON.sales, 'sales'),
    (SALES_PERSON.agent, 'agent'),
    (SALES_PERSON.driver, 'driver')
)
RENTAL_CHOICES = (
        (RENTAL.monthly, "monthly"),
        (RENTAL.weekly, "weekly"),
        (RENTAL.daily, "daily"),
    )