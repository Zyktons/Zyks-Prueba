# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
from openerp.osv import fields
from openerp.osv import osv
from openerp.tools import config
import time
from openerp.report import report_sxw



class  correspondencia_administracion__report_wizard(osv.TransientModel):
    _name = 'correspondencia_administracion.report.wizard'
    _columns = {
        'date_start': fields.datetime('Start Date', required=True),
        'date_end': fields.datetime('End Date', required=True),
    }

    def print_report(self, cr, uid, ids, context=None):
        values = {
            'ids': ids,
            'model': 'correspondencia.administracion',
            'form': self.read(cr, uid, ids, context=context)[0]
        }
        return self.pool['report'].get_action(cr, uid, [], 'correspondencia.id_administracion_report_qweb', data=values, context=context)
