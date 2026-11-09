# Discord Bot

Bot de Discord construido con [discord.py](https://discordpy.readthedocs.io) 2.x y Python 3.10+.

## Requisitos

- Python 3.10 o superior
- Una aplicación creada en el [Discord Developer Portal](https://discord.com/developers/applications)
  - En **Bot → Privileged Gateway Intents**, activa **Message Content Intent**

## Configuración

1. Crea y activa el entorno virtual, e instala las dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Crea un archivo `.env` en la raíz del proyecto (no se sube a GitHub):
   ```env
   DISCORD_TOKEN=tu_token_aqui
   # Opcional: ID de tu servidor para que los slash commands aparezcan al instante
   GUILD_ID=
   # Opcional: prefijo para comandos de texto (por defecto "!")
   COMMAND_PREFIX=!
   ```
3. Invita el bot a tu servidor (Developer Portal → OAuth2 → URL Generator, scopes `bot` y `applications.commands`).
4. Inicia el bot desde la raíz del proyecto:
   ```bash
   python -m src.bot
   ```

## Estructura

```
src/
├── bot.py        # Punto de entrada: crea el bot, carga cogs y sincroniza comandos
├── config.py     # Carga y valida las variables de .env
└── cogs/
    └── general.py  # /ping y !ping
```

## Agregar comandos

Crea un archivo en `src/cogs/` con una clase `commands.Cog` y una función `async def setup(bot)`. Se carga automáticamente al iniciar el bot. Usa `@commands.hybrid_command` para que el comando funcione como `/comando` y como `!comando`.
