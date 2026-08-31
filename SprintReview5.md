---
layout: default
title: Sprint Review 5
---

# Sprint Review Feedback - Proces, Demo en Code

## Context
Deze feedback is ontvangen tijdens de sprint review dag. De feedback richt zich op proces, demo inhoud en codekwaliteit.

---

## Proces feedback
- Er staan veel zaken open.
- Als iets op *To Do* staat, betekent dit dat het is beloofd dus plaats het in de backlog.
- Het afvinken van acceptatiecriteria is erg belangrijk.
- Wanneer in acceptatiecriteria staat “bestaat al”, moet worden aangegeven waar dit terug te vinden is.
- Meer aandacht voor de status *Ready to Review*.
- Mooie wireframes.
- Goede sub-issues.
- Maak een aparte issue voor accessibility.
- Op **8 januari** volgt opnieuw een accessibility test.
- Twee dagen vóór de demo alles pushen naar de repository.

---

## Demo feedback
- Validatie voor datums moet werken vóór de demo.
- Een admin-rol moet worden aangemaakt om gebruikers en categorieën te beheren (admin dient geen declaraties in).
- Eerst validatie goed laten werken, daarna andere functionaliteiten.
- Statistieken moeten worden afgerond.
- Validatie heeft hoge prioriteit.
- Validatie van bedragen ontbreekt.
- Spelling van categorieën op de website is onjuist.
- Statistieken zijn nog niet af.
- Er is deze sprint onvoldoende contact geweest.
- Stel prioriteiten: wat is het belangrijkste voor deze sprint?
- Er zijn drie verschillende categorieën met maximale bedragen en verschillende datums.
- Er volgt een e-mail met aanvullende informatie.

---

## Code review feedback
- Het gaat niet om unit tests maar om integration tests (`CategoryServiceTest`).
- `@PrePersist` is niet betrouwbaar.
- `setActive` mag niet public zijn en hoort in de constructor.
- De package-naam van *Declaratie* is niet correct, maar aanpassen kost veel werk.
- `Declaratie.java` moet worden verwijderd.
- Niet alle functies hebben `@Transactional` nodig.
- Geef extra aandacht aan de logica in `ClaimController.java`.
