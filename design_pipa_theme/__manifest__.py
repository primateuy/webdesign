{
	'name': 'Design Pipa Theme',
	'version': '19.0.3.0.0',
	'author': 'PrimateUY',
	'website': 'https://primate.uy',
	'category': 'Theme/Corporate',
	'license': 'AGPL-3',
	'summary': """
		Tema visual para el sitio web de Design Pipa.
		""",
	'description': """
		Módulo de tema para el sitio web de Design Pipa, agencia de comunicación,
		diseño y producción gráfica con base en Praia da Pipa, RN, Brasil.

		Al instalarse crea automáticamente una página nueva en /design-pipa
		sin modificar ninguna página existente del sitio.

		La página es una one-page con navegación interna fija (sticky) y
		tres secciones con anclas: #inicio, #produtos-servicos, #assessoria.

		Supuestos:
		- Requiere el módulo 'website' instalado.
		- Las imágenes placeholder deben reemplazarse con imágenes reales
		  de Design Pipa desde el editor visual (no requiere código).
		- Las fuentes son provisorias (Google Fonts). Reemplazar en
		  static/src/scss/theme.scss cuando Agus confirme las originales.
		""",
	'depends': [
		'website',
	],
	'data': [
		# GRUPOS
		# ROLES
		# IR.MODEL.ACCESS.CSV
		# VISTAS
		'views/snippets.xml',
		# MENU
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
