MEMSQL_USER = root
MEMSQL_HOST = 127.0.0.1
MEMSQL_DATABASE = nba
BACKUP_DATE = $(shell date +%Y_%m_%d_%H_%M)
BACKUP_PATH = backups/${BACKUP_DATE}.sql

.PHONY: backup
backup:
	mysqldump -u ${MEMSQL_USER} -h ${MEMSQL_HOST} ${MEMSQL_DATABASE} > ${BACKUP_PATH}

