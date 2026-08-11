# To Do List — Task Tracker (Django + Vue)

Full-stack task tracker with token-based authentication: a Django REST Framework
backend and a Vue.js frontend.

**▶ Try it live — no account needed:**
[portfolio-mparraf.herokuapp.com/todo/demo](https://portfolio-mparraf.herokuapp.com/todo/demo/)
(embedded in my portfolio; the demo user resets its tasks on every visit)

## Features

- Task CRUD with priority (low / medium / high / important) and effort levels
- Dashboard grouping tasks by priority
- Token authentication (Djoser) for the API; session auth for the embedded app
- AJAX task list updates without full page reloads

## Stack

| Layer | Technologies |
|---|---|
| Backend | Python · Django · Django REST Framework · Djoser · PostgreSQL |
| Frontend | Vue.js · Axios · Vuex store |
| Auth | Token-based (API) · session (web) |

## Project layout

```
backend/    Django project: config/, todo_app/ (models, DRF views, serializers)
frontend/   Vue application: src/, store/, plugins/
```

## Running locally

Backend:

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env      # fill in your own values — never commit .env
python manage.py migrate
python manage.py runserver
```

Frontend:

```bash
cd frontend
npm install
npm run serve
```

## Author

Marco Antonio Parra F. — [portfolio](https://portfolio-mparraf.herokuapp.com) ·
[LinkedIn](https://www.linkedin.com/in/marco-antonio-parra-82999337/)
