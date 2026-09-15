#!/bin/bash

set -e
set -u

function create_user_and_database() {
    local database=$1
    local username=$2
    local password=$3
    echo "Ensuring user '$username' and database '$database' exist"

    if ! psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_roles WHERE rolname = '$username'" | grep -q 1; then
        psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
            CREATE USER "$username" WITH PASSWORD '$password';
EOSQL
    fi

    if ! psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_database WHERE datname = '$database'" | grep -q 1; then
        psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -c "CREATE DATABASE \"$database\""
    fi

    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -c "GRANT ALL PRIVILEGES ON DATABASE \"$database\" TO \"$username\""
    echo "  User '$username' and database '$database' are ready"
}

# Metadata database
create_user_and_database $METADATA_DATABASE_NAME $METADATA_DATABASE_USERNAME $METADATA_DATABASE_PASSWORD

# Celery result backend database
create_user_and_database $CELERY_BACKEND_NAME $CELERY_BACKEND_USERNAME $CELERY_BACKEND_PASSWORD

# ELT database
create_user_and_database $ELT_DATABASE_NAME $ELT_DATABASE_USERNAME $ELT_DATABASE_PASSWORD

echo "All databases and users created successfully"