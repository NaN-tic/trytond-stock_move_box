# This file is part of the stock_move_box module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['ShipmentIn', 'ShipmentOut', 'ShipmentOutReturn']


class ShipmentIn():
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.in'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        move = super(ShipmentIn, cls)._get_inventory_moves(incoming_move)
        if not move:
            return
        move.box = incoming_move.box
        return move


class ShipmentOut():
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out'

    def _get_inventory_move(self, move):
        inventory_move = super(ShipmentOut, self)._get_inventory_move(move)
        inventory_move.box = move.box
        return inventory_move


class ShipmentOutReturn():
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        move = super(ShipmentOutReturn,
            cls)._get_inventory_moves(incoming_move)
        if not move:
            return
        move.box = incoming_move.box
        return move
