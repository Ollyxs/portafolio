# Lucas Ollarce - Portafolio Personal

Portafolio personal web interactivo construido enteramente en **Python** utilizando el framework [Reflex](https://reflex.dev/).

**URL en vivo:** [https://ollyxs.com.ar](https://ollyxs.com.ar)

## Tecnologías

* **Backend & Frontend:** Reflex (Python puro)
* **Estilos:** Radix Themes / CSS in JS
* **Despliegue:** GitHub Pages

## Modificaciones Técnicas

Este proyecto toma como base una plantilla inicial, sobre la cual realicé los siguientes trabajos de ingeniería y adaptación:

* Migración de Infraestructura (CI/CD): Migración del sistema de despliegue original de Vercel hacia GitHub Pages, implementando automatización de flujos de trabajo (GitHub Actions) para la construcción estática del proyecto.
* **Migración y Refactorización:** Actualización del código base para garantizar la compatibilidad con la última versión de Reflex.
* **Customización de UI/UX:** Adaptación de componentes visuales, colores y estructura para alinearlos a mi marca personal.
* **Optimización:** Limpieza de dependencias y adaptación del contenido estático para mejorar la velocidad de carga.

## Despliegue

El proyecto utiliza **GitHub Pages** como hosting de recursos estáticos.

Se configura el despliegue automático desde el archivo de GitHub Actions [.github/workflows/config.yml](./.github/workflows/config.yml) y [build.sh](./build.sh).

El proyecto se despliega automáticamente en la rama principal tras cada push.

## Despliegue Local

Si querés correr este proyecto en tu entorno local:

1. Cloná el repositorio:

  ```bash
    git clone https://github.com/Ollyxs/portafolio.git
  ```

1. Creá un entorno virtual e instalá las dependencias:

  ```bash
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

1. Inicializá y corré Reflex:

  ```bash
  reflex init
  reflex run
```

## Créditos

Construido a partir de una plantilla original de [MoureDev](https://github.com/mouredev/portafolio-template), refactorizada y mantenida por Lucas Ollarce.
