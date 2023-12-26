# This is the old deleter where i was still in windows insiders. I am not in that crappy program anymore, so the buggy win.old deletion script is not needed anymore.
#This is the deleter for win.old folder
print('Checking if Windows.old Exists')
folder_path = "C:/Windows.old"

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    while True:
        antwort = input("The Deletion of Windows.old can take up to 2 Hours.  Do You want to continue? (yes/no): ")
        # if schleife antwort yes
        if antwort.lower() == 'yes':
            print("deleting Windows.old")

            # Den Thread starten
            mein_thread.start() 

            # Der Hauptprozess kann weitermachen, ohne auf das Unterprogramm zu warten
            print('')
            break  # Die Schleife beenden und das Programm fortsetzen.

        # if schleife nein
        elif antwort.lower() == 'no':
            textno = 'Leaving Windows.old as it is. You can also delete it with the "Disk Cleanup" Utility.'
            print(textno)
            # Hier kannst du den Code hinzufügen, den du ausführen möchtest, wenn die Antwort 'nein' ist.
            break  # Die Schleife beenden und das Programm beenden.

        else:
            print("please only respond with yes / no")
            # Die Schleife wird fortgesetzt, und der Benutzer wird erneut nach einer gültigen Antwort gefragt.

else:
    print('')
