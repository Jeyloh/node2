# Node
## Skoleprosjekt av:
Daniel Eide, Jørgen Lybeck Hansen, Jonas Dam, Elaine Sajets, Christian Fredrik Thorne, Bastian Strang



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


## Rebase

Use the git rebase command:

$ git rebase origin/master
This tells Git to replay commit C (your work) as if you had based it on commit B instead of A.
CVS and Subversion users routinely rebase their local changes on top of upstream work when they update before commit.
Git just adds explicit separation between the commit and rebase steps.

The graph of history now looks like this:

... o ---- o ---- A ---- B  origin/master (upstream work)
                          \
                           C'  master (your work)
Commit C' is a new commit created by the git rebase command.
It is different from C in two ways:

It has a different history: B instead of A.
It's content accounts for changes in both B and C: it is the same as M from the merge example.
Note that the history behind C' is still linear.
We have chosen (for now) to allow only linear history in cmake.org/cmake.git.
This approach preserves the CVS-based workflow used previously and may ease the transition.
An attempt to push C' into our repository will work (assuming you have permissions and no one has pushed while you were rebasing).

The git pull command provides a shorthand way to fetch from origin and rebase local work on it:

$ git pull --rebase
This combines the above fetch and rebase steps into one command.


