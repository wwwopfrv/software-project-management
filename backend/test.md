# Стратегия тестирования API Gateway

## Типы тестов

### 1. Unit тесты
- Маршрутизация (правильный endpoint)
- Валидация JWT токенов
- Rate limiting логика
- Circuit breaker состояния (closed/open/half-open)

### 2. Интеграционные тесты
- Gateway ↔ Redis (лимиты)
- Gateway ↔ микросервисы (маршрутизация)
- Gateway ↔ Swagger (генерация документации)

### 3. Нагрузочное тестирование (опционально)
- Проверка 1000 RPS
- Проверка корректной работы rate limiting

## CI/CD пайплайн (GitHub Actions)

```yaml
name: CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test # unit + интеграционные тесты
      - run: npm run test:load # нагрузочное (опционально)

  deploy-staging:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    steps:
      - run: echo "Деплой на staging Kubernetes"
