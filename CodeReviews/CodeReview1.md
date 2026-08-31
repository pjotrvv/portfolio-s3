# Code review 1

Deze code is gereviewed door Mirko.

Wat ik heb geimplementeerd is het weergeven van error messages onder elke form input die verkeerd is ingevoerd.

https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/pull/165

## Feedback
Wat me op valt is de manier waarop je de vertaling geïmplementeerd hebt. Als ik het goed begrijp krijg je een Engelstalige string (ik neem aan uit de backend) en die ga je matchen met een string in ERROR_TRANSLATIONS en als je een match hebt  gebruik je die. 
 
Dit lijkt me erg kwetsbaar en daardoor niet erg onderhoudbaar. Stel dat er een spelfoutje zit in de Engelse tekst en je past deze aan in de backend, dan moet je je bedenken dat je dezelfde wijziging maakt in de frontend anders gaat het mis. Ook is het niet mogelijk om een derde taal makkelijk toe te voegen (het is dus niet makkelijk uitbreidbaar).
 
Een slimmere methode is om (ook) een error ID vanuit de backend mee te geven. Deze kan je dan matchen tegen welke vertaling dan ook. 
 
-----
 
Wat ik wel sterk vind is de conversatie tussen Merlijn en jou in de PR. Merlijn is scherp, maar jij weet goed antwoord te geven. Dat is wat we in een PR willen zien.

## Verwerken feedback

### U.S/Bug
https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/193
