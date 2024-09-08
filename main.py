import os
import random
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents,)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync()

# Saluta te stesso
@tree.command(name="salutami", description="Saluta te stesso")
async def salutami(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ciao, {interaction.user.name}!")


# Saluta utente specifico
@tree.command(name="saluta", description="Saluta un utente specifico")
async def saluta(interaction: discord.Interaction, user: discord.Member):
    greetings = ["Ciao", "Salve", "Hola", "Bonjour"]
    random_greeting = random.choice(greetings)
    await interaction.response.send_message(f"{random_greeting}, {user.name}!")


# Randomnick
@tree.command(name="randomnick",
              description="Cambia il tuo nickname in modo random")
async def randomnick(interaction: discord.Interaction):
    nicknames = [
        "Containment Breach",
        "Sono un furry",
        "Francese DOC",
        "Sebastian",
        "Pandemonium",
        "IKEA Employee",
        "Mario",
        "Waluigi",
        "Moroi",
        "Phantom",
        "Wraith",
        "Banshee",
        "Tua madre",
        "Sua madre",
        "Max Verstappen",
        "Lewis Hamilton",
        "Geolier",
        "Michael Jordan",
        "Lionel Messi",
        "The Spicy Meatball",
        "I Make Bread",
        "The One Who Eats Too Much",
        "Boomer",
        "Always Right",
        "Angry",
        "Scared Bozo",
        "Always Wrong",
        "Sleepyhead",
        "Happy Camper",
        "Sad Sack",
        "The Sculpture",
        "The Plague Doctor",
        "The Hard-to-Destroy Reptile",
        "The Old Man",
        "The Shy Guy",
        "Il Guardiano",
        "Erri Pottah",
        "Il Signore degli Anelli",
        "Bowser",
        "Regina delle Tenebre",
        "Terrone",
        "Koopaldo",
        "Shaddyy",
        "THE CALL IS DEEPING",
        "I am 11",
    ]

    random_nickname = random.choice(nicknames)
    await interaction.user.edit(nick=random_nickname)
    await interaction.response.send_message(
        f"Il tuo nuovo nickname è **{random_nickname}**!")


# Cercare su Wikipedia
@tree.command(name="wiki", description="Cerca su Wikipedia")
async def wiki(interaction: discord.Interaction, search_term: str):
    try:
        import wikipedia
        wikipedia.set_lang("it")
        result = wikipedia.summary(search_term, sentences=2)
        page = wikipedia.page(search_term)
        image_url = page.images[0] if page.images else None
        embed = discord.Embed(title=page.title, description=result)
        if image_url:
            embed.set_image(url=image_url)
        await interaction.response.send_message(embed=embed)
    except wikipedia.exceptions.PageError:
        await interaction.response.send_message(embed=discord.Embed(
            description="Non ho trovato nulla su Wikipedia."))
    except wikipedia.exceptions.DisambiguationError as e:
        await interaction.response.send_message(embed=discord.Embed(
            description=
            "Ho trovato più risultati per la tua ricerca. Specifica meglio."))


# Picker agenti Valorant
@tree.command(name="agente",
              description="Selezione random di agenti di Valorant")
async def agente(interaction: discord.Interaction):
    agenti = [
        "Jett", "Sova", "Sage", "Phoenix", "Cypher", "Raze", "Omen",
        "Breach", "Viper", "Killjoy", "Chamber", "Neon", "Yoru", "Fade",
        "Skye", "Harbor", "Astra", "KAY/O", "Deadlock", "Reyna", "Clove",
        "Iso"
    ]

    selected_agent = random.choice(agenti)
    await interaction.response.send_message(
        f"Il tuo agente selezionato è: **{selected_agent}**")


# # Aggiungi oggetti in una lista array
# @tree.command(name="lista", description="Mostra questo messaggio")
# async def lista(interaction: discord.Interaction, item: str):
#     lista = []
#     lista.append(item)
#     await interaction.response.send_message(embed=discord.Embed(
#         title="Lista:", description="\n".join(lista), color=discord.Color.red()))


# Picker mappe Valorant
@tree.command(name="mappa",
              description="Selezione random di mappe di Valorant")
async def mappa(interaction: discord.Interaction):
    mappa = [
        "Bind", "Split", "Haven", "Ascent", "Icebox", "Fracture", "Pearl",
        "Lotus", "Breeze"
    ]

    selected_agent = random.choice(mappa)
    await interaction.response.send_message(
        f"La mappa selezionata è: **{selected_agent}**")

# Picker armi Valorant
@tree.command(name="arma",
              description="Selezione random di armi di Valorant")
async def arma(interaction: discord.Interaction):
    arma = [
        "Classic", "Shorty", "Frenzy", "Ghost", "Sheriff", "Stinger", "Spectre",
        "Bucky", "Judge", "Bulldog", "Guadian", "Phantom", "Vandal", "Marshal",
        "Outlaw", "Operator"
    ]

    arma_random = random.choice(arma)
    await interaction.response.send_message(
        f"L'arma selezionata è: **{arma_random}**")

# Testa o croce
@tree.command(name="moneta", description="Testa o croce")
async def moneta(interaction: discord.Interaction):
    risultato = random.choice(["Testa", "Croce"])
    await interaction.response.send_message(
        f"Il risultato è: **{risultato}**")


# Comando Help
@tree.command(name="help", description="Mostra questo messaggio")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=discord.Embed(
        title="Comandi disponibili",
        description="Prefisso: / ",
        color=discord.Color.red()
    ).add_field(
        name="Divertimento",
        value="Salutami: Saluta te stesso\n"
        "Saluta [nome]: Saluta un utente specifico\n"
        "Randomnick: Cambia il tuo nickname in modo random\n",
        inline=False
    ).add_field(
        name="Valorant",
        value="Agente: Selezione random di agenti di Valorant\n"
        "Mappa: Selezione random di mappe di Valorant\n"
        "Arma: Selezione random di armi di Valorant",
        inline=False
    ).add_field(
        name="Altro",
        value="Wiki [argomento]: Cerca su Wikipedia\n"
        "Moneta: Testa o croce\n"
        "Help: Mostra questo messaggio",
        inline=False
    ).set_footer(
        text="Made by itsjustcri and defeatof13"
    ).set_image(
        url=
        "https://cdn.discordapp.com/attachments/1281142794261499918/1281229215211192374/Frame_1.png?ex=66daf530&is=66d9a3b0&hm=e67b7f23ad9afe940f66ae7bb4081f61f722faed68c34b17fd837b1e9028fab8&"
    ))


try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
