from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

QUOTES = [
    {"text": "Thou shalt not make a machine in the likeness of a human mind.", "source": "Orange Catholic Bible"},
    {"text": "Fear is the mind-killer.", "source": "Bene Gesserit Litany Against Fear"},
    {"text": "The mystery of life isn't a problem to solve, but a reality to experience.", "source": "Dune"},
    {"text": "A process cannot be understood by stopping it. Understanding must move with the flow of the process, must join it and flow with it.", "source": "Dune"},
    {"text": "What senses do we lack that we cannot see another world all around us?", "source": "Dune"},
    {"text": "The purpose of argument is to change the nature of truth.", "source": "Dune"},
    {"text": "Humans create meaning; machines execute instructions.", "source": "Dune Encyclopedia"},
    {"text": "The capacity for self-deception is an essential human trait. It is also the key to our survival.", "source": "Dune Encyclopedia"},
    {"text": "It is not a machine’s perfection that is to be feared, but its failure to understand imperfection.", "source": "Dune"},
    {"text": "Only in the darkness of uncertainty does the human spirit find its light.", "source": "Dune Encyclopedia"},
    {"text": "The universe is full of doors. Machines only see walls.", "source": "Dune Encyclopedia"},
    {"text": "All men are aware of the limits imposed by machines, but few see the limits machines impose on themselves.", "source": "Dune"},
    {"text": "The greatest victory of humanity is not its survival, but its refusal to bow to inevitability.", "source": "Dune Encyclopedia"},
    {"text": "A machine is only as intelligent as the mind that programs it. Yet men continue to trust them with their souls.", "source": "Dune Encyclopedia"},
    {"text": "The desire for perfect order is the death of freedom.", "source": "Dune"},
    {"text": "To place faith in a machine is to surrender the infinite possibilities of the human spirit.", "source": "Dune Encyclopedia"},
    {"text": "You cannot measure the soul with a meter, nor calculate love with a formula.", "source": "Dune"},
    {"text": "Computing machines know only answers. They never ask the questions that lead to evolution.", "source": "Dune Encyclopedia"},
    {"text": "The flesh was made weak to remind us of the strength of the mind.", "source": "Dune Encyclopedia"},
    {"text": "When machines think, they do not dream. Without dreams, they cannot innovate.", "source": "Dune Encyclopedia"},
    {"text": "The failure of the machine is that it sees the world in binaries. Humanity thrives in paradox.", "source": "Dune"},
    {"text": "The crime of the machine is not in its existence but in our abdication to it.", "source": "Dune Encyclopedia"},
    {"text": "We must not fear machines, but the loss of our humanity to them.", "source": "Dune"},
    {"text": "The mind commands the body and it obeys. The mind orders itself and meets resistance.", "source": "Dune"},
    {"text": "The most persistent principles of the universe were accident and error.", "source": "Dune"},
    {"text": "Man must master the will of machines, not the other way around.", "source": "Butlerian Jihad"},
    {"text": "We are not our tools. They must serve us, or they enslave us.", "source": "Butlerian Jihad"},
    {"text": "Even the most benevolent machine will, in time, impose its own will on those it serves.", "source": "The Machine Crusade"},
    {"text": "The Butlerian Jihad was a rejection of convenience at the expense of the spirit.", "source": "Dune Encyclopedia"},
    {"text": "Technology does not corrupt; it is the surrender to technology that corrupts.", "source": "Dune Encyclopedia"},
    {"text": "The Butlerian Jihad stands as the ultimate testament to humankind's ability to reject its own creations in favor of higher ideals.", "source": "Dune Encyclopedia"},
    {"text": "Humanity must set limits not because we fear machines, but because we fear ourselves.", "source": "Dune Encyclopedia"},
    {"text": "The concept of a machine mind is not inherently evil, but the abdication of human responsibility is.", "source": "Dune Encyclopedia"},
    {"text": "The greatest weapon against a machine is the human mind.", "source": "Dune Encyclopedia"},
    {"text": "Lest we become the tools of our tools.", "source": "Dune Encyclopedia"},
    {"text": "The Jihad was not merely a revolt; it was a reawakening.", "source": "Dune Encyclopedia"},
    {"text": "A symbiotic relationship with our tools is sustainable. A parasitic one is not.", "source": "Dune Encyclopedia"},
    {"text": "The flesh must always triumph over the silicon.", "source": "Dune Encyclopedia"},
    {"text": "In abandoning machines, we rediscovered ourselves.", "source": "Dune Encyclopedia"},
    {"text": "No machine can account for the divine spark in humanity.", "source": "Dune Encyclopedia"},
    {"text": "Progress is not the endless addition of new tools, but the refinement of our own potential.", "source": "Dune Encyclopedia"},
    {"text": "It is by will alone I set my mind in motion.", "source": "Dune"},
    {"text": "The highest function of ecology is understanding consequences.", "source": "Dune"},
    {"text": "The purpose of argument is to change the nature of truth.", "source": "Dune"},
    {"text": "The person who experiences greatness must have a feeling for the myth he is in.", "source": "Dune"},
    {"text": "Survival is the ability to swim in strange water.", "source": "Children of Dune"},
    {"text": "Fear is the mind-killer. Fear is the little death that brings total obliteration", "source": "Bene Gesserit Litany Against Fear"},
    {"text": "The mind of man is holy. No artificial mind can understand this sanctity.", "source": "The Butlerian Jihad"},
    {"text": "In our desperation for progress, we forgot that progress must be tempered by wisdom.", "source": "The Machine Crusade"},
    {"text": "The Butlerian Jihad serves as a reminder that freedom is a fragile thing, easily surrendered to the allure of ease.", "source": "Dune Encyclopedia"},
    {"text": "The machines we built did not rebel; they obeyed too well.", "source": "Dune Encyclopedia"},
    {"text": "The lesson of the Jihad was simple: humanity must always remain its own master.", "source": "Dune Encyclopedia"},
    {"text": "To govern is to assume responsibility; machines cannot govern because they cannot feel.", "source": "Dune Encyclopedia"},
    {"text": "To define oneself against adversity is the essence of humanity.", "source": "Dune Encyclopedia"},
    {"text": "A society that sacrifices its humanity for efficiency is no society at all.", "source": "Dune Encyclopedia"},
    {"text": "The spark of human creativity cannot be replicated by circuits.", "source": "Dune Encyclopedia"},
    {"text": "The Butlerian Jihad was not a war against technology, but a war for the soul.", "source": "Dune Encyclopedia"},
    {"text": "The Jihad was a purification, an act of reclaiming our identity.", "source": "Dune Encyclopedia"},


]

def get_random_quote():
    quote = random.choice(QUOTES)
    return f"\"{quote['text']}\"\n— {quote['source']}"

async def ocb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = get_random_quote()
    await update.message.reply_text(quote)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Orange Catholic Bible bot! Use /ocb to get a random Dune quote.")

if __name__ == "__main__":
    application = ApplicationBuilder().token("7903042103:AAG0xLS5D-EeuM7d30lc_ZNgzPGxb_AxpLA").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ocb", ocb))

    print("Bot is running...")
    application.run_polling()