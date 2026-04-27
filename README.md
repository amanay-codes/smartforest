A Django incident management system for reporting and managing forest incidents.

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create local settings from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

   Then replace `your_password_here` in `.env` with the real Neon database password.

4. Run migrations:

   ```powershell
   python manage.py migrate
   ```

5. Start the app:

   ```powershell
   python manage.py runserver
   ```

The app runs at `http://127.0.0.1:8000/`.

The project is configured for a shared Neon PostgreSQL database. When everyone uses the same `DATABASE_URL`, registrations, users, and incident reports are stored in the same cloud database and can be viewed from pgAdmin.

## Configuration

Local configuration is read from `.env`. Keep real secrets out of Git.

- `DATABASE_URL` is the recommended way to connect to Neon PostgreSQL.
- `DATABASE_URL` overrides the separate `DB_ENGINE` and `DB_*` values.
- `DB_ENGINE=postgresql` uses the PostgreSQL variables in `.env` if `DATABASE_URL` is empty.
- `DB_HOST` should be the Neon host, not `localhost`, when the team is sharing one cloud database.
- `USE_CLOUDINARY=True` enables Cloudinary media storage.
- `USE_CLOUDINARY=False` stores uploads in local `media/`.

## Neon PostgreSQL Setup

Use the connection string from Neon in `.env`. Do not commit the real password.

Recommended:

```env
DATABASE_URL=postgresql://neondb_owner:your_password_here@ep-morning-darkness-al4cl046-pooler.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

Alternative:

```env
DB_ENGINE=postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=your_password_here
DB_HOST=ep-morning-darkness-al4cl046-pooler.c-3.eu-central-1.aws.neon.tech
DB_PORT=5432
DB_SSLMODE=require
```

After changing database settings, run:

```powershell
python manage.py migrate
```

Django stores registered users in the built-in `auth_user` table.
Submitted incident reports are stored in the `incidents_incidentreport` table.

If submitted reports include images, database rows will be shared through PostgreSQL, but local image files will still be saved on the machine that received the upload unless `USE_CLOUDINARY=True` is configured with shared Cloudinary credentials.
