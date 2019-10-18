# Artificial Intelligence first homework
Legyen adott egy reptéri hosszútávú parkoló, ahol akárhetekig parkolhatnak tetszőleges méretű gépjárművek,
azaz autók, buszok, motorkerékpárok. A célunk az, hogy minden járműnek legyen helye a parkolóban,
a járművek egyedi hozzáférhetőségtől most eltekintünk.
###Bemenet
A bemenet tabulátorokkal tagolt szöveges adat, amely elsősorában a parkolóhosszátés szélességét,
második sorában a járművek számát, utána soronként egy-egy járműhosszátés szélességét tartalmazza.

**Példa:**
```
5   7
7
4   2
3   2
1   2
2   5
2   2
2   1
3   1
```
### Kimenet
Kimenetként írja a **_P_** mátrixot a standard outputra, tabulátorokkal tagolt formátumban.
```
1   1   1   1   4   4   6
1   1   1   1   4   4   6
2   2   3   3   4   4   7
2   2   5   5   4   4   7
2   2   5   5   4   4   7
```
