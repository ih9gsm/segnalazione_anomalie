# segnalazione_anomalie

Simple anomaly reporting application for airports. The backend exposes APIs to
manage users, configure SMTP and logo settings, and generate reports. Reports
are produced as PDF and Word files and can be emailed to specified recipients.

## Testing

Backend tests use PyTest:

```bash
PYTHONPATH=. pytest
```

Frontend unit tests use Jest and Cypress for end-to-end tests:

```bash
npm test --prefix frontend
npm run cypress --prefix frontend
```
