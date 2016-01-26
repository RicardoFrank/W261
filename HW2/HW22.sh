
hdfs dfs -rm /tmp/enronemail_1h.txt
hdfs dfs -put enronemail_1h.txt /tmp/enronemail_1h.txt
hdfs dfs -rm -r /tmp/output_HW22
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.4.5.jar -file ~/test/wc_mapper.py ~/test/wc_reducer.py -mapper "python wc_mapper.py" -reducer "python wc_reducer.py" -input /tmp/enronemail_1h.txt -output /tmp/output_HW22
hdfs dfs -cat /tmp/output_HW22/part-00000