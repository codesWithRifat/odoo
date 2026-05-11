{
    "name": "PDF Preview",
    "version": "19.0.1.1",
    "summary": "Preview PDF reports in Odoo file viewer instead of direct download in Odoo 19.",
    "depends": ["web"],
    "category": "Customizations",
    "author": "Softeko_Rifat",
    "assets": {
        "web.assets_backend": [
            "pdf_preview_19/static/src/js/pdf_preview.js",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
