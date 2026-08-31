# S3 - Accessibility Test

## Site

[URL van de site](http://172.160.249.155/)

## Testplan
Gebruikers
| Rol     	| Wachtwoord 	| Email          	|
|---------	|------------	|----------------	|
| Manager 	| 1234       	| jan@quintor.nl 	|

### Scenario 1: Manager Dashboard Accessibility
1. Login als een manager
2. Navigeer naar de Manager Dashboard pagina.
3. Open een declaratie vanuit de zijbalk.
4. Beoordeel op basis van de declaratie details of de declaratie goedgekeurd of afgekeurd moet worden.
5. Beoordeel de declaratie en voer de actie goedkeuren of afkeuren uit.

### Scenario 2: Foute invoer in een declaratie geeft foutmeldingen die accessable zijn
1. Login met een account, het maakt niet uit welke.
2. Maak een nieuwe declaratie aan via de home pagina, en laat expres een veld leeg zodat er een foutmelding komt.
3. Verbeter daarna de declaratie door het lege veld in te voeren.
4. Dien de declaratie in.

## Scenario 3: Categorie aanpassen is hoorbaar voor screenreaders
1. Login als manager.
2. Navigeer naar de categoriepagina.
3. Activeer een screenreader (bijvoorbeeld NVDA of VoiceOver).
4. Druk op de knop **“Aanpassen”** bij een categorie.
5. Controleer of de screenreader aankondigt dat er een dialoog is geopend.
6. Controleer of de focus automatisch in het formulier staat.
7. Sluit de dialoog met de **Escape-toets**.

## Scenario 4: Nieuwe categorie toevoegen is hoorbaar voor screenreaders
1. Login als manager.
2. Ga naar de categoriepagina.
3. Activeer een screenreader.
4. Druk op de knop **“Nieuwe categorie toevoegen”**.
5. Luister of de screenreader meldt dat een nieuwe dialoog is geopend.
6. Vul het formulier in met het toetsenbord.
7. Sla de categorie op.

## Scenario 5: Categorie verwijderen is toegankelijk
1. Login als manager.
2. Navigeer naar de categoriepagina.
3. Activeer een screenreader.
4. Kies een categorie en druk op **Verwijderen**.
5. Controleer of de bevestigingsdialoog hoorbaar wordt aangekondigd.
6. Annuleer of bevestig de actie met het toetsenbord.

## Scenario 6: Navigeren tussen declaraties
1. Login met een account, het maakt niet uit welke.
2. Navigeer naar home pagina met de declaraties van de gebruiker.
3. Selecteer links een declaratie uit het selectiemenu.
4. Controleer of de declaratie opent en dat de focus automatisch naar h1 van die declaratie gaat.

## Scenario 7: Gebruik maken van filtermenu
1. Login met een account, het maakt niet uit welke.
2. Navigeer naar home pagina met de declaraties van de gebruiker.
3. Open het filtermenu van het selectiemenu.
4. Stel een paar filters in.
5. Druk onderaan op de reset filters knop.
6. Controleer of de screenreader een bevesteging zegt.

## Scenario 8: Invullen declaratie
1. Login met een account, het maakt niet uit welke.
2. Navigeer naar home pagina met de declaraties van de gebruiker.
3. Druk op de knop "Nieuwe declaratie" in het selectiemenu.
4. Controleer of de focus automatisch gaat naar h1 van nieuwe declaratie.
5. Navigeer met de focus naar het uploaden van een bewijsstuk.
6. Upload een bewijsstuk.
7. Vul de rest van de declaratie in.
8. Dien de declaratie in.

## GitHub Issues

- [User story: Manager dashboard accessibility #159](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/159)

- [Bug: De foutmelding die via alert() gegeven worden zijn niet accessable voor mensen die een screenreader gebruiken #162](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/162)

- [User story: Accessibility 'mijn declaraties' pagina #167](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/167)

- [User story: Filter menu accessibility #160](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/160)

- [User story: Toegankelijke categoriepagina met screenreader ondersteuning #170](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/170)

## Solved Issues

_Geef hier een lijst van (GitHub) issues, waarvan na de 2e test blijkt dat deze zijn opgelost. Als dat weer GitHub issues zijn, zorg er dan voor dat de links naar de issues werken._

## Feedback van Tom
Onze applicatie is getest op toegankelijkheid door Tom, een gebruiker die blind is en werkt met een screenreader en toetsenbordnavigatie.
Tijdens de test gaf hij aan dat alle functionaliteiten goed te bedienen waren met tab-navigatie en dat de screenreader duidelijke en correcte feedback gaf bij interacties met de applicatie.
De enige feedback die hij gaf, was dat het uploaden van een bestand niet mogelijk was. Buiten dit punt kon hij de applicatie zelfstandig en zonder problemen gebruiken.

[Issue bug afbeelding uploaden](https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/186)
