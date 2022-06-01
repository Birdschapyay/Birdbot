# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import random
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0
video = ["https://www.youtube.com/watch?v=gdEcQfAUggo&t=2s&ab_channel=FunnyVines", "https://www.youtube.com/watch?v=9QbL9c_XrtE&t=8s&ab_channel=ThePetCollective",
          "https://www.youtube.com/watch?v=zjIqSEJxiaU&ab_channel=ThePetCollective", "https://www.youtube.com/watch?v=JaNlkWEFo7g&ab_channel=PetsArena",
          "https://www.youtube.com/watch?v=dW2utwg9oOg&ab_channel=JustAww", "https://www.youtube.com/watch?v=Zn_y0iu_rIs&ab_channel=BlackFish",
          "https://www.youtube.com/watch?v=KE0k_Qn-fo0&ab_channel=BirdiesWorld", "https://www.youtube.com/watch?v=kiyocAooXmo&ab_channel=BirdiesWorld",
          "https://www.youtube.com/watch?v=fP7JfLWxz-Y&ab_channel=LaughTV", "https://www.youtube.com/watch?v=e1UloTQEiWc&ab_channel=BudgieWorld",
          "https://www.youtube.com/watch?v=U7jDVgw7SME&ab_channel=ShahistaSharoyKhan", "https://www.youtube.com/watch?v=MNadccrz0aA&ab_channel=ClaireBelbin",
          "https://www.youtube.com/watch?v=6MviIV9t4zU&ab_channel=ThePetCollective", "https://www.youtube.com/watch?v=K41IMe28zhg&ab_channel=RGreen",
          "https://www.youtube.com/watch?v=wO0vPzkkZag&ab_channel=BenPluimer", "https://www.youtube.com/watch?v=ePSUMnkXyJM&ab_channel=Spax",
          "https://www.youtube.com/watch?v=mzZ1N0UNb9E&ab_channel=ThePetCollective", "https://www.youtube.com/watch?v=Ea6dghBbIU8&t=1s&ab_channel=ALLBIRD",
          "https://www.youtube.com/watch?v=xH-FMD4lU6I&t=1s&ab_channel=JustAww", "https://www.youtube.com/watch?v=D1eaHtaal-Y&ab_channel=Newsflare",
          "https://www.youtube.com/watch?v=cgieNtydQPU&ab_channel=PetMate", "https://www.youtube.com/watch?v=JL6PaZt6BNs&ab_channel=CuteAnimalPlanet",
          "https://www.youtube.com/watch?v=68RKNJkarAM&ab_channel=FunnyPets", "https://www.youtube.com/watch?v=exIYiwbyJU4&ab_channel=EnglishFunnyClips",
          "https://www.youtube.com/watch?v=YE8PTMSFMUg&ab_channel=Cair", "https://www.youtube.com/watch?v=NF_jeR0aOn4&ab_channel=MasterGorilla",
          "https://www.youtube.com/watch?v=UtBQrBLsTQY&ab_channel=LaughTV", "https://www.youtube.com/watch?v=B-eeNvUEGDk&ab_channel=DailyPicksandFlicks",
          "https://www.youtube.com/watch?v=g8LBnZOjHqA&ab_channel=davidnoles", "https://www.youtube.com/watch?v=aqcgD2sAd8o&ab_channel=BirbBoy",
          "https://www.youtube.com/watch?v=s40PLzt6bL4&ab_channel=TigerProductions", "https://www.youtube.com/watch?v=czuLrKydT3g&ab_channel=JUSTANIMALVIDEOS",
          "https://www.youtube.com/watch?v=vesipJBrU_I&ab_channel=BuZZinG", "https://www.youtube.com/watch?v=BoiJ_KRjB2M&ab_channel=ThePetCollective"]
	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "bird video":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send(random.choice(video))

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("OTgxMzEwNzYxNTM0MTE1ODUw.G5T38n.Twsvbs9hAMC4QRXzev4qNoNPV5xnP9BWrjuCWk")



          

