import socket
import sys
import webbrowser

def is_connected():
    try:

        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


print("Hey there! Welcome to Windows images.Please note that all of the images are set to US english. Please make your choice: ")
print("1) Windows 11 (multiple editions)")
print("2) Windows 10 (multiple editions)")
print("3) Windows 8.1 (Pro / Core)")
print("4) Windows 7 (Ultimate SP1)")
print("5) Windows Vista (SP2)")
print("6) Windows XP (SP3)")

a = int(input())

if not is_connected():
    print("Unfortunetly, you don't seem to have a valid internet connection so you won't be able to continue with the download. Press any key to quit the program")
    input()
    sys.exit()

while a>6 or a<1:
    print("Please enter a valid input ")
    a = int(input())

if a == 1 :
    print("Since Windows 11 is still available on microsoft's website, you will be redirected to their website.")
    print("Press any key to continue...")
    input()
    webbrowser.open("https://www.microsoft.com/en-us/software-download/windows11")
elif a == 2 :
    print("Since Windows 10 is still available on microsoft's website, you will be redirected to their website")
    print("Press any key to continue...")
    input()
    webbrowser.open("https://www.microsoft.com/en-US/software-download/windows10")
elif a == 3 :
    print("Please make your choice: ")
    print("1) x64 edition")
    print("2) x86 edition")
    b = int(input())
    while b != 1 and b != 2:
        print("Please enter a valid input")
        b = int(input())
    if b == 1:
        webbrowser.open("https://software.download.prss.microsoft.com/dbazure/Win8.1_English_x64.iso?t=724a4b6e-737f-40f1-9634-850974cec1cc&P1=1755201974&P2=601&P3=2&P4=Vn3hbVUj1taBL7nnQtekB77bBsygLOGYcDM3%2fNHhRfCH6EwpQRp6sA%2bHLiycEf%2fB5tgqpyPcm13ZGqF8%2fZ3KNlaxauhob%2fMvv54ZIjYSmsVxSaVngd5FLnbFHsmoEZnBLKKMWLu0Suln8qSIMj8ozLlNbCsNqeTnCTyMMvgCR7F3bH9PqHP45rJj6iKuYIIB8iuzE7eTHqMUt%2f2QgQ2I2Ujji48p3%2fO0wcx4QzLkRWr4HQBslwC1LM9RpplM1lke6AQ%2f5kdmw8do9i5XQC8DdirBkXKa1C2MywTcfW1FKbCJghcyNqmlAx099a7emnX2WTVynuYEXnhRJd4jOYUpJg%3d%3d")
    elif b == 2:
        webbrowser.open("https://software.download.prss.microsoft.com/dbazure/Win8.1_English_x32.iso?t=724a4b6e-737f-40f1-9634-850974cec1cc&P1=1755201975&P2=601&P3=2&P4=MUGKlDrcKVhVDhxlVYq%2bhxd%2bD9F8BDl680imIA7xODuvwZrRNdzYu1QXQMXn08ofBUHJEnFFGz%2bOf0KFzPCSgT5cSXxtIfLCPxoUg6LqeT0jxXY5%2bfbYAMG22SRWr8PHyZ9gW74XG5n9oEyr%2bO8PMTy7fHtptG2ttD%2bDTh%2fyHCGv2qY0FgBYW80ySCKVC9dN%2fqr2RStG0a0uo3jv4igSjvdhLSFVOpTArcjhQpY6rF10OJ0SAkP1hFfnkHF1jApSlova4fmX9JZGP8IQnKbsVB4jxjWfI4rQ6pSnGDuF8%2fw3A22NB0ZKLJa0OuFTfd7G3fvcAdtrI8o5kt53Vd%2fXYg%3d%3d")
elif a == 4 :
    print("Please make your choice: ")
    print("1) x64 edition")
    print("2) x86 edition (download link kinda buggy idk why)")
    b = int(input())
    while b != 1 and b != 2:
        print("Please enter a valid input")
        b = int(input())
    if b == 1:
        webbrowser.open("https://api.isdn.network/api/v1/artifacts/7b3c9d42-bcb2-4c44-90d2-0bcff70f84d8/download")
    elif b == 2:
        webbrowser.open("https://api.isdn.network/api/v1/artifacts/49fc3b61-dfc8-4d74-a472-a78eda192514/download")
elif a == 5:
    print("Please make your choice: ")
    print("1) x64 edition")
    print("2) x86 edition")
    b = int(input())
    while b != 1 and b != 2:
        print("Please enter a valid input")
        b = int(input())
    if b == 1:
        webbrowser.open("https://drive.massgrave.dev/en_windows_vista_sp2_x64_dvd_342267.iso")
    elif b == 2:
        webbrowser.open("https://drive.massgrave.dev/en_windows_vista_with_sp2_x86_dvd_342266.iso")
elif a == 6:
    webbrowser.open("https://drive.massgrave.dev/en_windows_xp_professional_with_service_pack_3_x86_cd_vl_x14-73974.iso")
