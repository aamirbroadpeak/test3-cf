from odoo import _, fields, models


class PurchseOrderReportWizard(models.TransientModel):
    _name = "purchase.order.report.wizard"
    _description = "Purchase Order Report Wizard"

    date_from = fields.Date("Date From", required=True)
    date_to = fields.Date("Date TO", required=True)

    def get_record(self):
        po_ids = self.env['purchase.order'].search([('invoice_status', '=', 'invoiced'), ('date_order', '>=', self.date_from),('date_order', '<=', self.date_to)])
        orders = []
        for rec in po_ids:
            list = []
            for record in rec.order_line:
                tax_am = 0
                for re in record.taxes_id:
                    tax_am += re.amount
                data = {
                    'name' : record.name,
                    'product_qty' : record.product_qty,
                    'price_unit': record.price_unit,
                    'qty_received': record.qty_received,
                    'tax': (tax_am / 100) * (record.price_unit * record.qty_received),
                    'amount': record.price_unit * record.qty_received,
                }
                list.append(data)
            orders.append((rec.name,list))
        return orders

    def action_print_report(self):
        data = {
            'forms_data': self.read()[0],
            'po_orders': self.get_record(),
        }
        return self.env.ref('oc_cf_customization.action_report_purchase_order_print').report_action(self, data=data)
