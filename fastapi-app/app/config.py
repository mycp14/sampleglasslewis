import os

# e.g. postgresql+psycopg://user:password@host:5432/dbname
# When unset, the app falls back to the in-memory repository.
DATABASE_URL: str | None = os.getenv("DATABASE_URL") or None
