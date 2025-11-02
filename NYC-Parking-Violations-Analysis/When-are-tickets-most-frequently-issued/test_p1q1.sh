#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/parking_violation_data.csv /project/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/project/mapper_p1q1.py -mapper ../../mapreduce-test-python/project/mapper_p1q1.py \
-file ../../mapreduce-test-python/project/reducer_p1q1.py -reducer ../../mapreduce-test-python/project/reducer_p1q1.py \
-input /project/input/* -output /project/output/
/usr/local/hadoop/bin/hdfs dfs -cat /project/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
../../stop.sh
