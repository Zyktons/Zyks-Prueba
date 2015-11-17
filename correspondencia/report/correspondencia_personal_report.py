# -*- encoding: utf-8 -*-

from openerp.osv import osv
import time
from openerp.report import report_sxw
from datetime import datetime

class correspondencia_personal_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(correspondencia_personal_report,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'time': time,
            'get_data': self.get_data,
            'get_data_personal_vieja': self.get_data_personal_vieja,
        })
        self.context = context
    

    def get_data(self, date_start, date_end):
        personal_obj = self.pool.get('correspondencia.personal')
        tids = personal_obj.search(self.cr, self.uid, [('fecha_ingreso', '>=', date_start), ('fecha_firma', '<=', date_end)])
        res = personal_obj.browse(self.cr, self.uid, tids)
        return res
        
    def get_data_personal_vieja(self, date_start, date_end):
        corres_gestion_pres_obj=self.pool.get('correspondencia.gestion.presidencia')
        corres_gestion_pres_ids=corres_gestion_pres_obj.search(self.cr,self.uid,[('fecha_ingreso', '>=', date_start), ('fecha_firma', '<=', date_end),('is_personal','=',True)])
        res = corres_gestion_pres_obj.browse(self.cr, self.uid, corres_gestion_pres_ids)
        return res

class report_correspondencia_personal(osv.AbstractModel):
    _name = "report.correspondencia.id_personal_report_qweb"
    _inherit = "report.abstract_report"
    _template = "correspondencia.id_personal_report_qweb"
    _wrapped_report_class = correspondencia_personal_report
        

# report_sxw.report_sxw('correspondencia.models', 'correspondencia.personal', 'correspondencia/report/id_correspondencia_personal_report_qweb.rml',parser=correspondencia_personal_report)
