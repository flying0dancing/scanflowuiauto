# -*- coding: utf-8 -*-
import subprocess

def killScanFlow():
    subprocess.call([r'Resources/kill_scanFlow.bat'])
    snooze(2)