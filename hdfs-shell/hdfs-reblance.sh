#!/bin/bash

##########################################################################################
# - Copyright(C), 2017-2020, Pokyu Tung
# - File name: hdfs_reblance.sh
# - Author: Pokyu Tung    Version: 1.0    Date: 2017-12-23
# - Description: //用于详细说明程序文件完成的主要功能，与其它模块或函接口，输出值，取值范
#				   围，含意及参数间的控制、顺序、独立或依赖等关系
# - Others: 
# - Function List: //主要函数列表，每条记录应包括函数名及功能简要说明
#   - 1. ...
#   - 2. ... 
# - History: 
#   - 1. Date: ...
#        Author: ...
#        Modification: ...
#   - 2. ...
##########################################################################################

# source /opt/hadoopclient/bigdata_env admin

# beeline
# min1 = `hadoop dfsadmin -report |awk -F ':' '/DFS Used%/'|sed '1d'|cut -c 12-13|sort|head -n 1`
# max1 = `hadoop dfsadmin -report |awk -F ':' '/DFS Used%/'|sed '1d'|cut -c 12-13|sort|tail -n 1`


hadoop dfsadmin -report |awk -F ':' '/DFS Used%/'|sed '1d'|cut -c 12-13|sort > auto_temp.tmp
# cat auto_temp.tmp

max=`cat auto_temp.tmp |tail -n 1`
min=`cat auto_temp.tmp |head -n 1`

printf "min = $min\n"
printf "max = $max"

val=`expr $max - $min`

if [ $val -gt 10 ]
then 
  echo "reblance"
  $HADOOP_HOME/bin/start-balancer.sh -t 10%
else
  echo "no reblance"
fi