import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = [] # Made it list

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username", "status"]) # Made it dict
        info["cpu_percent"] = proc.cpu_percent(None)
        info["meomory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

def PlatforServillence(FolderName):
    # -----------------------------------------------------

    border = "_"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to processed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("\nDirectory for the log file gets created successfully")

    # -----------------------------------------------------
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log"%timestamp)

    fobj = open(FileName,"w")
    print(f"\nLog file created successfully with name {FileName}")

    fobj.write(border+"\n")
    fobj.write("\nMarvellous Platform Servillence System\n")
    fobj.write("Log file gets created at: "+timestamp+"\n")
    fobj.write(border+"\n\n")
    fobj.write("---------- System report ----------")

    # CPU Information
    fobj.write("\nNumber of active CPU cores: %s \n" %psutil.cpu_count())
    fobj.write("CPU usage: %s %%\n" %psutil.cpu_percent())
    fobj.write(border+"\n")

    # RAM Information
    memory = psutil.virtual_memory()

    fobj.write("\nRAM usage: %s %%\n" %memory.percent)
    fobj.write("Total RAM avilable: %s \n" %memory.total) # Showing in result bytes
    fobj.write(border+"\n")

    # Network Usage
    netobj = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent: %.2f MB\n" %(netobj.bytes_sent/(1024 * 1024)))
    fobj.write("Recieve: %.2f MB\n" %(netobj.bytes_recv/(1024 * 1024)))
    fobj.write(border+"\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        # fobj.write(f"{info}\n")
        fobj.write("PID: %s\n" %info.get("pid"))
        fobj.write("Name: %s\n" %info.get("name"))
        fobj.write("User Name: %s\n" %info.get("username"))
        fobj.write("Status: %s\n" %info.get("status"))
        fobj.write("CPU Usage: %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM Usage: %.2f\n" %info.get("meomory_percent"))

        fobj.write(border+"\n")
    
    fobj.write(border+"\n")
    fobj.write("\n---------- End of log file ----------\n")
    fobj.write(border+"\n")

    fobj.close()

    # -----------------------------------------------------

def main():
    border = "_"*50

    print(border)
    print("\nMarvellous Platform Servillence System")
    print(border)

    # --h and --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("\nThis script use to perform")
            print("1: It fetch the information of running process")
            print("2: It fetch the information of running RAM")
            print("3: It fetch the information of Secondary Stroage")
            print("4: It fetch the information of microprocessor")
            print("5: It get auto scheduled periodically")
            print("6: It maintains all records into log file")
            print("7: It send the log files through mail periodically")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("\nUse the automation script as: ")
            print(f"Python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval: Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for the log file creation")
        else:
            print("\nUnable to proceed as there is no mathching argument")
            print("Please use --h or --u flag getting more details")
            

    # Main Business Logic
    elif(len(sys.argv) == 3):
        # PlatforServillence(sys.argv[2])

        # print("CPU usage: ", psutil.cpu_percent())
        print("\nScheduler started successfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minute.do(PlatforServillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1) # 1 is second

    else:
        print("\nInvalid number of argument")
        print("Unable to proceed as argument are not matching")
        print("Please use --h or --u flag getting more details")

    print(border)
    print("\nThan you for using out Automation System")
    print(border)

if __name__ == "__main__":
    main()