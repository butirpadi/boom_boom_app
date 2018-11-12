from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class ProductCategory(models.Model):
    _inherit = "product.category"
    
    @api.multi
    def unlink(self):
        for prodCat in self:
            print('Delete -> '  + prodCat.name)
            if prodCat.name == 'Tiket' or prodCat.name == 'Wahana' or prodCat.name == 'Tenant':
                raise UserError(_('You cannot delete this data.')) 
            
        return super(ProductCategory, self).unlink()
