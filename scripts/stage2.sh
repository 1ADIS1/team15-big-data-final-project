#!/bin/bash
source secrets/.psql.pass

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n teamx -p $password -f sql/q1.hql --hiveconf hive.resultset.use.unique.column.names=false > output/q1.csv