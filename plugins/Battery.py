#! /usr/bin/env python3
from BarItem import BarItem
import subprocess

class Battery(BarItem):

    def __init__(self, number=0):
        BarItem.__init__(self, "Battery")
        self.output['name'] = "Battery"
        self.number = number

    def update(self):
        args = ("cat", "/sys/class/power_supply/BAT0/energy_full_design") #to get a realistic value
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_full = popen.stdout.read().decode("utf-8").strip()

        args = ("cat", "/sys/class/power_supply/BAT0/energy_now")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_now = popen.stdout.read().decode("utf-8").strip()

        args = ("cat", "/sys/class/power_supply/BAT0/status")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        status = popen.stdout.read().decode("utf-8").strip()

        percentage = (int(bat_now) / int(bat_full)) * 100
        self.output['full_text'] = "Battery: " + '%.1f' % percentage + "%"

        if(status == "Charging"):
            self.output['color'] = "#0676cb"
        else:
            if(25 < percentage):
                self.output['color'] = "#FFFFFF"
            elif(10 < percentage <= 25):
                self.output['color'] = "#FFFF00"
            else:
                self.output['color'] = "#FF0000"

