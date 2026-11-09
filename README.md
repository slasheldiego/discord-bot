# Discord Bot

Bot de Discord construido con [discord.js](https://discord.js.org) v14 y Node.js 20+.

## Requisitos

- Node.js 20 o superior
- Una aplicación creada en el [Discord Developer Portal](https://discord.com/developers/applications)

## Configuración

1. Instala las dependencias:
   ```bash
   npm install
   ```
2. Copia el archivo de ejemplo y completa tus credenciales:
   ```bash
   cp .env.example .env
   ```
3. Invita el bot a tu servidor (Developer Portal → OAuth2 → URL Generator, scopes `bot` y `applications.commands`).
4. Registra los slash commands:
   ```bash
   npm run deploy
   ```
   Con `GUILD_ID` definido se registran al instante en ese servidor; sin él, se registran globalmente (puede tardar hasta 1 hora).
5. Inicia el bot:
   ```bash
   npm start      # producción
   npm run dev    # recarga automática al guardar
   ```

## Estructura

```
src/
├── index.js            # Punto de entrada: cliente y manejo de interacciones
├── config.js           # Carga y valida variables de entorno
├── loadCommands.js     # Carga dinámica de comandos desde src/commands
├── deploy-commands.js  # Registra los slash commands en Discord
└── commands/
    └── ping.js         # /ping
```

## Agregar un comando

Crea un archivo en `src/commands/` que exporte `data` (un `SlashCommandBuilder`) y `execute(interaction)`, luego ejecuta `npm run deploy`.
