A Django incident management system for reporting and managing forest incidents.

## Features

- User registration and login
- Incident reporting with optional image upload
- Personal dashboard with report stats and history
- Admin dashboard with filters, status updates, and notes
- Admin statistics and user overview
- Optional Cloudinary media storage

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a local environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Fill in `.env` values (see Configuration below).
5. Run migrations:

   ```powershell
   python manage.py migrate
   ```

6. Create an admin user (optional but recommended):

   ```powershell
   python manage.py createsuperuser
   ```

7. Start the app:

   ```powershell
   python manage.py runserver
   ```

The app runs at `http://127.0.0.1:8000/`.

## Configuration

Local configuration is read from `.env`. Keep real secrets out of Git. The project expects PostgreSQL and will raise an error if a non-PostgreSQL engine is configured.

Required:

- `DJANGO_SECRET_KEY` (use a unique value in production)
- `DJANGO_DEBUG` (`True` or `False`)
- `DJANGO_ALLOWED_HOSTS` (comma-separated)

Database (recommended):

- `DATABASE_URL` (Neon connection string)

Database (alternative if `DATABASE_URL` is empty):

- `DB_ENGINE=postgresql`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_SSLMODE`

Media storage:

- `USE_CLOUDINARY=True` enables Cloudinary storage
- `USE_CLOUDINARY=False` stores uploads in local `media/`
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` (required when Cloudinary is enabled)

## Neon PostgreSQL setup

Use the connection string from Neon in `.env`. Do not commit the real password.

Recommended:

```env
DATABASE_URL=postgresql://neondb_owner:your_password_here@your-neon-host/neondb?sslmode=require&channel_binding=require
```

Alternative:

```env
DB_ENGINE=postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=your_password_here
DB_HOST=your-neon-host
DB_PORT=5432
DB_SSLMODE=require
```

After changing database settings, run:

```powershell
python manage.py migrate
```

Django stores registered users in the built-in `auth_user` table. Incident reports are stored in `incidents_incidentreport`.

If reports include images, database rows are shared through PostgreSQL, but image files remain local unless `USE_CLOUDINARY=True` is configured with shared Cloudinary credentials.

## Routes

- `/` login
- `/register/` registration
- `/dashboard/` user dashboard
- `/my-reports/` report history
- `/report/submit/` new report
- `/admin-dashboard/` admin overview (staff only)
- `/admin/` Django admin

## Tests

```powershell
python manage.py test
```
