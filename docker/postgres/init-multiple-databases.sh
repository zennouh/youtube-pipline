#!/bin/bash

set -e
set -u

function create_database_if_not_exists() {
    local database=$1
    local username=$2

    echo "Ensuring database '$database' exists (owned by '$username')"

    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
        SELECT 'CREATE DATABASE "$database"'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$database')\gexec
EOSQL

    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
        GRANT ALL PRIVILEGES ON DATABASE "$database" TO "$username";
EOSQL

    echo "  Database '$database' is ready"
}

# Collect (database,username) pairs, then dedupe by database name
declare -A seen_databases

for pair in \
    "$METADATA_DATABASE_NAME:$METADATA_DATABASE_USERNAME" \
    "$CELERY_BACKEND_NAME:$CELERY_BACKEND_USERNAME" \
    "$ELT_DATABASE_NAME:$ELT_DATABASE_USERNAME"
do
    db="${pair%%:*}"
    user="${pair##*:}"

    if [[ -z "${seen_databases[$db]:-}" ]]; then
        create_database_if_not_exists "$db" "$user"
        seen_databases[$db]=1
    else
        echo "Skipping '$db' - already created in this run"
    fi
done

echo "All databases created successfully"