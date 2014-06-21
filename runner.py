#! /usr/bin/env python3

from Bar import Bar
from Plugins import Time, Battery, CPU, Memory, MPD


my_bar = Bar(delay=3)
time = Time.Time("%H:%M")
bat = Battery.Battery()
mpd = MPD.MPD()
cpu = CPU.CPU()
mem = Memory.Memory()

my_bar.register_item(mem)
my_bar.register_item(cpu)
my_bar.register_item(bat)
my_bar.register_item(time)
my_bar.register_item(mpd)

my_bar.loop()
