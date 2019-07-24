# -*- coding: utf-8 -*-
{
    'name': "Reporte_Avantec",

    'summary': """
        Reportes para mostar clientes con facturas calculando el total,margen,porcentaje de margen,aplica para productos y productos con envio""",
    'description': """
        Reportes para calcular margen porcentaje de margen 
    """,

    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reportes/reporte_avantec.xml',
        'reportes/reporte_avanet_tem.xml',
        'reportes/reporte_avantec_prod.xml',
        'reportes/reporte_avantec_prod_temp.xml',
        
        'reportes/reporte_envio.xml',
        'reportes/reporte_envio_tem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,

}