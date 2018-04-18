#!/bin/bash
killall -9 non-mixer
killall -9 carla
killall -9 jackdbus
sleep 5
jack_control start & 
sleep 1
pulseaudio --start
cadence &
sleep 5 
pacmd unload-module module-jack-sink
pacmd unload-module module-jack-source
sleep 5

#pulseaudio bridges | in / out

pacmd load-module module-jack-source channels=2 source_name=voip-in client_name=voip-in connect=false
pacmd load-module module-jack-sink channels=2 sink_name=voip-out client_name=voip-out connect=false

pacmd load-module module-jack-sink channels=2 sink_name=games-out client_name=games-out connect=false

pacmd load-module module-jack-source channels=2 source_name=media-in client_name=media-in connect=false
pacmd load-module module-jack-sink channels=2 sink_name=media-out client_name=media-out connect=false


sleep 2
a2jmidid -e &
sleep 2
#killall mididings
#mididings -f ~/audio-scripts/midi-osc.py &
sleep 2
non-mixer --osc-port=15159 ~/audio-scripts/non.mix &
sleep 2

sleep 2

carla ~/audio-scripts/carla.presets/default.carxp &
sleep 3
wall "Audio systems up and running"
sleep 1
exit 0
