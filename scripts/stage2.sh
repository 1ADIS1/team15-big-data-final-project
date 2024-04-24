password=$(<secrets.psql.pass)

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/db.hql > output/hive_results.txt
