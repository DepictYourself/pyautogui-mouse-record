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
            print()

            timestr = line[:23] + "000"
            timeobj = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S,%f")
            deltatime = timeobj - starttime
            print(deltatime)
            starttime = timeobj
            dtimesec = timedelta.total_seconds(deltatime)
            dtimesecstr = (str)(dtimesec)
            print(dtimesecstr)

            

            # time format
            # timeobj.strftime("%Y-%m-%d %H:%M:%S,%f") + "\n"
            if(command[10:16] == "moveTo" and dtimesec > 0.015):
                outputfile.write(command)
                outputfile.write("pyautogui.PAUSE = " + dtimesecstr + "\n")
            else :
                if (command[10:16] == "moveTo"):
                    outputfile.write(command)
                else :
                    outputfile.write(command)
                    outputfile.write("pyautogui.PAUSE = " + dtimesecstr + "\n")
