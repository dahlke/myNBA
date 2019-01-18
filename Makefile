MEMSQL_USER = root
MEMSQL_HOST = 127.0.0.1
MEMSQL_DATABASE = nba
BACKUP_DIR = backups
BACKUP_DATE = $(shell date +%Y_%m_%d_%H_%M)
BACKUP_PATH = ${BACKUP_DIR}/${BACKUP_DATE}.sql
NBA_MODERN_ERA_BACKUP_PATH = ${BACKUP_DIR}/1979_2018.sql

.PHONY: setup
setup:
	mysql -u ${MEMSQL_USER} -h ${MEMSQL_HOST} < sql/schema.sql

.PHONY: load
load: setup
	mysql -u ${MEMSQL_USER} -h ${MEMSQL_HOST} ${MEMSQL_DATABASE} < ${NBA_MODERN_ERA_BACKUP_PATH}

.PHONY: backup
backup:
	mysqldump -u ${MEMSQL_USER} -h ${MEMSQL_HOST} ${MEMSQL_DATABASE} > ${BACKUP_PATH}

.PHONY: logs
logs:
	tail -f my_nba.log

.PHONY: todo
todo:
	@ag "TODO" --ignore Makefile

.PHONY: notebook
notebook:
	jupyter notebook