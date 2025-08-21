# segnalazione_anomalie

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
