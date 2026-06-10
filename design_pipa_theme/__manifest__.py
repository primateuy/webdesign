{
	'name': 'Design Pipa Theme',
	'version': '19.0.1.0.0',
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

		Incluye:
		- Snippets personalizados para cada sección de la landing page
		- Estilos propios (tipografía, colores, layout)
		- Soporte bilingüe portugués / español vía sistema de traducciones de Odoo
		- Imágenes placeholder listas para reemplazar desde el builder visual

		Supuestos:
		- Requiere el módulo 'website' de Odoo instalado
		- Las páginas del menú (Sobre, Serviços, Produtos, Assessorias, Donde estamos)
		  deben crearse manualmente desde el backend de Website
		- Las imágenes placeholder deben reemplazarse con las imágenes reales
		  de Design Pipa desde el editor visual (no requiere código)
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
		'views/assets.xml',
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
