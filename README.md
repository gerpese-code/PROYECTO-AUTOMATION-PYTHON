# 🚀 Framework de Automatización - SauceDemo con Playwright & Python

Este proyecto es un framework de pruebas automatizadas profesional desarrollado para la plataforma **SauceDemo**. Implementa las mejores prácticas de la industria para garantizar que el proceso de compra de un usuario final sea fluido y libre de errores.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Herramienta de Automatización:** Playwright
* **Framework de Pruebas:** Pytest
* **Patrón de Diseño:** Page Object Model (POM)
* **CI/CD:** GitHub Actions
* **Reportes:** Capturas de pantalla automáticas (evidencias visuales)

## 🏗️ Estructura del Proyecto

* `pages/`: Contiene las clases de Page Object que encapsulan la lógica de la interfaz de usuario.
* `tests/`: Contiene los scripts de prueba que ejecutan los escenarios de negocio.
* `results/`: Carpeta donde se almacenan automáticamente las evidencias (screenshots) de cada ejecución.
* `.github/workflows/`: Configuración del pipeline de Integración Continua.

## 🧪 Escenarios Automatizados

1.  **Login Exitoso:** Validación de acceso con credenciales correctas.
2.  **Flujo de Carrito de Compras:**
    * Navegación al inventario.
    * Adición de productos al carrito (ej. Sauce Labs Backpack).
    * Validación en tiempo real del contador (badge) del carrito.

## 🚀 Ejecución en la Nube (CI/CD)

Este repositorio cuenta con un flujo de **GitHub Actions** configurado. Cada vez que se realiza un cambio en el código, el servidor:
1.  Instala las dependencias y navegadores.
2.  Ejecuta la suite de pruebas completa.
3.  Genera un reporte del estado de salud del proyecto (Check verde ✅).

## 📥 Instalación Local

Si deseas ejecutar las pruebas en tu máquina local:

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/gerpese-code/Proyecto-Automation-Python.git](https://github.com/gerpese-code/Proyecto-Automation-Python.git)