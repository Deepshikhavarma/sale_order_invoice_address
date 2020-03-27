# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customer = fields.Boolean(string="Customer")
    invoice_address = fields.Boolean(string="Invoice Address")
    delivery_address = fields.Boolean(string="Delivery Address")


    @api.model
    def get_values(self):
        res = super(SaleConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            customer=(get_param('sale_order_invoice_address.customer')),
            invoice_address = get_param('sale_order_invoice_address.invoice_address'),
            delivery_address=get_param('sale_order_invoice_address.delivery_address'),
        )
        return res


    @api.multi
    def set_values(self):
        super(SaleConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        # we store the repr of the values, since the value of the parameter is a required string
        set_param('sale_order_invoice_address.customer', self.customer)
        set_param('sale_order_invoice_address.invoice_address', self.invoice_address)
        set_param('sale_order_invoice_address.delivery_address', self.delivery_address)



# class SaleOrder(models.Model):
# 	_inherit = 'sale.order'


# 	@api.onchange('')

