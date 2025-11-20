import asyncio
from telethon import TelegramClient

# Credenciais do Telegram
api_id = 32762064
api_hash = "802a1c71d828f65ea81a246c05771b83"
bot_token = "8288407638:AAHDCgsMqhphqW0SOP1xu6ASIlpuL25BLvM"

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

GRUPO = -1002279117860
USUARIO_ALVO = "sylweir"   # sem @

async def responder():
    while True:
        try:
            mensagens = await client.get_messages(GRUPO, limit=50)
            for msg in mensagens:
                if msg.sender and msg.sender.username == USUARIO_ALVO:
                    await client.send_message(GRUPO, "/cenoura", reply_to=msg.id)
                    break
        except Exception as e:
            print("Erro:", e)

        await asyncio.sleep(10800)  # 3 horas


# Mantém o bot vivo no Render
async def keep_alive():
    while True:
        await asyncio.sleep(60)


async def main():
    await asyncio.gather(
        responder(),
        keep_alive()
    )

client.loop.run_until_complete(main())