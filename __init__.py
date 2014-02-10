# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .payment import *
from .party import *


def register():
    Pool.register(
        Journal,
        Group,
        Party,
        module='account_payment_sepa_es', type_='model')
