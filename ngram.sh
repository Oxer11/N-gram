#!/bin/bash


set -e
set -u

echo "Running the $1-gram algorithm..."
K=$1

hadoopJar="/home/u17300240035/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar"
input="/corpus/news_sohusite.xml"
output="/user/u17300240035/${K}gram"
#删除输出路径
hadoop fs -test -e "${output}" && hadoop fs -rm -r "${output}" 

#hadoop jar "${hadoopJar}" \
mapred streaming \
-mapper "python map.py -k=${K}"  \
-reducer "python reduce.py" \
  -file "map.py"    \
  -file "reduce.py" \
-input "${input}" \
-output "${output}" 
