# N-gram

Map Reduce Project for *Distributed Systems* 2020 Fall @ Fudan University, by [**Zuobai Zhang**](https://oxer11.github.io/)


## 文件说明

1. `n_gram.sh`：Map Reduce调用脚本，脚本中调用Hadoop命令，将map.py和reduce.py分别作为mapper和reducer执行Map Reduce过程。
2. `n_gram_slow.sh`：同上，慢速版本，将map.py和reduce.py分别作为mapper和reducer执行Map Reduce过程。
3. `main.py`：交互式代码，通过在代码中调用n_gram_slow.sh脚本完成运算任务。
4. `map.py`：带有stripe combiner优化的mapper
5. `reduce.py`：map.py对应的reducer
6. `map_slow.py`：带有combiner优化的mapper
7. `reduce_slow.py`：map_slow.py对应的reducer

## 使用方式

交互版本

``
python main.py
``

快速版本

``
sh ./ngram.sh 2
``


