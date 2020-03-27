# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	invoice_address = fields.Many2many('res.partner',string="Invoice Address")
	delivery_address = fields.Many2many('res.partner',string="Delivery Address")

	@api.onchange('partner_id')
	def get_address(self):
		child_list = []
		config_setting = self.env['res.config.settings'].search([], limit=1, order="id desc")
		if self.partner_id.child_ids:
			child_list = [x.id for x in self.partner_id.child_ids]	
			if config_setting.customer == True:
				if config_setting.invoice_address == True:
					self.update({
					'invoice_address': [(6, 0, child_list)]})
				if config_setting.delivery_address == True:
					self.update({
					'delivery_address': [(6, 0, child_list)]})


