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

4. Run migrations:

   ```powershell
   python manage.py migrate
   ```

5. Start the app:

   ```powershell
   python manage.py runserver
   ```

The app runs at `http://127.0.0.1:8000/`.

By default, each developer uses their own local SQLite database at `db.sqlite3`. Users registered on one computer will not appear on another computer unless both apps are configured to use the same shared database.

## Configuration

Local configuration is read from `.env`. Keep real secrets out of Git.

- `DB_ENGINE=sqlite` uses the local SQLite database.
- `DB_ENGINE=postgresql` uses the PostgreSQL variables in `.env`.
- `DB_HOST=localhost` means the database on the same computer running Django. Do not use `localhost` if you expect other computers to write into your database.
- `USE_CLOUDINARY=True` enables Cloudinary media storage.
- `USE_CLOUDINARY=False` stores uploads in local `media/`.

## Shared database setup

If everyone should register and submit reports into the same database, create one shared PostgreSQL database on a server or hosted provider, then give each developer the same database connection in their local `.env`.

Recommended:

```env
DATABASE_URL=postgresql://your_shared_db_user:your_shared_db_password@your-db-host-or-server-ip:5432/smartforest?sslmode=prefer
```

`DATABASE_URL` overrides the separate `DB_ENGINE` and `DB_*` values.

Alternative:

```env
DB_ENGINE=postgresql
DB_NAME=smartforest
DB_USER=your_shared_db_user
DB_PASSWORD=your_shared_db_password
DB_HOST=your-db-host-or-server-ip
DB_PORT=5432
DB_SSLMODE=prefer
```

After changing database settings, run:

```powershell
python manage.py migrate
```

Django stores registered users in the built-in `auth_user` table.
Submitted incident reports are stored in the `incidents_incidentreport` table.

If submitted reports include images, database rows will be shared through PostgreSQL, but local image files will still be saved on the machine that received the upload unless `USE_CLOUDINARY=True` is configured with shared Cloudinary credentials.
