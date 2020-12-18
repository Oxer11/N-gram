#!/bin/bash


set -e
set -u

echo "Running the $1-gram algorithm..."
K=$1
echo "Predicting the probability of $2"
input_txt=$2

hadoopJar="/home/u17300240035/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar"
input="/corpus/news_sohusite.xml"
output="/user/u17300240035/test"
#删除输出路径
hadoop fs -test -e "${output}" && hadoop fs -rm -r "${output}" 

#hadoop jar "${hadoopJar}" \
mapred streaming \
-mapper "python map_slow.py -k=${K} --input ${input_txt}"  \
-reducer "python reduce_slow.py" \
  -file "map_slow.py"    \
  -file "reduce_slow.py" \
-input "${input}" \
-output "${output}" 
