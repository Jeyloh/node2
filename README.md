# Node
## Skoleprosjekt av:
Daniel Eide, Jørgen Lybeck Hansen, Jørn Utheim-Olsen, Jonas Dam, Elaine Sajets, Christian Fredrik Thorne, Bastian Strang



## Basic bruk av Git

1. git pull 

2. Arbeide med

3. git add filnavn.py (eller "." istedetfor filnavn.py for å legge til alt)

4. git commit -m "din kommentar"

5. git push origin master (eller navnet på branch)


## Når du pusher og får en merge conflict:

1. Kjør en git pull for å merge filene

2. Åpne filene og fiks alle steder som inneholder konflikter. Fjern git linjer osv.

3. Push filen når den er ordnet i. Git klarer å se at du har arbeidet med en fil som har vært i konflikt og vil derfor laste opp filen din uten problem etter å ha endret feil i en merge conflict.


## Linux Terminal Commands:

cat test.txt (shows the file)

echo "This is a test file." > test.txt (creates a new file with content

touch test.txt (creates new file)

ls (list objects)

mkdir (make directory)

ls *.py (henter alle python filer)

ls ex*

mv filnavn directory 

mv filnavn filnavn

sudo (work as superuser)

rm -r filnavn  (delete)

