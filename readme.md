# Shooter 2D en PyGame

## Descripción general

Este proyecto es un juego shooter 2D de desplazamiento lateral, desarrollado en Python utilizando exclusivamente la librería **PyGame**.
El jugador controla una nave ubicada en el lado izquierdo de la pantalla y debe sobrevivir el mayor tiempo posible mientras elimina enemigos que aparecen desde la derecha.

El proyecto fue desarrollado como una prueba técnica, priorizando una arquitectura clara, uso correcto de PyGame y mecánicas bien definidas.

---

## Características principales

- Shooter lateral 2D
- Menú principal con navegación
- Selección de dificultad
- Múltiples tipos de enemigos
- Sistema de puntaje y récord persistente
- Hitboxes personalizadas
- Dificultad progresiva y claramente diferenciada

---

## Controles

- Flecha arriba: mover jugador hacia arriba
- Flecha abajo: mover jugador hacia abajo
- Barra espaciadora: disparar
- Enter: confirmar selección en menús
- Escape / Enter: regresar al menú desde pantallas informativas

---

## Menús del juego

El juego cuenta con una estructura completa de menús:

1. **Menú principal**

   - Jugar
   - Mejor puntaje
2. **Menú de dificultad**

   - Fácil
   - Normal
   - Difícil
3. **Pantalla de mejor puntaje**

   - Muestra el récord guardado
4. **Pantalla de Game Over**

   - Muestra puntaje actual y récord
   - Permite volver al menú principal

---

## Sistema de dificultad

La dificultad seleccionada afecta múltiples aspectos del juego:

- Probabilidad de aparición de enemigos avanzados
- Frecuencia de aparición de enemigos
- Velocidad de los enemigos
- Número máximo de enemigos en pantalla
- Precisión de las hitboxes del jugador

Esto garantiza que el paso de una dificultad a otra sea claramente perceptible.

---

## Tipos de enemigos

El juego incluye tres tipos de enemigos:

- **Basic**Enemigo estándar, velocidad normal, un impacto para destruirlo.
- **Fast**Enemigo más rápido, un impacto para destruirlo.
- **Tank**
  Enemigo más grande visualmente, más lento, pero con mayor resistencia (requiere tres impactos).

Cada tipo de enemigo tiene comportamiento, velocidad y puntaje distintos.

---

## Sistema de puntaje

El puntaje del jugador se calcula a partir de:

- Tiempo sobrevivido
- Enemigos eliminados

El mejor puntaje se guarda de forma persistente en el archivo `highscore.txt` y se muestra tanto en el menú como en la pantalla de Game Over.

---

## Colisiones y hitboxes

Las colisiones no se basan directamente en el tamaño del sprite visual.Cada entidad (jugador, enemigos y balas) cuenta con una **hitbox personalizada**, lo que permite:

- Colisiones más justas
- Evitar problemas causados por transparencias en los sprites
- Ajustes específicos según dificultad y tipo de enemigo

Las colisiones se manejan mediante funciones personalizadas usando el parámetro `collided` de PyGame.

---

## Requisitos

- Python 3.9 – 3.11 (recomendado)
- pip actualizado
- pygame

> ⚠️ Nota: PyGame no es totalmente compatible con Python 3.12+ en Windows.

---

## Instalación y ejecución

1. Clonar el repositorio
2. Crear el entorno virtual (python 3.11 recomendado)
   `python -m venv .venv`

   `.venv\Scripts\activate`
3. Instalar PyGame:

   `pip install -r requirements.txt`
4. Ejecutar el juego ejecutando el archivo ***main.py***

---

## Recursos gráficos

Los sprites utilizados en este proyecto provienen de recursos **free** disponibles públicamente en el sitio  **CraftPix** :

* [https://craftpix.net](https://craftpix.net)

Los assets gráficos se utilizan únicamente con fines educativos y demostrativos dentro del contexto de esta prueba técnica, respetando las condiciones de uso de los recursos gratuitos proporcionados por el sitio.

---
