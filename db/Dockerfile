FROM postgres:10
COPY scripts/entrypoint.sh /docker-entrypoint-initdb.d/init-user-db.sh
COPY scripts/reset.sh /reset.sh
#ENTRYPOINT ["/entrypoint.sh"]
