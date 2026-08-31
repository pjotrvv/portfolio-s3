# Sprint Review Feedback

## Proces review (Annemieke)

- Waarom niet sub-issues gemaakt in plaats van taken? (Manager dashboard accessibility)
- Definition of Ready (DOR) is niet nodig hier (Manager dashboard accessibility)
- Geen dubbele dingen in de user story, anders komt er verwarring
- Gaan de declaraties niet stuk als er een nieuw max bedrag wordt toegevoegd?  
  **Antwoord:** Nee (Max bedrag per categorie)
- Regels maken voor goedgekeurde declaraties met het nieuwe max bedrag per categorie
- Tegen de klant (Timo) zeggen wat we allemaal hebben gedaan
- Afvinken gaat al een stuk beter, nog 1 vergeten dit keer
- “Zou moeten doen” wil ik niet meer horen in een user story
- User stories zitten netjes uitgeschreven
- Als je een wireframe hebt in een sub-issue, verwijs er dan naar in de hoofd user story

## Demo met de klant

- Admin is een beheerder en moet het volgende kunnen:
   - Gebruikers beheren
   - Categorieën beheren
   - Zelf declaraties aanmaken
- Een office manager mag ook categorieën beheren
- Manager mag geen gebruikers beheren, wel categorieën beheren
- Sprintdoelen zijn goed
- Goed dat een manager zijn eigen declaraties niet mag goedkeuren
- Overdracht: ZIP
- Verder geen feedback, goede applicatie

## Code review

- Boolean is niet altijd fijn
- `password` is geen goede endpoint PATCH-mapping (`UserController.java`)

## Sprint planning sprint 7 (verbeter week)
- Max bedrag per categorie per periode
- Admin rol toevoegen en deze kan gebruikers en categorieën beheren
- Accessibility bugfixes
- Responsiveness bugfixes
