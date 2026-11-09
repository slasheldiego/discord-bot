import { SlashCommandBuilder } from 'discord.js';

export const data = new SlashCommandBuilder()
  .setName('ping')
  .setDescription('Responde con Pong! y la latencia del bot');

export async function execute(interaction) {
  const sent = await interaction.reply({ content: 'Pong!', fetchReply: true });
  const latency = sent.createdTimestamp - interaction.createdTimestamp;
  await interaction.editReply(`Pong! 🏓 Latencia: ${latency} ms · WebSocket: ${interaction.client.ws.ping} ms`);
}
