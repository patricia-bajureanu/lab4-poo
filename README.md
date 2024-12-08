Simulare Ecosistem
-
Descrierea proiectului
-
Acest proiect implementează o simulare a unui ecosistem natural în care plantele și animalele coexistă și interacționează între ele. Proiectul demonstrează utilizarea principiilor Programării Orientate pe Obiecte (OOP), cum ar fi moștenirea, polimorfismul, utilizarea claselor abstracte și a interfețelor.

Caracteristici principale:

- Creșterea și reproducerea plantelor.

- Deplasarea, hrănirea și reproducerea animalelor (erbivore, carnivore și omnivore).

- Interacțiunile dinamice dintre entități (mâncare, vânătoare, reproducere, moarte).

- Simulare controlată manual – utilizatorul avansează pașii de simulare apăsând Enter și poate opri simularea tastând stop.

- Raport final – la sfârșitul simulării, se generează un raport cu populația finală de plante și animale.

Descrierea claselor și ierarhiilor
-
Clasa abstractă EntitateEcosistem:

Această clasă definește structura de bază pentru toate entitățile ecosistemului, fie ele plante, fie animale. Toate clasele derivate moștenesc metodele și atributele acestei clase.

Atribute:

- nume – Numele entității.
- energie – Cantitatea de energie pe care o are entitatea.
- x, y – Coordonatele de poziție ale entității pe harta ecosistemului.
- rata_supravietuire – Parametru utilizat pentru creștere și supraviețuire.

Metode:

- actioneaza() – Metodă abstractă care trebuie implementată în clasele derivate.
- reproduce() – Reproducerea entității.

Clasa Planta:

Moștenește de la EntitateEcosistem. Plantele au o rată de creștere (rata_crescut), iar pe parcursul simulării își măresc energia și se pot reproduce.

Atribute:

- rata_crescut – Cantitatea de energie câștigată la fiecare pas de simulare.

Metode:

- actioneaza() – Crește energia plantei.
- reproduce() – Dacă energia plantei depășește 50, aceasta se reproduce.

Clasa abstractă Animal:

Aceasta este o clasă abstractă derivată din EntitateEcosistem. Toate animalele au atribute suplimentare precum viteza și tipul de hrană.

Atribute:

- viteza – Intervalul de deplasare al animalului (poate merge în orice direcție cu ± viteza).
- tip_hrana – Tipul de hrană consumată de animal (plante, animale sau ambele).

Metode:

- actioneaza() – Se deplasează și consumă energie.
- mananca(prada) – Metodă abstractă, trebuie implementată de subclase.
- deplaseaza() – Modifică poziția animalului pe hartă.

Subclase ale Animal:

Erbivor

- Mănâncă doar plante.
- Se deplasează pe hartă și, dacă găsește o plantă, o mănâncă.
- Metode: mananca(planta)

Carnivor
- Vânează alte animale pentru hrană.
- Dacă prinde un animal, îi consumă energia și se hrănește.
- Metode: mananca(prada)

Omnivor

- Poate mânca atât plante, cât și animale.
- Se hrănește cu orice entitate întâlnește, în afară de sine.
- Metode: mananca(entitate)

Clasa Ecosistem:

Această clasă gestionează întreaga hartă a ecosistemului și toate entitățile. Simulează interacțiunile dintre plante și animale și afișează un raport final al ecosistemului.

Atribute:

- latime, inaltime – Dimensiunile hărții ecosistemului.
- entitati – Lista de entități (plante și animale) din ecosistem.

Metode:

- adauga_entitate(entitate) – Adaugă o entitate în ecosistem.
- elimina_entitate(entitate) – Elimină o entitate moartă din ecosistem.
- simuleaza_pasu() – Simulează un pas de interacțiune pentru toate entitățile.
- raport_final() – Afișează raportul final al populației.

Explicația fiecărei metode
-
- EntitateEcosistem.actioneaza()
Declanșează comportamentul entității. Pentru animale, aceasta implică deplasarea și consumul de energie, iar pentru plante, creșterea energiei.
- EntitateEcosistem.reproduce()
Permite entității să se reproducă dacă sunt îndeplinite condițiile necesare (de exemplu, dacă energia depășește o anumită valoare).
- Animal.deplaseaza()
Animalul se deplasează la o poziție aleatorie pe hartă, în funcție de viteza sa. Direcția este aleasă aleatoriu.
- Animal.mananca(prada)
Animalul mănâncă o altă entitate (fie plantă, fie animal, în funcție de tipul animalului). Dacă entitatea este consumată, energia acesteia este transferată animalului.
- Ecosistem.adauga_entitate(entitate)
Adaugă o entitate (plantă sau animal) la ecosistem și o poziționează pe hartă.
- Ecosistem.elimina_entitate(entitate)
Elimină o entitate care a murit (de exemplu, din cauza lipsei de energie) din ecosistem.
- Ecosistem.simuleaza_pasu()
Simulează toate acțiunile entităților din ecosistem într-un singur pas. Fiecare entitate își realizează acțiunea proprie (plantele cresc, animalele se deplasează, se hrănesc și consumă energie). Entitățile cu energie 0 sunt eliminate.
- Ecosistem.raport_final()
Generează un raport final cu populațiile rămase la sfârșitul simulării. Sunt afișate tipurile de entități și numărul de indivizi din fiecare tip.
   
UML Diagram
-

                    +-------------------------+
                    |    EntitateEcosistem    |
                    +-------------------------+
                    | - nume: str              |
                    | - energie: int          |
                    | - x, y: int             |
                    | - rata_supravietuire: int|
                    +-------------------------+
                    | + actioneaza()          |
                    | + reproduce()           |
                    +-------------------------+
                               |
               +---------------+--------------+
               |                              |
         +-------------+              +---------------+
         |   Planta    |              |    Animal      |
         +-------------+              +---------------+
         | - rata_crescut: int        | - viteza: int  |
         | + actioneaza()             | - tip_hrana: str|
         | + reproduce()              | + deplaseaza() |
         +-------------+              | + mananca()    |
                                       +---------------+
                                             |
             +---------------+---------------+---------------+
             |               |               |
         +---------+     +---------+     +---------+
         | Erbivor |     | Carnivor|     | Omnivor |
         +---------+     +---------+     +---------+
         | + mananca()   | + mananca()   | + mananca() |
         +---------+     +---------+     +---------+

         +-----------------+
         |    Ecosistem     |
         +-----------------+
         | - latime: int    |
         | - inaltime: int  |
         | - entitati: list |
         +-----------------+
         | + adauga_entitate() |
         | + elimina_entitate()|
         | + simuleaza_pasu()  |
         | + raport_final()    |
         +-----------------+
Scenarii de utilizare
-
- Adăugarea entităților – Se creează plante, erbivore, carnivore și omnivore, care sunt adăugate în ecosistem.
- Simularea pas cu pas – Utilizatorul controlează avansarea simulării prin apăsarea Enter.
- Hrănirea animalelor – Carnivorele vânează erbivore, erbivorele mănâncă plante, omnivorele mănâncă plante și animale.
- Raport final – Se generează raportul final cu numărul de entități rămase.

Dificultăți întâlnite și soluții adoptate
-
- Interacțiuni complexe între entități

-Problema: Controlul acțiunilor diferite ale fiecărui tip de entitate.

-Soluție: S-a utilizat o ierarhie de clase cu moștenire OOP și polimorfism.
- Gestionarea pozițiilor animalelor

-Problema: Evitarea coliziunilor.

-Soluție: Animalele au poziții aleatorii și se deplasează în funcție de viteza lor.

- Control manual al simulării

-Problema: Oprirea simulării.

-Soluție: Utilizatorul controlează manual pașii de simulare.