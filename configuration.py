# This file is part product_ean13_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'product.configuration'
    ean13_sequence = fields.Many2One('ir.sequence',
        'EAN13 Sequence', required=True,
        domain=[
            ('code', '=', 'product.product'),
            ])
