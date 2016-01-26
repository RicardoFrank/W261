
hdfs dfs -rm /tmp/enronemail_1h.txt
hdfs dfs -put enronemail_1h.txt /tmp/enronemail_1h.txt
hdfs dfs -rm -r /tmp/output_HW23
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.4.5.jar -file ~/test/nb_mapper.py ~/test/nb_reducer.py -mapper "python nb_mapper.py" -reducer "python nb_reducer.py" -input /tmp/enronemail_1h.txt -output /tmp/output_HW23
hdfs dfs -cat /tmp/output_HW23/part-00000