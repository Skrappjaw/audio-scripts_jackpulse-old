# This script os for bridging NANOkontrol 2 to work with non-mixer. Must have mididings installed for it to work.

# Get the mididings and OSC stuffs
from mididings import *
from mididings.extra.osc import SendOSC
from mididings.extra.osc import OSCInterface
hook(OSCInterface())

# Set up the OSC port 
#(you define it in non-mixer thanks to  "--osc-port=15159" option - no quotes)
port =  15159
 
#The actual conversion stuff
run(
   Filter(CTRL) >> CtrlSplit({
       # Non-mixer maping
       #It's always : /strip/[strip_name]/[effect_name]/[control_name]
       #Non-mixer uses values from 0.0 to 1.0. Therfore you have to divide by 127
       # Caution : 127.0 ( .0 !!). Check 'python's promotion' if you want to know why.

       #Pan Knobs for sends and sub mixes
       16: SendOSC(port, '/strip/VoipSend/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),


       #Fader Volumes
       1: SendOSC(port, '/strip/UMC-1/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       2: SendOSC(port, '/strip/UMC-2/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       3: SendOSC(port, '/strip/UMC-3/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       4: SendOSC(port, '/strip/UMC-4/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       5: SendOSC(port, '/strip/Game/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       6: SendOSC(port, '/strip/Music/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       7: SendOSC(port, '/strip/Voip/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),
       8: SendOSC(port, '/strip/System/Gain/Gain%20(dB)', lambda ev: ev.value / 127.0),

       # Mute Buttons
       48: SendOSC(port, '/strip/UMC-1/Gain/Mute', lambda ev: ev.value / 127.0),
       49: SendOSC(port, '/strip/UMC-2/Gain/Mute', lambda ev: ev.value / 127.0),
       50: SendOSC(port, '/strip/UMC-3/Gain/Mute', lambda ev: ev.value / 127.0),
       51: SendOSC(port, '/strip/UMC-4/Gain/Mute', lambda ev: ev.value / 127.0),
       52: SendOSC(port, '/strip/Game/Gain/Mute', lambda ev: ev.value / 127.0),
       53: SendOSC(port, '/strip/Music/Gain/Mute', lambda ev: ev.value / 127.0),
       54: SendOSC(port, '/strip/Voip/Gain/Mute', lambda ev: ev.value / 127.0),
       55: SendOSC(port, '/strip/System/Gain/Mute', lambda ev: ev.value / 127.0),
       32: SendOSC(port, '/strip/VoipSend/Gain/Mute', lambda ev: ev.value / 127.0),





   })
)
