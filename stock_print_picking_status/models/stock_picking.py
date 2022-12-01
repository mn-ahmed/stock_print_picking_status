# Copyright 2021-2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    printed = fields.Boolean(tracking=True)



