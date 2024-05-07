#!/bin/bash
source secrets/.psql.pass

beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team15 -p $password -f sql/create_evaluation_tables.hql
