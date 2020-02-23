#!/bin/bash
killall -9 carla
killall -9 jackdbus
killall -9 pulseaudio
sleep 5
jack_control start & 
sleep 1
pulseaudio --start
cadence &
sleep 2
pacmd unload-module module-jack-sinkc
pacmd unload-module module-jack-source
sleep 2

#pulseaudio bridges | in / out

pacmd load-module module-jack-source channels=2 source_name=voip-in client_name=voip-in connect=false
pacmd load-module module-jack-sink channels=2 sink_name=voip-out client_name=voip-out connect=false

pacmd load-module module-jack-sink channels=2 sink_name=games-out client_name=games-out connect=false

pacmd load-module module-jack-source channels=2 source_name=media-in client_name=media-in connect=false
pacmd load-module module-jack-sink channels=2 sink_name=media-out client_name=media-out connect=false


sleep 2
a2jmidid -e &
sleep 2
Mixbus5 &
sleep 5
carla &
sleep 3
wall "Audio systems up and running"
sleep 1
exit 0
