# -*- coding: utf-8 -*-

from odoo import models, fields, api

class validation(models.Model):
    _name ="validation.validation"

    name = fields.Char(string="name")

    type_report = fields.Selection( [('cliente','Cliente'),('productoo','Producto'),('gasto','Producto con envio')], strting="Tipo de reporte" )
    partner_id = fields.Many2one('res.partner',string="Cliente")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status')
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('no', 'Nothing to Invoice')
        ], string='Invoice Status')
    type_category = fields.Many2one('product.category', string="Categoria de producto")
    

    @api.multi
    def reporte(self):
        self.ensure_one()
        if self.type_report:
            dom =[]
            title_sel = ""
            if self.type_report == 'cliente':
                dom = [('invoice_status','=','invoiced')]
                title_sel = ' por Cliente'
            
                tree_view_id = self.env.ref('sale.view_order_tree').id
                form_view_id = self.env.ref('sale.view_order_form').id
                # We pass `to_date` in the context so that `qty_available` will be computed across
                # moves until date.
                action = {
                    'type': 'ir.actions.act_window',
                    'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
                    'view_mode': 'tree,form',
                    'name':('Reporte' + str(title_sel)),
                    'res_model': 'sale.order',
                    #"'context': dict(self.env.context, to_date=self.date),
                    'domain':  dom
                    }
                return action

            elif self.type_report == 'productoo':
                dom = [('type','=','product')]
                title_sel = ' por Producto'

                tree_view_id = self.env.ref('product.product_template_tree_view').id
                form_view_id = self.env.ref('product.product_template_only_form_view').id
                # We pass `to_date` in the context so that `qty_available` will be computed across
                # moves until date.
                action = {
                    'type': 'ir.actions.act_window',
                    'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
                    'view_mode': 'tree,form',
                    'name':('Reporte' + str(title_sel)),
                    'res_model': 'product.template',
                    #"'context': dict(self.env.context, to_date=self.date),
                    'domain':  dom
                    }
                return action
            elif self.type_report =='gasto':
                dom = [('categ_id.property_cost_method', '=', 'fifo')]
                title_sel = ' por productos con gatos de envio' 

                tree_view_id = self.env.ref('stock_account.view_stock_product_tree2').id
                form_view_id = self.env.ref('product.product_template_only_form_view').id
                # We pass `to_date` in the context so that `qty_available` will be computed across
                # moves until date.
                action = {
                    'type': 'ir.actions.act_window',
                    'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
                    'view_mode': 'tree,form',
                    'name':('Reporte' + str(title_sel)),
                    'res_model': 'product.product',
                    #"'context': dict(self.env.context, to_date=self.date),
                    'domain':  dom
                    }
                return action    