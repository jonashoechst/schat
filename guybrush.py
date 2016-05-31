#!/usr/bin/env python
import os, random, time

lines = ["guybrush Look behind you, a Three-Headed Monkey!", 
        "guybrush That\\'s the second biggest exploit I\\'ve ever seen!",
        "guybrush I must have left it in my other pants.",
        "guybrush Is it over? ...Hello? ...Did we win?"
        ]
        
while True:
    line = random.choice(lines)
    os.system("/command/schat/schat-add "+line)
    time.sleep(random.randint(10, 30))