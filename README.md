# proiect-cloud-lor
Proiect Cloud Computing 2022 - 2023
Facultatea de Matematica si Informatica
Calculatoare si Tehnologia Informatiei

Grupa 361
Studenti participanti:
- Albei Liviu-Andrei
- Cojocaru Andrei-Laurentiu
- Codreanu Radu-Stefan

Scopul proiectului este acela de a incarca pe pagina .html un fisier video .mp4, aplicatia creand un fisier .jpg, un thumbnail pentru acel videoclip.
:-
  De asemenea, se introduce email-ul persoanei astfel incat aceasta sa fie notificata via mail in legatura cu faptul ca imaginea thumbnail a fost generata.
  Astfel, aplicatia foloseste serviciile Email si Storage Blob. Pe Storage Blob se incarca fisierul video de unde aplicatia urmeaza sa il descarce iar tot pe Blob se va incarca imaginea.
 
  De asemenea, serviciile Queue si CosmosDB sunt active, in momentul in care un thumbnail este creat, in queue, apare un mesaj specific iar email-ul persoanei este salvat in CosmosDB.


Pentru a realiza acest proiect, urmatoarele au fost necesare:
- o masina virtuala cu sistemul de operare Debian 11 Bullseye, creata folosing Microsoft Azure
- odata creata masina, conectarea se face prin cadrul wsl/PuTTy, folosind cheia SSH <.pem> ce a fost generata automat
- cheia .pem primeste acces 'chmod 400 key.pem'
- conectare (doar dupa ce se da acces!) -> ssh -i <key.pem> nume_user@public_ip
- dupa conectare se instaleaza librariile
- sudo apt-get update
- sudo apt-get install python3
- sudo apt-get install nginx -y
- sudo apt-get install python3-pip
- sudo apt-get install cron -y  + sudo crontab -e (pentru Script-ul de rulare cand se face tranzitia de la VM la Scale Set)
- sudo waagent -deprovision+user
- pip install requests
- pip install Flask - aplicatia pe care ruleaza server-ul
- pip install moviepy - thumbnail
- python3-m venv venv
- source venv/bin/activate
- pip install azure-storage-queue - pentru Azure
- pip install  azure-communication-email
- pip install  azure-communication-email
- pip install azure-storage-blob 
- pip install azure-identity
- sudo apt install ffmpeg - pentru generare thumbnail
- sudo apt install imagemagick

- dupa instalarea tuturor componentelor, se foloseste "sudo su -" pentru a accesa modul de root
- urmeaza crearea folderului in care o sa avem aplicatia, din "cd ~/" folosim "mkdir nume_proiect"
- "cd nume_proiect" si aici o sa executam "touch __init__.py"
- "__init__.py" contine codul pentru aplicatia Flask
