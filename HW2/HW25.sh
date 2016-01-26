
hdfs dfs -rm /tmp/enronemail_1h.txt
hdfs dfs -put enronemail_1h.txt /tmp/enronemail_1h.txt
hdfs dfs -rm -r /tmp/output_HW25
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.4.5.jar -file ~/test/nb_mapper_laplace_over3.py ~/test/nb_reducer_laplace_over3.py -mapper "python nb_mapper_laplace_over3.py" -reducer "python nb_reducer_laplace_over3.py" -input /tmp/enronemail_1h.txt -output /tmp/output_HW25
hdfs dfs -cat /tmp/output_HW25/part-00000