import { readdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const commandsDir = path.join(path.dirname(fileURLToPath(import.meta.url)), 'commands');

export async function loadCommands() {
  const files = (await readdir(commandsDir)).filter((f) => f.endsWith('.js'));
  const commands = [];
  for (const file of files) {
    const mod = await import(pathToFileURL(path.join(commandsDir, file)).href);
    if (mod.data && mod.execute) commands.push(mod);
    else console.warn(`[comandos] ${file} no exporta "data" y "execute"; se omite.`);
  }
  return commands;
}
