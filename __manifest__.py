# super_stock/__manifest__.py
{
    "name": "Super Stock",
    "version": "17.0.1.0",
    "summary": "Gestion de stock, catégories, seuils d’alerte, entrées/sorties et rapport PDF",
    "category": "Inventory",
    "author": "Aristide MIBO",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/super_stock_security.xml",
        "security/ir.model.access.csv",
        "data/stock_category_data.xml",
        "data/stock_cron_alert.xml",
        "views/stock_category_views.xml",
        "views/stock_product_views.xml",
        "views/stock_move_views.xml",
        "report/stock_move_report.xml",
        "report/stock_move_report_templates.xml",
    ],
    "application": True,
}
