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

* Python 3.9 o superior
* PyGame

---

## Instalación y ejecución

1. Instalar PyGame:

<pre class="overflow-visible! px-0!" data-start="3166" data-end="3196"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install pygame
</span></span></code></div></div></pre>

2. Ejecutar el juego desde la carpeta raíz del proyecto:

<pre class="overflow-visible! px-0!" data-start="3256" data-end="3282"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py</span></span></code></div></div></pre>

---

## Recursos gráficos

Los sprites utilizados en este proyecto provienen de recursos **free** disponibles públicamente en el sitio  **CraftPix** :

* [https://craftpix.net](https://craftpix.net)

Los assets gráficos se utilizan únicamente con fines educativos y demostrativos dentro del contexto de esta prueba técnica, respetando las condiciones de uso de los recursos gratuitos proporcionados por el sitio.

---
