from os import system
import time
import os
import sys

version = 1.0


class couleur:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    PERS = 0xf03434


def clear():
    cleara = lambda: os.system("cls")
    cleara()


def logo():
    print(couleur.FAIL + f"""
    {espace}██╗    ██╗██████╗ ████████╗{espace}
    {espace}██║    ██║██╔══██╗╚══██╔══╝{espace}
    {espace}██║ █╗ ██║██║  ██║   ██║   {espace}
    {espace}██║███╗██║██║  ██║   ██║   {espace}
    {espace}╚███╔███╔╝██████╔╝   ██║   {espace}
    {espace} ╚══╝╚══╝ ╚═════╝    ╚═╝   v""" + str(version) + espace + couleur.WHITE + f"""{espace}
                                               Webhook Discord Tool
                                     | github.com/nowed02 | discord.io/dewon |{espace}""")


def fermer():
    clear()
    logo()
    print(couleur.OKGREEN + f"\n\n{espace_menu * 5} Instruction terminée fermeture de l'application dans 3 secondes...")
    time.sleep(3)
    print(couleur.FAIL + f"\n{espace_menu * 10}Fermeture...")
    time.sleep(1.5)
    sys.exit()


def choix1():
    clear()
    logo()
    content = input(couleur.OKBLUE + f"\n{espace_menu * 7} Que voulez vous spam ?: ")
    time.sleep(0.3)
    combien = input(couleur.OKBLUE + f"\n{espace_menu * 7} Combien de fois ?: ")
    time.sleep(0.3)
    pseudo = input(couleur.OKBLUE + f"\n{espace_menu * 7}Entrez le pseudo souhaité du Webhook: ")
    time.sleep(0.3)
    url = input(couleur.OKBLUE + "\nEntrez l'URL du Webhook: ")
    print()
    time.sleep(0.3)
    webhook = DiscordWebhook(url=url, username=str(pseudo), content=str(content))
    try:
        for i in range(int(combien)):
            envoie = webhook.execute()
            print(couleur.WHITE + f"{espace_menu * 10}Message envoyé: " + str(i + 1))
            time.sleep(0.5)
    except:
        erreur()
    time.sleep(0.5)


def choix2():
    clear()
    logo()
    pseudo = input(couleur.OKBLUE + f"\n{espace_menu * 7}Entrez le pseudo souhaité du Webhook: ")
    time.sleep(0.3)
    url = input(couleur.OKBLUE + "\nEntrez l'URL du Webhook: ")
    time.sleep(0.3)
    content = input(couleur.OKBLUE + f"\n{espace_menu * 7}Que voulez vous envoyer (hors embed) ?: ")
    webhook = DiscordWebhook(url=url, username=str(pseudo), content=str(content))
    mettreEmbed = input(str(f"\n{espace_menu * 7}Voulez-vous mettre un embed ? [o/n]: "))
    if mettreEmbed == "o":
        titre = input(f"{espace_menu * 8}Titre de l'embed: ")
        contenue = input(f"{espace_menu * 8}Le contenue du webhook ?: ")
        embed = DiscordEmbed(title=titre, color=424242)
        embed.add_embed_field(name="Message", value=contenue)
        embed.set_footer(text="discord.io/dewon")
        webhook.add_embed(embed)
    else:
        pass
    envoie = webhook.execute()
    print(f"{espace_menu * 9}Message envoyé !")
    time.sleep(0.5)


def choix3():
    clear()
    logo()
    webhook = input(couleur.OKBLUE + "\nL'URL du Webhook à supprimer: ")
    print(couleur.OKBLUE + f"{espace_menu * 10}Suppresion...")
    time.sleep(0.3)
    try:
        hook = Webhook(webhook)
        hook.delete()
        print(couleur.OKGREEN + f"{espace_menu * 9}   Webhook supprimé !")
        time.sleep(1)
    except:
        erreur()


def choix4():
    clear()
    logo()
    webhook = input(couleur.OKBLUE + "\nEntrez l'URL du webhook: ")
    print(f"\n\n{espace_menu * 9}Récolte des infos...")
    time.sleep(1.5)
    hook = Webhook(webhook)
    hook.get_info()
    print(couleur.OKGREEN + f"{espace_menu * 9}Récolte des infos terminé.")
    time.sleep(1)
    print(couleur.WHITE + f"\n\n{espace_menu * 9}Nom du Webhook: " + str(hook.default_name))
    time.sleep(0.3)
    print(f"\n{espace_menu * 6}Photo de profil: " + hook.default_avatar_url)
    time.sleep(0.3)
    print(f"\n{espace_menu * 6}Catégorie où le bot se situe (Avec un ID): " + str(hook.guild_id))
    time.sleep(0.3)
    print(f"\n{espace_menu * 6}Channel où le bot se situe (Avec un ID): " + str(hook.channel_id))
    time.sleep(0.3)
    print(f"\n{espace_menu * 4}Token du bot: " + hook.token)
    time.sleep(0.3)
    input(couleur.OKBLUE + "\n\nAppuyez sur ENTER pour fermer l'application.")


def choix5():
    clear()
    logo()
    print(couleur.OKBLUE + f"\n{espace_menu * 8}Ici tu peux modifier le nom du Webhook")
    webhook = input(str("Entrez l'URL du Webhook: "))
    pseudo = input(f"{espace_menu * 8}   Pseudo à modifier: ")
    time.sleep(0.5)
    try:
        hook = Webhook(webhook)
        hook.modify(name=pseudo)
        print(couleur.OKGREEN + f"{espace_menu * 9}    Pseudo modifié !")
        time.sleep(1.5)
    except:
        erreur()


def erreur():
    print(couleur.FAIL + "ERREUR: Erreur lors de l'execution du script, veuillez vérifier vos arguments.")
    time.sleep(3)


def menu():
    print(couleur.OKGREEN + f"""


    {espace_menu * 3}   [1] Spam un Webhook{espace_menu}[2] Envoyer un message {espace_menu}[3] Supprimer un Webhook{espace_menu}

    {espace_menu * 5}      [4] Infos Webhook{espace_menu}[5] Modifier un Webhook{espace_menu * 5} 
    """)


def main():
    init(convert=True)
    logo()
    menu()
    choix = input(couleur.OKBLUE + f"\n{espace_menu * 7}    Que voulez vous faire (Numéro): ")
    print(choix)
    if choix == str(1):
        choix1()
        fermer()
    elif choix == str(2):
        choix2()
        fermer()
    elif choix == str(3):
        choix3()
        fermer()
    elif choix == str(4):
        choix4()
        fermer()
    elif choix == str(5):
        choix5()
        fermer()


try:
    system("title " + "Webhook Discord Tools v" + str(version))
    clear()
    print("Chargement des modules...")
    from colorama import Fore, Back, Style, init
    import discord
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from dhooks import Webhook

    print("Tout les modules ont étés correctement chargés.")
    time.sleep(1)
    clear()
except:
    print("Les modules ne sont pas correctement chargés / installés.")
    time.sleep(0.5)
    clear()
    print("Tentative d'installation des modules...")
    time.sleep(0.5)
    clear()
    try:
        system("pip install discord")
        clear()
        system("pip install colorama")
        clear()
        system("pip install discord_webhook")
        clear()
        system("pip install dhooks")
        time.sleep(1)
        clear()
        print("Tout les modules sont correctement installés.")
    except:
        print("Erreur lors de l'installation des modules...")
        leave = input("Veuillez vérifier si PIP est correctement installé. (ENTER pour quitter)")
        quit()
    quit()

espace = ' ' * 40
espace_menu = " " * 5


if __name__ == '__main__':
    main()
    input()
