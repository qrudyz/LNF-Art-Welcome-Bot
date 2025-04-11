import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
ROLE_ID = int(os.getenv("ROLE_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} este online!")

@bot.event
async def on_member_join(member):
    if member.guild.id != GUILD_ID:
        return
    
    role = member.guild.get_role(ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
            print(f"A fost adăugat rolul {role.name} la {member}")
        except Exception as e:
            print(f"Eroare la atribuirea rolului: {e}")

    channel = member.guild.get_channel(CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="Welcome to LNF Art!",
            description=(
                f"Hello, {member.mention}! Welcome to the **LNF Art** server!\n\n"
                "**About Us**\n"
                "Welcome to LNF Art! We're glad to have you here.\n\n"
                "**Server Rules**\n"
                "Please make sure to read our server rules.\n\n"
                "**Get Started**\n"
                "Check out our channels and introduce yourself!"
            ),
            color=0x5865F2
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(
            text=f"We now have {member.guild.member_count} members!"
        )

        await channel.send(content=f"", embed=embed)

bot.run(TOKEN)