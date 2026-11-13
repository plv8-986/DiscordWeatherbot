import discord
import requests
import pyttsx3
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def start(ctx):
    await ctx.send("Hello! I'm a weather bot. to know your locations weather or to know another location's weather, use the command !weather <city>")

def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(base_url)
    if response.status_code ==200:
        return response.text.strip()
    else:
        return "Sorry, I can't fetch the weather information right now. Please try again later :("
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 125)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

@bot.command()
async def weather(ctx,*,city:str):
    weather_info = get_weather(city)
    await ctx.send(weather_info)
    speak(weather_info)

bot.run("put your token here gng")
