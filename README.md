                A Django incident management system for reporting and managing forest incidents.

## Local Setup

1. Create and activate a virtual environment.
2. Install depen                                                                                                                                                           dencies:

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

The app runs at `http://127.0.0.1:8000/` and uses local SQLite by default, so submitted incidents and admin updates persist immediately in `db.sqlite3`.

## Configuration

Local configuration is read from `.env`. Keep real secrets out of Git.

- `DB_ENGINE=sqlite` uses the local SQLite database.
- `DB_ENGINE=postgresql` uses the PostgreSQL variables in `.env`.
- `USE_CLOUDINARY=True` enables Cloudinary media storage.
- `USE_CLOUDINARY=False` stores uploads in local `media/`.
