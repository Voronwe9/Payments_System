


# 💰 Payments System — Django Webhook Service

Проект представляет собой backend-сервис на Django, который принимает входящие вебхуки от банка и обновляет баланс организаций.

## 📌 Функциональность

- Приём вебхуков через `POST /api/webhook/bank/`
- Проверка на дублирование операций по `operation_id`
- Начисление суммы на баланс организации по `payer_inn`
- Хранение платежей и логов изменения баланса
- Просмотр текущего баланса по ИНН: `GET /api/organizations/<inn>/balance/`
- Swagger и ReDoc для тестирования и документации API



## 🚀 Установка и запуск

1. **Клонировать репозиторий**
   ```bash
   git clone <your-repo-url>
   cd payments_system


2. **Создать виртуальное окружение и установить зависимости**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Настроить базу данных (MySQL)**

   *Убедись, что в `settings.py` прописаны правильные параметры подключения к базе(в примере указаны не реальные данные)*:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'payments_db',
           'USER': 'USER',
           'PASSWORD': 'PASSWORD',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Выполнить миграции**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Запустить сервер**

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Swagger и тестирование

Swagger UI доступен по адресу:

```
http://127.0.0.1:8000/swagger/
```

ReDoc (альтернатива Swagger):

```
http://127.0.0.1:8000/redoc/
```

Пример запроса на `/api/webhook/bank/`:

```json
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": "145000.12",
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}
```

Пример ответа на дубликат:

```json
{
  "detail": "Payment already exists"
}
```

---

## 📂 Структура

* `payments/` — логика приёма и обработки платежей
* `organizations/` — модель организаций и баланс
* `api/` — urls, views, serializers
* `drf_yasg` — автогенерация документации

---

## 👨‍💻 Автор

Антон Барынин
📧 [anton.barynin.dev@gmail.com](mailto:anton.barynin.dev@gmail.com)
📱 +7 916 070-77-70
💬 Telegram: [@Voron9gg](https://t.me/Voron9gg)
💼 GitHub: [Voronwe9](https://github.com/Voronwe9)

---


