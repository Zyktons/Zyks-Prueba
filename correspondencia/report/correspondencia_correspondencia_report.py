# -*- encoding: utf-8 -*-

from openerp.osv import osv
import time
from openerp.report import report_sxw
from datetime import datetime

class correspondencia_correspondencia_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(correspondencia_correspondencia_report,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'time': time,
            
        
        })
        self.context = context


class report_correspondencia_correspondencia(osv.AbstractModel):
    _name = "report.correspondencia.id_correspondencia_report_qweb"
    _inherit = "report.abstract_report"
    _template = "correspondencia.id_correspondencia_report_qweb"
    _wrapped_report_class = correspondencia_correspondencia_report
        

# report_sxw.report_sxw('correspondencia.models', 'correspondencia.correspondencia', 'correspondencia/report/id_correspondencia_correspondencia_report_qweb.rml',parser=correspondencia_correspondencia_report)
