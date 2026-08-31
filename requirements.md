# Requirementanalyse
## 1. Doel van de applicatie
Een gebruiksvriendelijke, efficiënte en schaalbare webapplicatie ontwikkelen voor het indienen, goedkeuren en verwerken van declaraties, met als doel:
- Administratieve lasten te verminderen
- Fouten te vermeiden
- Verwerkingstijd te verkorten
- Transparantie te verbeteren

## 2. Functionele eisen
### 2.1 Werknemers kunnen declaraties indienen via een website (Must)
- Werknemers kunnen inloggen via een webomgeving
- Mogelijkheid om een foto van een bonnetje te maken en te uploaden
- Invoervelden: titel, datum, bedrag en type kosten
- Validatie van invoervelden

### 2.2 Goedkeuringsflow (Must)
- Declaraties worden automatisch naar de juiste manager gestuurd op basis van de afdeling
- Managers kunnen declaraties goedkeuren of afkeuren met één klik.
- Managers kunnen opmerkingen toevoegen bij een afwijzing. (Could)

### 2.3 Dashboard voor office managers
- Overzicht van alle goedgekeurde declaraties (Must)
- Filtermogelijkheden op status, medewerker, datum, type kosten. (Could)
- Mogelijkheid om opmerkingen en statussen te zien (Should)

### 2.4 Accountant-integratie (could)
- Exportfunctie van goedgekeurde declaraties voor verwerking in loonadministratie
- Via CSV export?

### 2.5 Beheer in instellingen
- Rollen en rechtenbeheer (werknemer, manager, office manager en accountant) (Must)
- Instelbare goedkeuringsregels per afdeling? (Could)

## 3. Niet-functionele eisen
### 3.1 Gebruiksvriendelijkheid
- Makkelijk te gebruiken interface voor elke gebruikersrol
- Responsive design voor desktop en mobiel

### 3.2 Beveiliging en privacy
- Gegevens worden versleuteld opgeslagen (must)
- Voldoet aan AVG-richtlijnen (must)
- Geavanceerde beveiliging zoals 2FA of SSO (could)

### 3.3 Performance
- De applicatie moet snel reageren, ook bij grote aantallen declaraties. (should)
- Backend moet schaalbaar zijn voor toekomstige uitbereiding. (should)

### 3.4 Betrouwbaarheid
- Audit logs (could)
