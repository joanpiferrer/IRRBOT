async def run(message, args, utilidad):
   await message.channel.send(" ".join(args))
   await message.delete()


info ={
   "nombre": "say",
   "des": "El bot repeteix el que dius",
   "uso": "$say [texto]"
}