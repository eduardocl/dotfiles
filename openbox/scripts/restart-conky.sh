#!/bin/sh

#pid=`ps ax | grep -e "conky" | grep -e  "openbox" | awk '{print $1}'`
#echo $pid
#kill -9 $pid
killall conky
/usr/bin/conky -c /home/82035644020/.config/openbox/conkyrc.ecl.conf &
exit 0