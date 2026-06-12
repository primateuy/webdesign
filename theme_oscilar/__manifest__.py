{
    'name': 'Theme Oscilar para Existir',
    'version': '18.0.1.0.0',
    'author': 'PrimateUY',
    'website': 'https://github.com/primateuy/WMS/',
    'category': 'Theme/Creative',
    'license': 'AGPL-3',
    'summary': """
        Tema editorial para el blog Oscilar para Existir
    """,
    'description': """
        Tema completo para el sitio web Oscilar para Existir.

        Incluye diseño editorial para el blog (listado y post individual),
        header y footer personalizados con la identidad visual de la marca.

        Paleta de color:
        - Navy:   #0D2137 (fondos, header, footer)
        - Naranja: #E8621A (acento, CTA, énfasis)
        - Crema:  #FBF6EF (fondo de contenido)
        - Tinta:  #2D1F0E (texto cuerpo)

        Tipografía editorial: Lora (titulares y cuerpo) + Inter (UI funcional).
    """,
    'depends': ['website', 'website_blog'],
    'data': [
        'views/layout_templates.xml',
        'views/blog_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'theme_oscilar/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_frontend': [
            'theme_oscilar/static/src/scss/theme.scss',
        ],
    },
    'auto_install': False,
    'installable': True,
    'application': False,
}
