# design_pipa_theme

Módulo de tema para el sitio web de **Design Pipa** — Odoo 19.0 Community.

---

## Instalación

1. Copiar la carpeta `design_pipa_theme` dentro del directorio `addons` de tu instancia Odoo.
2. Desde el backend de Odoo: **Aplicaciones → Actualizar lista de aplicaciones**.
3. Buscar "Design Pipa Theme" e instalar.
4. Ir a **Sitio Web → Ir al sitio web → Editar**.
5. En el panel lateral aparecerá la sección **"Design Pipa"** con los 7 snippets disponibles.

---

## Snippets disponibles

| Snippet | Descripción |
|---|---|
| DP — Hero | Sección principal con título y CTA |
| DP — Por qué Design Pipa | Texto + foto con cita manuscrita |
| DP — Destaque Internacional | Bloque negro "Se você não está no Brasil" |
| DP — Servicios | Lista de servicios + foto |
| DP — Portafolio Grid | Grilla 4×2 de imágenes |
| DP — Producción Gráfica | Lista de productos gráficos |
| DP — Brand Manager | CTA final con imagen de fondo |

---

## Imágenes a reemplazar

Todas las imágenes son **placeholders**. Desde el editor visual de Odoo
(sin tocar código) reemplazar:

| Placeholder | Dónde reemplazar | Proporción sugerida |
|---|---|---|
| `foto_agus.jpg` | Snippet "Por qué Design Pipa" | 3:4 vertical |
| `foto_servicios.jpg` | Snippet "Servicios" | 7:5 landscape |
| `portafolio_1..8.jpg` | Snippet "Portafolio Grid" | 1:1 cuadrado |
| `fondo_brand_manager.jpg` | Snippet "Brand Manager" (fondo) | 16:9 landscape |

---

## Idiomas

- **Portugués**: idioma base (textos en los templates).
- **Español**: archivo `i18n/es.po` incluido.

Para activar el español:
1. **Ajustes → Idiomas → Añadir idioma → Español**.
2. Odoo carga el `.po` automáticamente al instalar/actualizar el módulo.

---

## Fuentes (provisorias)

Las fuentes actuales son Google Fonts provisorias:

| Rol | Fuente actual | Reemplazar en |
|---|---|---|
| Títulos | Barlow Condensed | `static/src/scss/theme.scss` línea `$dp-font-title` |
| Cuerpo | Inter | `static/src/scss/theme.scss` línea `$dp-font-body` |
| Script/manuscrita | Dancing Script | `static/src/scss/theme.scss` línea `$dp-font-script` |

Cuando Agus confirme las fuentes originales, editar las tres variables
y el `@import` de Google Fonts al inicio del SCSS.

---

## Colores

| Variable | Valor actual | Uso |
|---|---|---|
| `$dp-black` | `#0a0a0a` | Fondos oscuros, texto |
| `$dp-white` | `#ffffff` | Texto sobre fondo oscuro |
| `$dp-gray-mid` | `#cccccc` | Texto secundario |
| `$dp-accent` | `#ffffff` | Pendiente confirmar con Agus |

---

## Links del menú

Los ítems del menú apuntan a páginas separadas de Odoo Website.
Crearlas desde **Sitio Web → Páginas → Nueva página**:

- Sobre o Estúdio
- Serviços
- Produtos
- Assessorias
- Donde estamos

---

## Historial de versiones

| Versión | Cambio |
|---|---|
| 19.0.1.0.0 | Versión inicial — 7 snippets, bilingüe PT/ES |
