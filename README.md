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
- `"auteur"` : l'auteur du raid.

Vous devez remplir les champs correspondants dans le fichier `config.json` avant d'exécuter le programme.

### Lancement du programme

Une fois que vous avez configuré les paramètres dans le fichier `config.json`, vous pouvez lancer le programme en exécutant le fichier `main.py`.

Un `/raid` est intégré

Le bot va raid le serveur.

### Remarque

- Ce script est conçu à des fins éducatives uniquement et ne doit pas être utilisé pour nuire à autrui ou violer les conditions d'utilisation de Discord.
- L'utilisation de ce script pour effectuer un raid sur un serveur sans l'autorisation du propriétaire du serveur est illégale.
- L'auteur de ce script n'est pas responsable des dommages ou des problèmes juridiques pouvant résulter de l'utilisation de ce script.

## Licence

Ce programme est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
