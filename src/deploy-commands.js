import { REST, Routes } from 'discord.js';
import { config } from './config.js';
import { loadCommands } from './loadCommands.js';

const body = (await loadCommands()).map((c) => c.data.toJSON());
const rest = new REST().setToken(config.token);

const route = config.guildId
  ? Routes.applicationGuildCommands(config.clientId, config.guildId)
  : Routes.applicationCommands(config.clientId);

await rest.put(route, { body });
console.log(`✅ ${body.length} comando(s) registrados ${config.guildId ? `en el servidor ${config.guildId}` : 'globalmente'}.`);
