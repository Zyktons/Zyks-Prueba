# -*- coding: utf-8 -*-

{
    'name': "Correspondencia",
    'summary': "",
    'description': """
""",
    'author': "Jhonattan Martinez, Bertha Polo, Jesus Espinoza",
    'website': "",
    'category': '',
    'version': '1',
    'depends': ['base','report','mail','direccion_venezuela'],
    'data': [
        'views/correspondencia.xml',
        'security/correspondencia_security.xml',
        'security/group_admin_correspondencia/ir.model.access.csv',
        'security/group_correspondencia_correspondencia/ir.model.access.csv',
        'security/group_presidencia_correspondencia/ir.model.access.csv',
        'security/group_secretaria_correspondencia/ir.model.access.csv',
        'data/correspondencia.remitente.csv',
        'report/correspondencia_correspondencia_report.xml',
        
        'views/correspondencia_providencia_template.xml',
        'wizard/correspondencia_providencia_wizard.xml',
        'report/correspondencia_providencia_report.xml',
        
        'views/correspondencia_consultoria_template.xml',
        'wizard/correspondencia_consultoria_wizard.xml',
        'report/correspondencia_consultoria_report.xml',
        
        'views/correspondencia_ingresos_propios_template.xml',
        'wizard/correspondencia_ingresos_propios_wizard.xml',
        'report/correspondencia_ingresos_propios_report.xml',
        
        'views/correspondencia_personal_template.xml',
        'wizard/correspondencia_personal_wizard.xml',
        'report/correspondencia_personal_report.xml',
        
        'views/correspondencia_infraestructura_template.xml',
        'wizard/correspondencia_infraestructura_wizard.xml',
        'report/correspondencia_infraestructura_report.xml',
        
        'views/correspondencia_cheques_template.xml',
        'wizard/correspondencia_cheques_wizard.xml',
        'report/correspondencia_cheques_report.xml',
        
        'views/correspondencia_direccion_general_template.xml',
        'wizard/correspondencia_direccion_general_wizard.xml',
        'report/correspondencia_direccion_general_report.xml',
        
        #~ 'views/correspondencia_punto_cuenta_template.xml',
        #~ 'wizard/correspondencia_punto_cuenta_wizard.xml',
        #~ 'report/correspondencia_punto_cuenta_report.xml',
        
        'views/correspondencia_transferencia_template.xml',
        'wizard/correspondencia_transferencia_wizard.xml',
        'report/correspondencia_transferencia_repot.xml',
        
        'views/correspondencia_administracion_template.xml',
        'wizard/correspnondencia_administracion_wizar.xml',
        'report/correspondencia_administracion_report.xml',
        
        'views/correspondencia_auditoria_template.xml',
        'wizard/correspondencia_auditoria_wizar.xml',
        'report/correspondencia_auditoria_report.xml',
        
        'views/correspondencia_planificacion_template.xml',
        'wizard/correspondencia_planificacion_wizard.xml',
        'report/correspondemcia_planificacion_report.xml',
        
        'views/correspondencia_informatica_template.xml',
        'wizard/correspondencia_informatica_wizard.xml',
        'report/correspondencia_informatica_report.xml',
        
        'views/correspondencia_upe_template.xml',
        'wizard/correspondencia_upe_wizard.xml',
        'report/correspondenci_upe_report.xml',
        
        'views/correspondencia_correspondencia_template.xml',
        'views/correspondencia_sequence.xml',
    
    ],
    'tests': [
    ],
    'installable': True,
    'application': True,
}
