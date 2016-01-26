
hdfs dfs -rm /tmp/enronemail_1h.txt
hdfs dfs -put enronemail_1h.txt /tmp/enronemail_1h.txt
hdfs dfs -rm -r /tmp/output_HW24
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.4.5.jar -file ~/test/nb_mapper_laplace.py ~/test/nb_reducer_laplace.py -mapper "python nb_mapper_laplace.py" -reducer "python nb_reducer_laplace.py" -input /tmp/enronemail_1h.txt -output /tmp/output_HW24
hdfs dfs -cat /tmp/output_HW24/part-00000