# Basic Discord Bot Shop : Readme

Ce Bot est fait pour subvenir au besoin d'un discord de vente de services avec un systeme de vouch avancer, et bien plus. Le programme lit la configuration (token, lien et message) depuis le fichier `config.json`.

## Installation des differents modules

Si vous utilisez une machine vous aurez simplement besoin de renseigner le fichier `requirements.txt` dans l'onglet startup de votre Hebergeur, n'oublier pas de mettre dans la machine le `main.py` dans `APP PY FILE`

https://media.discordapp.net/attachments/1131599070281089104/1209081086492155924/image.png?ex=65e59f82&is=65d32a82&hm=5b1356a2217f948bb188c0c283decb1f4988caddc4aa7896e6c512ba2c06305f&=&format=webp&quality=lossless&width=546&height=462

## Autres facons d'installer les modules

Vous allez ouvrire le dossiers de votre bot est dans la localisation de votre dossiers vous allez y inscrire `cmd` et `ENTRER` 
https://media.discordapp.net/attachments/1131599070281089104/1209081437735616562/image.png?ex=65e59fd6&is=65d32ad6&hm=31a883815fb369c5b0dd8224adcbef02f17c56ee971005affec7e0922bb38b77&=&format=webp&quality=lossless

En suite vous allez inscrire dans l'invite de command:

```bash
pip install -r requirements.txt
```

## Utilisation du programme

### Configuration

Avant de lancer le bot, vous devez configurer les paramètres dans le fichier `config.json`. Les paramètres disponibles sont :

- `"token"` : le token de votre bot Discord.
- `"app_id"` : L'ID de votre bot.
- `"guild"` : Le serveur ou vous utilisez le module ou le bot.
- `"channel"` : Le salon ou vous utilisez le module ou le bot.
- `"role"` : Le role donne au nouveau arrivant sur le serveur.
- `"title"` : Le titre qui apparait sur l'image d'affichage du modules de bienvenue.
- `"background"` : La localisation de l'image d'affichage du modules de bienvenue.

Vous devez remplir les champs correspondants dans le fichier `config.json` avant d'exécuter le programme.

### Lancement du programme

Une fois que vous avez configuré les paramètres dans le fichier `config.json`, vous pouvez lancer le programme en exécutant le fichier `main.py` ou depuis votre hebergeur.

Apres lancement un message apparaitra dans la console et vos command seront sous forme de `slash commands`.

### Remarque

- Ce code est soumis a des loi de droits d'auteur toute usurpation est passible de poursuite.

## Licence

Ce programme est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
