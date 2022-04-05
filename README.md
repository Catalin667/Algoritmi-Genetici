# Algoritmi-Genetici
Implementaţi un algoritm genetic pentru determinarea maximului unei funcţii pozitive pe un domeniu
dat (funcţia se va fixa în cod)
<br> Date de intrare:
- dimensiunea populaţiei
- domeniul de definiţie al funcţiei
- parametri pentru functia de maximizat (coeficientii polinomului de grad 2)
- precizia cu care se lucrează (cu care se discretizează intervalul)
- probabilitatea de recombinare (crossover, încrucişare)
- probabilitatea de mutaţie
- numărul de etape ale algoritmului
Ieşire:
- Un fişier text sugestiv care evidenţiază operaţiile din prima etapă a algoritmului, (de
exemplu fişierului Evolutie.txt (obţinut pentru funcţia –x2+x+2, domeniul [-1, 2],
dimensiunea populaţiei 20, precizia 6, probabilitatea de recombinare 0.25, probabilitatea de
mutaţie 0.01 şi 50 de etape))
- Bonus: Interfaţă grafică sugestivă, care evidenţiază evoluţia algoritmului

În fişier sunt scrise:
<br>
● populaţia iniţială sub forma
i: reprezentare cromozom x = valoarea corespunzătoare cromozomului în domeniul de definiţie
al funcţiei f =valoarea corespunzătoare cromozomului (f(Xi)) <br>
● probabilităţile de selecţie pentru fiecare cromozom <br>
![image](https://user-images.githubusercontent.com/79132416/161714483-42da4579-471e-453d-8a70-9b8d2cc14014.png)
<br>
● probabilităţile cumulate care dau intervalele pentru selecţie ![image](https://user-images.githubusercontent.com/79132416/161714671-cee54509-b7db-4b23-aa53-9517a009c724.png)
<br>
● evidenţierea procesul de selecţie, care constă în generarea unui număr aleator u uniform pe
[0,1) şi determinarea intervalului [qi
, qi+1) căruia aparține acest număr; corespunzător acestui
interval se va selecta cromozomul i+1. Procesul se repetă până se selectează numărul dorit de
cromozomi. Cerinţă: căutarea intervalului corespunzător lui u se va face folosind căutarea
binară.<br>
● evidenţierea cromozomilor care participă la recombinare<br>
● pentru recombinările care au loc se evidenţiază perechile care participă la recombinare,
punctul de rupere generat aleator precum şi cromozomii rezultaţi în urma recombinării (sau,
după caz, se evidenţiază tipul de încrucişare ales)<br>
● populaţia rezultată după recombinare<br>
● populaţia rezultată după mutaţii<br>
● pentru restul generaţiilor (populaţiilor din etapele următoare) se vor afişa doar valoarea
maximă ![image](https://user-images.githubusercontent.com/79132416/161714975-0ea9daeb-43a2-40e4-8848-428e6864bbbc.png)
și valoarea medie a performanței ![image](https://user-images.githubusercontent.com/79132416/161715043-d3a30ea0-1c8f-49ce-b888-2df62fe15c0c.png)
