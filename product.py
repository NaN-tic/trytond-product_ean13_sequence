# This file is part product_ean13_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    __name__ = 'product.product'

    @classmethod
    def get_new_ean13(cls):
        pool = Pool()
        Config = pool.get('product.configuration')
        Sequence = pool.get('ir.sequence')
        config = Config(1)
        sequence = config.ean13_sequence.id
        ean = Sequence.get_id(sequence)
        checksum = 0
        for i, digit in enumerate(reversed(ean)):
            checksum += int(digit) * 3 if (i % 2 == 0) else int(digit)
        return ean + str((10 - (checksum % 10)) % 10)

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]
        for values in vlist:
            skip = False
            if values.get('codes'):
                for action, codes in values.get('codes'):
                    if action == 'create':
                        for code in codes:
                            if code['barcode'] == 'EAN13':
                                skip = True
                                break
                        else:
                            codes.append({
                                    'barcode': 'EAN13',
                                    'number': cls.get_new_ean13(),
                                    'active': True,
                                    })
                            skip = True
                            break
            if not skip:
                values['codes'] = [
                    ('create', [{
                                'barcode': 'EAN13',
                                'number': cls.get_new_ean13(),
                                'active': True,
                                }]),
                    ]
        return super(Product, cls).create(vlist)
