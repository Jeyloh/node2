# Node



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


# Node2
## Skoleprosjekt av:
Daniel Eide, Jørgen Lybeck Hansen, Jonas Dam, Elaine Sajets, Christian Fredrik Thorne, Bastian Strang

## Informasjon
Gjennom semesteret har gruppen utført lab oppgaver. Alle labbene er testet med Python 2.7.6. 

## /lab1

lab1-svar.txt inneholder teoretiske svar til oppgaver fra lab1.
lab1.py inneholder oppgaver med python besvarelse i form av kode.



## /lab2

lab2.py inneholder funksjoner for å gjøre om desimal verdi til romerske tall og motsatt. Disse er hentet fra en annen git repository. Det er også implementert en addisjonsfunksjon. Den følger algoritmen fra http://turner.faculty.swau.edu/mathematics/materialslibrary/roman/ der den legger sammen to strings, trekker fra subtraksjoner, erstatter med nye romerske tall og viser til svaret. 

lab2_dict.py inneholder to lister med desimal og romerske referanse tall som blir tatt i bruk i int_to_roman() og roman_to_int().

## /lab3

client.py lager en UDP klient for å sende over små bokstaver til server.py, gjøre de om til bits, gjøre de til store bokstaver, gjøre de tilbake til ascii og printe dem ut. 

## /lab4

poker.py inneholder et pokerspill.

## /lab5

lab5.py inneholder teoribesvarelser.

