# Code review
> Deze code review is gegeven door Annet

### Feedback
- Goed gebruik gemaakt van de bcrypt password encoder met interface
- Goed gebruik gemaakt van password rules door middel van een regex in de dto, alleen moet dit in de toekomst in het domein toegepast worden.
- De user identifier word uit de jwt token gehaald wat ook erg goed is.
- Op dit moment kan er een gebruiker die needsPasswordChange true heeft alsnog requests maken naar de back-end. Het is veilig als dit niet kan.

### P.R

https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/pull/178/changes

## Verwerkte feedback
https://github.com/HU-SD-S3-Studenten-S2526/s3-project-codaro/issues/194
