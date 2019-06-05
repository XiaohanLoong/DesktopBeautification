sleep 20s
killall conky
cd "/home/loongxiaohan/.conky/CPUPanel/config"
conky -c "/home/loongxiaohan/.conky/CPUPanel/config/CPUPanel - 4 Core CPU" &
cd "/home/loongxiaohan/.conky/Gotham/config"
conky -c "/home/loongxiaohan/.conky/Gotham/config/Gotham" &
cd "/home/loongxiaohan/.conky/Metro/config"
conky -c "/home/loongxiaohan/.conky/Metro/config/conky.conf.12" &
cd "/home/loongxiaohan/.conky/Metro/config"
conky -c "/home/loongxiaohan/.conky/Metro/config/conky.conf.14" &
cd "/home/loongxiaohan/.conky/Metro"
conky -c "/home/loongxiaohan/.conky/Metro/conky.conf.12" &
