
WIDTH = 1600
HEIGHT = 900
FPS = 60

PLAYER_SPEED = 5
BULLET_SPEED = 8

ENEMY_SPEEDS = {
    "basic": 3,
    "fast": 5,
    "tank": 2
}

ENEMY_HEALTH = {
    "basic": 1,
    "fast": 1,
    "tank": 3
}


SPAWN_RATE = {
    "easy":    {"basic": 0.8, "fast": 0.15, "tank": 0.05},
    "normal":  {"basic": 0.6, "fast": 0.25, "tank": 0.15},
    "hard":    {"basic": 0.4, "fast": 0.35, "tank": 0.25}
}

SCORE_TIME_MULT = 1

SCORE_KILL = {
    "basic": 10,
    "fast": 20,
    "tank": 30
}

DIFFICULTY_SETTINGS = {
    "easy": {
        "spawn_delay": 90,
        "enemy_speed_mult": 1.0,
        "max_enemies": 4
    },
    "normal": {
        "spawn_delay": 60,
        "enemy_speed_mult": 1.2,
        "max_enemies": 6
    },
    "hard": {
        "spawn_delay": 35,
        "enemy_speed_mult": 1.5,
        "max_enemies": 8
    }
}
