
python random_gen.py 10000 > 10000_rand_list
hdfs dfs -rm /tmp/10000_rand_list
hdfs dfs -put 10000_rand_list /tmp/10000_rand_list
hdfs dfs -rmdir -r /tmp/output_HW21
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.4.5.jar -file ~/test/sort_mapper.py ~/test/top_10_reducer.py -mapper "python sort_mapper.py" -reducer "python top_10_reducer.py" -input /tmp/10000_rand_list -output /tmp/output_HW21
hdfs dfs -cat /tmp/output_HW21/part-00000