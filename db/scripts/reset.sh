psql -h 127.0.0.1 -U postgres <<EOF
\x
REVOKE CONNECT ON DATABASE newsboard FROM public;  DROP DATABASE newsboard;  CREATE DATABASE newsboard;  CREATE USER newsboard WITH PASSWORD '123';  ALTER ROLE newsboard SET client_encoding TO 'utf8'; ALTER ROLE newsboard SET default_transaction_isolation TO 'read committed';  ALTER ROLE newsboard SET timezone TO 'UTC';  GRANT ALL PRIVILEGES ON DATABASE newsboard TO newsboard;
EOF
