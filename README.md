# Sykepenge-styringsinfo-kvalitetssjekk

Naisjob for periodisk kjøring av Soda-sjekker på BigQuery-tabeller og varsle til Slack ved avvik.

Konfigurasjonen ligger i [nais/](nais/).

## Lokal utforskning

I mappen [local/](local/) ligger det filer som kan brukes til å kjøre fra lokal maskin. Merk! at disse IKKE er det samme som kjøres i naisjobben (konfigurasjonen for det ligger i [nais/](nais/)).

For å kjøre kan du forsøke følgende:
```
cd local
make run-soda-scan
```

## Henvendelser

Spørsmål knyttet til koden eller prosjektet kan rettes mot:

* Kjetil (kjetil.jorgensen-dahl at nav.no)

### For NAV-ansatte

Interne henvendelser kan sendes via Slack.