#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/shot_logs.csv /project/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/project/centroids.txt \
-file ../../mapreduce-test-python/project/mapper_p2q2.py -mapper ../../mapreduce-test-python/project/mapper_p2q2.py \
-file ../../mapreduce-test-python/project/reducer_p2q2.py -reducer ../../mapreduce-test-python/project/reducer_p2q2.py \
-input /project/input/* -output /project/output/
/usr/local/hadoop/bin/hdfs dfs -cat /project/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project/output/
../../stop.sh
