from flectra import api, fields, models
from flectra.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
from pprint import pprint


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    only_member = fields.Boolean('Only for Member', default=False)
    is_ticket = fields.Boolean('is ticket', default=False)
    is_wahana = fields.Boolean('is wahana', default=False)
    is_tenant = fields.Boolean('is tenant', default=False)
#     wahana_id = fields.Many2one('wahana', string="Wahana")

    @api.model
    def create(self, vals):        
        tiket_id = self.env['product.category'].search([('name','=',self.env.context.get('tipe'))]).id
        vals['categ_id'] = tiket_id

        result = super(ProductTemplate, self).create(vals)
        return result
     