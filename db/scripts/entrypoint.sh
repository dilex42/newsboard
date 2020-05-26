#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE newsboard;
    CREATE USER newsboard WITH PASSWORD '123';
    ALTER ROLE newsboard SET client_encoding TO 'utf8';
    ALTER ROLE newsboard SET default_transaction_isolation TO 'read committed';
    ALTER ROLE newsboard SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE newsboard TO newsboard;
EOSQL
