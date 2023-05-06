import discord
from key import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} está online!')


@client.event
async def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return

    if l_conteudo.startswith('oi'):
        await message.channel.send(f'"Oi" o caralho {message.author}, teu merda 😡')

    if message.content.startswith('!status'):
        server_status = check_minecraft_server_status(
            'hHNUH08a5z.aternos.me:64049')
        if server_status == 'online':
            channel = discord.utils.get(message.guild.channels, name="geral")
            # problema
            await channel.send('O servidor de Minecraft está online!')
        else:
            channel = discord.utils.get(message.guild.channels, name="geral")
            await channel.send('O servidor de Minecraft está offline.')


def check_minecraft_server_status(server_address):
    # Lógica para verificar o status do servidor de Minecraft usando o endereço fornecido
    # Retorna 'online' se o servidor estiver online e 'offline' caso contrário
    return 'online'


client.run(TOKEN)
