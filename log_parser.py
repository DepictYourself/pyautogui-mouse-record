import os
from datetime import datetime
from datetime import timedelta

pathDesktop = os.path.expanduser("~/Desktop")


with open(pathDesktop + "/mouse_log.txt", 'r') as inputfile:
    with open(pathDesktop + "/pyautogui_commands.txt", 'w') as outputfile:        
        starttime = inputfile.readline()
        starttime = datetime.strptime(starttime[:23]+"000", "%Y-%m-%d %H:%M:%S,%f")
        inputfile.seek(0)

        for line in inputfile:            
            command = line[25:]

            timestr = line[:23] + "000"
            timeobj = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S,%f")
            deltatime = timeobj - starttime
            starttime = timeobj
            dtimesecstr = (str)(deltatime.seconds)
            dtimemilsec = deltatime.microseconds * 1000
            dtimemilsecstr = (str)(dtimemilsec).rstrip('0')

            outputfile.write(command)

            # time format
            # timeobj.strftime("%Y-%m-%d %H:%M:%S,%f") + "\n"
            outputfile.write("time.sleep(" + dtimesecstr + "."+ dtimemilsecstr + ")\n")
