"""Report 3 additional paragraph translations."""

PASS2_R3: list[tuple[str, str]] = [
    (
        "Przyjęte konwencje kodowania zmiennych ankietowych:",
        "Survey variable coding conventions:",
    ),
    (
        "- **CZY\\_KIER** — czy pracownik zajmuje stanowisko kierownicze (Nie/Tak);\n- **PYT\\_2** — odpowiedź na pytanie 2 w skali porządkowej $\\{-2,-1,1,2\\}$\n  (w danych nie występuje wartość 0);\n- **STAŻ** — staż pracy w trzech kategoriach: `1 = <1 rok`,\n  `2 = 1–3 lata`, `3 = >3 lata`;\n- **CZY\\_ZADW**, **CZY\\_ZADW\\_2** — zadowolenie ze szkoleń odpowiednio\n  w pierwszym i drugim badanym okresie. Zmienne zdefiniowano jako binaryzację\n  pytań `PYT_2` oraz `PYT_3` względem zera (odpowiedź dodatnia $\\Rightarrow$\n  „Tak”, ujemna $\\Rightarrow$ „Nie”); ponieważ żadne z tych pytań nie\n  przyjmuje wartości 0, podział jest jednoznaczny.",
        "- **CZY\\_KIER** — whether the employee holds a management role (Nie/Tak);\n- **PYT\\_2** — response to question 2 on ordinal scale $\\{-2,-1,1,2\\}$ (no zero in data);\n- **TENURE** — three categories: `<1 year`, `1–3 years`, `>3 years`;\n- **CZY\\_ZADW**, **CZY\\_ZADW\\_2** — training satisfaction in periods 1 and 2, binarized from `PYT_2`/`PYT_3` (positive $\\Rightarrow$ \"Tak\", negative $\\Rightarrow$ \"Nie\").",
    ),
    (
        "Dla tablicy $2\\times2$ z liczebnościami $n_{ij}$ hipoteza symetrii sprowadza\nsię do $H_0:\\ p_{12} = p_{21}$ (komórki na przekątnej nie wpływają na test).\nW **teście warunkowym** rozumujemy warunkowo względem sumy liczebności\npozaprzekątniowych $m = n_{12} + n_{21}$. Przy $H_0$ każda z $m$ obserwacji\n„niezgodnych” trafia do komórki $(1,2)$ z prawdopodobieństwem $\\tfrac12$,\nzatem",
        "For a $2\\times2$ table, symmetry is $H_0:\\ p_{12} = p_{21}$. In the **conditional test** we condition on $m = n_{12} + n_{21}$. Under $H_0$, discordant counts follow $\\mathrm{Bin}(m,\\tfrac12)$, so",
    ),
    (
        "Dwustronną p-wartość wyznaczamy podwajając mniejszy z ogonów rozkładu\ndwumianowego:",
        "The two-sided p-value doubles the smaller binomial tail:",
    ),
    (
        "Dane (reakcja na lek po godzinie; ten sam pacjent dla obu leków):",
        "Data (drug reaction after one hour; same patient for both drugs):",
    ),
    (
        "Liczebności pozaprzekątniowe: $n_{12} = 5$ (negatywna na A, pozytywna na B)\noraz $n_{21} = 2$ (pozytywna na A, negatywna na B). Hipoteza\n$H_0$: leki są jednakowo skuteczne ($p_{12} = p_{21}$).",
        "Off-diagonal: $n_{12}=5$, $n_{21}=2$. $H_0$: equal efficacy.",
    ),
    (
        "**Wyniki.** Test McNemara z poprawką na ciągłość daje statystykę\n$\\chi^2 = (|5-2|-1)^2/(5+2) = 4/7 \\approx 0{,}571$ ($p \\approx 0{,}450$). Test\nwarunkowy zwraca $p = 2\\cdot\\mathrm{Bin}(X\\le 2;\\,7,\\,0{,}5) \\approx 0{,}453$.\nObie p-wartości są niemal identyczne i znacznie większe od $0{,}05$.",
        "**Results.** McNemar: $\\chi^2 \\approx 0.571$ ($p \\approx 0.450$). Conditional: $p \\approx 0.453$. Both well above $0.05$.",
    ),
    (
        "**Wniosek.** Brak podstaw do odrzucenia $H_0$ — dane nie dają dowodu na to,\nże leki różnią się skutecznością. Mała próba ($m = 7$ niezgodnych par)\noznacza zarazem niewielką moc testu.",
        "**Conclusion.** Insufficient evidence to reject $H_0$; small sample ($m=7$) implies low power.",
    ),
    (
        "Na podstawie zmiennych `CZY_ZADW` (okres 1) i `CZY_ZADW_2` (okres 2)\nbudujemy tablicę $2\\times2$ i testujemy model symetrii.",
        "Using `CZY_ZADW` and `CZY_ZADW_2` we build a $2\\times2$ table and test symmetry.",
    ),
    (
        "**Wyniki.** Wśród par niezgodnych $n_{12} = 20$ pracowników zmieniło status\nz „Nie” na „Tak”, a jedynie $n_{21} = 8$ z „Tak” na „Nie”. Test McNemara z\npoprawką daje $\\chi^2 \\approx 4{,}32$ ($p \\approx 0{,}038$), a test warunkowy\n$p \\approx 0{,}036$. Obie p-wartości są mniejsze niż $\\alpha = 0{,}05$.",
        "**Results.** $n_{12}=20$ (Nie→Tak), $n_{21}=8$ (Tak→Nie). McNemar $p\\approx0.038$; conditional $p\\approx0.036$. Both below $\\alpha=0.05$.",
    ),
    (
        "Dane z Tabeli 2 z treści zadania — odpowiedzi na to samo pytanie (ocena\npodejścia firmy) udzielone przez $n = 200$ pracowników w pierwszym\n(wiersze) i drugim (kolumny) okresie badania:",
        "Task Table 2 data — same question from $n=200$ employees in periods 1 (rows) and 2 (columns):",
    ),
    (
        "Dla tablicy $k\\times k$ uogólnieniem testu McNemara jest **test Bowkera**:",
        "For $k\\times k$ tables, **Bowker's test** generalizes McNemar:",
    ),
    (
        "z liczbą stopni swobody równą liczbie par $(i,j),\\ i<j$.",
        "with df equal to the number of pairs $(i,j),\\ i<j$.",
    ),
    (
        "**Zero-count problem.** Para kategorii $(0,2)$, tj. komórki $(3,5)$ i $(5,3)$,\nma $n_{35}+n_{53} = 0+0 = 0$, co prowadzi do dzielenia $0/0$ (funkcja\n`mcnemar.test` zwraca wówczas `NaN`). Para ta wnosi zerowy wkład do\nstatystyki, dlatego pomijamy ją w sumie i zmniejszamy liczbę stopni swobody\ndo $9$ (problem omówiony szerzej w zadaniu dodatkowym 1\\*).",
        "**Zero-count problem.** Pair $(0,2)$ yields $0/0$; omit and use df $=9$ (see task 1*).",
    ),
    (
        "**Wyniki.** $\\chi^2_B \\approx 10{,}57$. Przy $\\mathrm{df}=9$ otrzymujemy\n$p \\approx 0{,}306$, a przy nominalnym $\\mathrm{df}=10$ — $p \\approx 0{,}392$.\nW obu przypadkach $p > 0{,}05$.",
        "**Results.** $\\chi^2_B \\approx 10.57$; $p\\approx0.306$ (df=9) or $0.392$ (df=10). Both $p>0.05$.",
    ),
    (
        "**Wniosek.** Brak podstaw do odrzucenia hipotezy symetrii — rozkład\nodpowiedzi w obu okresach jest zgodny z modelem symetrii. Wobec tego\n**nie ma dowodu na zmianę oceny podejścia firmy**: odpowiedzi w pierwszym\ni drugim okresie są statystycznie nieodróżnialne pod względem symetrii\nrozkładu.",
        "**Conclusion.** No evidence against symmetry; **no evidence of change** in company approach rating.",
    ),
    (
        "Porównujemy skuteczność leczenia A (nowa procedura) i B (stara procedura)\nna całej grupie oraz w podgrupach względem występowania chorób\nwspółistniejących.",
        "We compare treatments A (new) and B (old) overall and by comorbidity.",
    ),
    (
        "**Wyniki.** Dla **całej grupy** lepsza okazuje się metoda B\n(80,1\\% vs 52,9\\% poprawy; $\\mathrm{OR} = 0{,}28 < 1$, czyli szanse\npoprawy są mniejsze przy A). Jednak **w obu podgrupach to metoda A jest\nlepsza**: u pacjentów z chorobami współistniejącymi 14,4\\% vs 5,3\\%\n($\\mathrm{OR} = 3{,}03$), a u pacjentów bez chorób — 97,1\\% vs 95,6\\%\n($\\mathrm{OR} = 1{,}52$).",
        "**Results.** Overall B looks better (80.1% vs 52.9%); **in both subgroups A is better**.",
    ),
    (
        "Przyjmujemy: zmienna **1 = CZY\\_KIER**, **2 = PYT\\_2**, **3 = STAŻ**.\nNiech $\\pi_{ijk}$ oznacza prawdopodobieństwo komórki $(i,j,k)$. Notacja\nnawiasowa wskazuje najwyższe (zachowane) składniki interakcyjne modelu\nhierarchicznego.",
        "Variables **1=CZY\\_KIER**, **2=PYT\\_2**, **3=TENURE**. $\\pi_{ijk}$ is cell probability; brackets show retained interactions.",
    ),
    (
        "**Comment.** Modele $[1\\ 3]$ i $[13]$ dotyczą tablicy dwuwymiarowej\n(zmienne 1 i 3): pierwszy zakłada niezależność, drugi jest nasycony.\nModele trójwymiarowe układają się od najbardziej restrykcyjnego\n(całkowita niezależność $[1\\ 2\\ 3]$), przez niezależność jednej zmiennej od\npary pozostałych ($[12\\ 3]$, $[1\\ 23]$), po niezależność warunkową\n($[12\\ 13]$, w której obecność wspólnej zmiennej dopuszcza zależność z nią obu\npozostałych, ale nie między nimi nawzajem).",
        "**Comment.** Two-way models $[1\\ 3]$, $[13]$; three-way from complete independence to conditional independence $[12\\ 13]$",
    ),
    (
        "$P(\\text{PYT\\_2}=2 \\mid \\text{kierownik}) \\approx 0{,}481$ — prawie połowa\n  kierowników jest zdecydowanie zadowolona ze szkoleń;",
        "$P(\\text{PYT\\_2}=2 \\mid \\text{manager}) \\approx 0.481$ — nearly half of managers strongly satisfied;",
    ),
    (
        "$P(\\text{kierownik} \\mid \\text{staż}<1\\text{ rok}) \\approx 0{,}024$ — wśród\n  najmłodszych stażem niemal nikt nie jest kierownikiem;",
        "$P(\\text{manager} \\mid \\text{tenure}<1\\text{ year}) \\approx 0.024$;",
    ),
    (
        "$P(\\text{nie kierownik} \\mid \\text{staż}>3\\text{ lata}) \\approx 0{,}526$.",
        "$P(\\text{non-manager} \\mid \\text{tenure}>3\\text{ years}) \\approx 0.526$.",
    ),
    (
        "**Results (model $[12\\ 23]$).** Pierwsze prawdopodobieństwo pozostaje takie\nsamo ($\\approx 0{,}481$), ponieważ model $[12\\ 23]$ zachowuje pełną zależność\npary (CZY\\_KIER, PYT\\_2). Pozostałe dwa zmieniają się, bo zależność\nCZY\\_KIER–STAŻ jest teraz „filtrowana” przez PYT\\_2 (warunkowa niezależność\n1 i 3 przy ustalonym 2): $P(\\text{kier}\\mid\\text{staż}<1) \\approx 0{,}128$\noraz $P(\\text{nie kier}\\mid\\text{staż}>3) \\approx 0{,}778$. Model wygładza\nskrajne oszacowania empiryczne, „pożyczając” informację między warstwami\nzmiennej PYT\\_2.",
        "**Results (model $[12\\ 23]$).** First probability unchanged; others shift as CZY\\_KIER–TENURE is filtered through PYT\\_2.",
    ),
    (
        "Każdą hipotezę weryfikujemy jako dopasowanie odpowiedniego modelu\nlog-liniowego względem modelu nasyconego. Statystyka ilorazu wiarogodności\n$G^2$ (dewiancja) ma przy $H_0$ rozkład $\\chi^2$ o liczbie stopni swobody\nrównej różnicy liczby parametrów.",
        "Each hypothesis: log-linear model vs saturated model; $G^2$ deviance is $\\chi^2$ under $H_0$.",
    ),
    (
        "1. **Wzajemna niezależność** $[1\\ 2\\ 3]$: $G^2 \\approx 42{,}24$,\n   $\\mathrm{df}=17$, $p \\approx 0{,}0006 < 0{,}05$ — **odrzucamy** $H_0$.\n   Zmienne CZY\\_KIER, PYT\\_2 i STAŻ **nie są** wzajemnie niezależne.",
        "1. **Mutual independence** $[1\\ 2\\ 3]$: reject $H_0$ ($p\\approx0.0006$).",
    ),
    (
        "2. **PYT\\_2 niezależna od pary (CZY\\_KIER, STAŻ)** $[2\\ 13]$:\n   $G^2 \\approx 23{,}15$, $\\mathrm{df}=15$, $p \\approx 0{,}081 > 0{,}05$ —\n   **brak podstaw do odrzucenia** $H_0$ (wynik jest jednak na granicy\n   istotności). Można przyjąć, że zadowolenie PYT\\_2 nie zależy od łącznego\n   układu stanowiska i stażu.",
        "2. **PYT\\_2 independent of (CZY\\_KIER, TENURE)** $[2\\ 13]$: insufficient evidence to reject ($p\\approx0.081$).",
    ),
    (
        "3. **PYT\\_2 niezależna od CZY\\_KIER przy ustalonym STAŻ** $[13\\ 23]$:\n   $G^2 \\approx 4{,}88$, $\\mathrm{df}=9$, $p \\approx 0{,}845 > 0{,}05$ —\n   **brak podstaw do odrzucenia** $H_0$. Po uwzględnieniu stażu zadowolenie\n   ze szkoleń nie zależy już od zajmowanego stanowiska.",
        "3. **PYT\\_2 independent of CZY\\_KIER given TENURE** $[13\\ 23]$: insufficient evidence to reject ($p\\approx0.845$).",
    ),
    (
        "**Comment on the figure.** Wykres przedstawia rozkład odpowiedzi PYT\\_2 w sześciu\nwarstwach (3 kategorie stażu $\\times$ 2 poziomy stanowiska). Kształt rozkładu\nPYT\\_2 jest podobny w poszczególnych warstwach (przewaga odpowiedzi\npozytywnych), co jest spójne z brakiem odrzucenia hipotez 2 i 3. Jednocześnie\nwidać silną zależność CZY\\_KIER–STAŻ: kierownicy występują niemal wyłącznie\nprzy dłuższym stażu (panel „Kierownik\" dla stażu `<1 rok` jest niemal pusty),\nco tłumaczy odrzucenie hipotezy o wzajemnej niezależności.",
        "**Comment on the figure.** PYT\\_2 in six strata; similar positive skew; managers almost only with longer tenure.",
    ),
    (
        "W zadaniu 4 test Bowkera napotyka problem: para komórek $(0,2)$ ma\n$n_{35}+n_{53}=0$, więc składnik $\\tfrac{(n_{ij}-n_{ji})^2}{n_{ij}+n_{ji}}$\njest postaci $0/0$. Rozwiązaniem jest **dokładny (warunkowy) test symetrii**.",
        "Bowker hits $0/0$ for pair $(0,2)$; use **exact conditional symmetry test**.",
    ),
    (
        "**Idea.** Przy hipotezie symetrii $\\pi_{ij}=\\pi_{ji}$ rozumujemy warunkowo\nwzględem sum par pozaprzekątniowych $m_{ij}=n_{ij}+n_{ji}$. Dla każdej pary\n$(i<j)$ liczebność $n_{ij}\\mid m_{ij}\\sim\\mathrm{Bin}(m_{ij},\\tfrac12)$,\na poszczególne pary są (warunkowo) niezależne. Statystyką może być np.\n$T=\\sum_{i<j}(n_{ij}-n_{ji})^2/(n_{ij}+n_{ji})$ (Bowker) lub suma odchyleń.",
        "**Idea.** Under symmetry, condition on pair sums; binomial allocation across pairs.",
    ),
    (
        "Dokładny (symulowany, $B=20000$) test symetrii daje\n$T \\approx `r round(es$T,3)`$ oraz p-wartość $\\approx `r signif(es$p,3)`$ —\nzgodnie z testem Bowkera p-wartość znacznie przekracza $0{,}05$, więc **nie\nma podstaw do odrzucenia hipotezy symetrii**. Test dokładny jest tu\npoprawniejszy, bo nie wymaga przybliżenia $\\chi^2$ ani niezerowych sum par.",
        "Exact test ($B=20000$): $T \\approx `r round(es$T,3)`$, p $\\approx `r signif(es$p,3)`$ — **insufficient evidence to reject symmetry**.",
    ),
    (
        "- **Zad. 1–2.** Warunkowy symmetry test dla tablicy $2\\times2$ to dokładny\n  odpowiednik testu McNemara ($n_{12}\\mid m\\sim\\mathrm{Bin}(m,\\tfrac12)$).\n  Dla leków przeciwbólowych ($p\\approx0{,}45$) brak dowodu na różną\n  skuteczność.\n- **Zad. 3.** Zadowolenie ze szkoleń **zmieniło się** między okresami\n  ($p\\approx0{,}036$) — istotnie więcej osób stało się zadowolonych.\n- **Zad. 4.** Ocena podejścia firmy **nie uległa zmianie** — test Bowkera\n  ($p\\approx0{,}31$) nie odrzuca symetrii (problem zer rozwiązany w sat. 1\\*).\n- **Zad. 5.** W danych o leczeniu **występuje paradoks Simpsona**: metoda B\n  wygrywa w agregacie, lecz metoda A jest lepsza w obu podgrupach.\n- **Zad. 6–7.** Podano interpretacje sześciu modeli log-liniowych oraz\n  oszacowano prawdopodobieństwa w modelu nasyconym i $[12\\ 23]$.\n- **Zad. 8.** Zmienne CZY\\_KIER, PYT\\_2, STAŻ **nie są** wzajemnie niezależne;\n  natomiast PYT\\_2 jest (warunkowo) niezależna od CZY\\_KIER przy ustalonym\n  stażu ($p\\approx0{,}85$).",
        "- **Tasks 1–2.** Conditional symmetry = exact McNemar; no analgesic difference ($p\\approx0.45$).\n- **Task 3.** Satisfaction **changed** ($p\\approx0.036$).\n- **Task 4.** Company rating **unchanged** (Bowker $p\\approx0.31$).\n- **Task 5.** **Simpson's paradox**.\n- **Tasks 6–7.** Log-linear interpretations and estimates.\n- **Task 8.** Not mutually independent; PYT\\_2 independent of CZY\\_KIER given tenure ($p\\approx0.85$).",
    ),
]
