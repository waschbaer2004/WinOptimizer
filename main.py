import os
import time
import threading
import subprocess

print('Jannis WinOptimizer V0.1')  # Press Ctrl+F8 to toggle the breakpoint.

print('If there are any Errors that say process not found, it means that the processes are not running.')
print('The running processes will still be killed!')
#time.sleep(5)
#kill all edge and onedrive tasks
#os.system('Taskkill /IM msedge.exe /F')
#os.system('Taskkill /IM edge.exe /F')
#os.system('Taskkill /IM msedgewebview2.exe /F')
#os.system('Taskkill /IM onedrive.exe /F')
#os.system('Taskkill /IM Widgets.exe /F')
#os.system('Taskkill /IM SearchHost.exe /F')
# os.system('Taskkill /IM msedge.exe /F')
# os.system('Taskkill /IM msedge.exe /F')
# os.system('Taskkill /IM msedge.exe /F')
# os.system('Taskkill /IM msedge.exe /F')
# os.system('Taskkill /IM msedge.exe /F')
# Delete Edge folder:

print('Deleting Edge and Onedrive Folders.')
#os.system('rd /s /q "C:/ProgramData/Microsoft OneDrive"')
#os.system('rd /s /q "C:/Program Files (x86)/Microsoft"')
#os.system('rd /s /q "%userprofile%/OneDrive"')

# Programm um Win.old zu löschen, weil das nicht in der While schleife stehen darf. Wird aber nicht benutzt,
# solange man es nicht aufruft

def mein_unterprogramm():
    print('winoldscript called --> Deleting Win.old')
    # os.system('TAKEOWN /F %SystemDrive%/Windows.old /A /R /D Y')
    # os.system('ICACLS %SystemDrive%/Windows.old /T /grant :r Administrators:F')
    # os.system('RD /S /Q %SystemDrive%/Windows.old')
    print('This is winold script')
    print("rm winold is running...")
    time.sleep(5)
    print("closing process")

#Programm was alles an unnötigen Tasks Löschen kann. Hauptsächlich für mist edge
def delete_task(task_name):
    try:
        subprocess.run(['schtasks', '/delete', '/tn', task_name, '/f'], check=True)
        print('')
    except subprocess.CalledProcessError as e:
        print('')

#erstellt den Thread schonmal, für den fall das windeleter zum einsatz kommt.
mein_thread = threading.Thread(target=mein_unterprogramm)



#if schleife von Windeleter beendet
print('')
print('')
print('now cleaning task scheduler, for better performance on computer startup')
print('If there are any Errors, that means that the Tasks dont exist, or are already deleted')

delete_task('testtttt2')
delete_task('testtttt1')
delete_task('MicrosoftEdgeUpdateTaskMachineUA')
delete_task('MicrosoftEdgeUpdateTaskMachineCore')
delete_task('MicrosoftEdgeUpdateBrowserReplacementTask')





#Checkt ob der Unterprozess noch läuft, und lässt solange eine warnung laufen bis der Prozess fertig ist.
# Ende des programms, damit das Programm noch auf Win.old deleter wartet
while True:
    if mein_thread.is_alive():
       print("Delete Win.old is still running ")
       time.sleep(3)
    else:
       print("")
       break


print('Done!')