{
	'name': 'Design Pipa Theme',
	'version': '19.0.4.0.0',
	'author': 'PrimateUY',
	'website': 'https://primate.uy',
	'category': 'Theme/Corporate',
	'license': 'AGPL-3',
	'summary': """
		Tema visual para el sitio web de Design Pipa.
		""",
	'description': """
		Landing page one-page de Design Pipa, agencia de comunicación,
		diseño y producción gráfica con base en Praia da Pipa, RN, Brasil.

		Fuentes: Helvetica (regular/bold/oblique/light) + Handflair (manuscrita).
		Secciones: Hero, Por qué, Destaque, Servicios, Portfolio (3+4), Produção Gráfica, Brand Manager.
		""",
	'depends': ['website'],
	'data': [
		'views/snippets.xml',
	],
	'assets': {
		'web.assets_frontend': [
			'design_pipa_theme/static/src/scss/theme.scss',
		],
	},
	'auto_install': False,
	'installable': True,
	'application': False,
}
