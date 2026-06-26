"""Second-pass paragraph translations (Polish -> English)."""

PASS2: list[tuple[str, str]] = [
    # --- report1 ---
    (
        "Przed przystąpieniem do właściwej analizy kluczowe jest sprawdzenie kompletności zbioru. Braki danych mogą wynikać z odmowy odpowiedzi przez respondenta, błędów w procesie zbierania danych lub -- jak w przypadku zmiennej `PYT_3` -- z faktu, że pytanie było zadawane tylko wybranej podgrupie (np. pracownikom, którzy uczestniczyli w drugiej turze badań).",
        "Before the main analysis, it is essential to check data completeness. Missing values may result from respondent refusal, data collection errors, or — as with `PYT_3` — the question being asked only to a selected subgroup (e.g. employees who participated in the second survey wave).",
    ),
    (
        "**Wnioski:** Tabela przedstawia liczbę brakujących obserwacji dla każdej zmiennej. Jeśli braki dotyczą wyłącznie zmiennej `PYT_3`, jest to zjawisko oczekiwane -- pytanie to zadawano jedynie osobom uczestniczącym w ponownym badaniu po cyklu szkoleń. Braki w pozostałych zmiennych demograficznych (jeśli wystąpią) wymagają ostrożności przy interpretacji -- mogą świadczyć o selektywnej odmowie odpowiedzi. W dalszej analizie braki są ignorowane lokalnie (operacja `filter(!is.na())`), co oznacza, że mianowniki w obliczeniach procentowych odnoszą się do liczby ważnych obserwacji, nie do pełnej próby.",
        "**Conclusions:** The table shows the number of missing observations for each variable. If missing values affect only `PYT_3`, this is expected — the question was asked only to participants in the follow-up survey after a training cycle. Missing values in other demographic variables (if any) require caution — they may indicate selective non-response. In further analysis, missing values are handled locally (`filter(!is.na())`), so percentage denominators refer to valid observations, not the full sample.",
    ),
    (
        "Ciągła zmienna wieku jest trudna do bezpośredniej analizy tabelarycznej -- każdy unikalny wiek tworzyłby osobną kategorię. Stosujemy **dyskretyzację** (ang. *binning*): dzielimy wiek respondentów na cztery przedziały prawostronnie domknięte, wybrane tak, aby odpowiadały naturalnym etapom kariery zawodowej:",
        "The continuous age variable is difficult to analyze directly in tables — each unique age would form a separate category. We apply **discretization** (*binning*): respondent age is split into four right-closed intervals corresponding to natural career stages:",
    ),
    (
        "-   **Do 35 lat** -- pracownicy na początku kariery (juniorzy, mid-level);\n-   **36--45 lat** -- pracownicy w środkowym stadium kariery (seniorzy, specjaliści);\n-   **46--55 lat** -- kadra z długim doświadczeniem, często menedżerska;\n-   **Powyżej 55 lat** -- pracownicy zbliżający się do końca kariery zawodowej.",
        "-   **Up to 35 years** — employees at the start of their careers (juniors, mid-level);\n-   **36--45 years** — mid-career employees (seniors, specialists);\n-   **46--55 years** — experienced staff, often in management roles;\n-   **Over 55 years** — employees approaching the end of their careers.",
    ),
    (
        "Podział ten pozwala ocenić, czy preferencje i oceny szkoleń różnią się między pokoleniami, co jest szczególnie istotne w kontekście rosnących różnic między podejściem do nauki pokolenia Z a starszymi rocznikami.",
        "This split helps assess whether training preferences and ratings differ across generations, which is especially relevant given growing differences between Generation Z and older cohorts in learning approaches.",
    ),
    (
        "Tablice liczności pozwalają ocenić, jak zróżnicowana jest badana próba pod względem demograficznym i organizacyjnym. Jest to kluczowy krok przed analizą odpowiedzi na pytania merytoryczne -- pozwala zidentyfikować ewentualne **efekty składu próby**: jeśli np. jedna z grup jest wyraźnie nadreprezentowana, jej opinie będą miały nieproporcjonalnie duży wpływ na wyniki zbiorcze.",
        "Frequency tables show how diverse the sample is demographically and organizationally. This is a key step before analyzing substantive questions — it helps identify **sample composition effects**: if one group is clearly overrepresented, its opinions disproportionately influence aggregate results.",
    ),
    (
        "Poniższe tablice przedstawiają rozkład respondentów według przynależności do działu oraz stażu pracy. Informacje te są niezbędne do oceny reprezentatywności próby -- czy wszystkie działy są proporcjonalnie reprezentowane, oraz czy przeważają pracownicy nowi czy doświadczeni.",
        "The tables below show the distribution of respondents by department and tenure. This information is needed to assess sample representativeness — whether all departments are proportionally represented and whether newer or more experienced employees predominate.",
    ),
    (
        "**Wnioski:** Analiza podziału na działy pozwala ocenić, czy wyniki ankiety są reprezentatywne dla całej firmy, czy też zdominowane przez jeden dział. Jeżeli np. dział IT stanowi ponad 50% próby, a szkolenia są projektowane z myślą o tym dziale, oceny mogą być systematycznie wyższe niż gdyby badano firmę w sposób warstwowy. Podobnie rozkład stażu pracy informuje o dojrzałości kadry -- dominacja pracowników z krótkim stażem sugeruje, że firma intensywnie rekrutuje i że szkolenia wdrożeniowe (onboardingowe) mają szczególne znaczenie. Pracownicy z długim stażem mają z kolei wyższe i bardziej specyficzne oczekiwania szkoleniowe, co może prowadzić do niższych ocen ogólnych.",
        "**Conclusions:** Analyzing the departmental split shows whether survey results represent the whole company or are dominated by one department. If IT exceeds 50% of the sample and training is designed for that department, ratings may be systematically higher than under stratified sampling. Tenure distribution reflects workforce maturity — a predominance of short-tenure employees suggests active hiring and the importance of onboarding training. Long-tenure employees tend to have higher and more specific training expectations, which can lower overall ratings.",
    ),
    (
        "Kolejne trzy tablice charakteryzują próbę pod kątem płci, udziału kadry kierowniczej oraz struktury wiekowej. Dane te są istotne przy interpretacji wyników -- pozwalają ocenić, czy obserwowane różnice w ocenach wynikają z czynników demograficznych.",
        "The next three tables characterize the sample by gender, management representation, and age structure. These data matter when interpreting results — they help assess whether observed rating differences stem from demographic factors.",
    ),
    (
        "**Wnioski:** Odsetek kadry kierowniczej w próbie powinien być zbliżony do rzeczywistej struktury firmy -- standardowo kierownicy stanowią 15--25% załogi. Znaczna nadreprezentacja menedżerów mogłaby zawyżać oceny szkoleń (menedżerowie częściej uczestniczą w szkoleniach i mogą postrzegać je bardziej pozytywnie). W zakresie płci warto sprawdzić, czy próba odzwierciedla strukturę firmy -- nierównowaga płci w ankiecie może zniekształcać wyniki, jeśli kobiety i mężczyźni mają różne doświadczenia ze szkoleniami. Analiza struktury wiekowej pozwala ocenić, czy firma zatrudnia głównie młodszych pracowników (profil typowy dla firm technologicznych i start-upów) czy ma bardziej zrównoważony rozkład wieku.",
        "**Conclusions:** The share of management staff in the sample should be close to the company's actual structure — managers typically make up 15--25% of the workforce. Overrepresentation of managers could inflate training ratings (managers participate more often and may view training more positively). For gender, check whether the sample reflects company structure — gender imbalance can distort results if women and men have different training experiences. Age structure analysis shows whether the company mainly employs younger workers (typical of tech firms and start-ups) or has a more balanced age distribution.",
    ),
    (
        "Analiza rozkładów odpowiedzi na poszczególne pytania stanowi rdzeń analizy opisowej. Dla każdego pytania prezentujemy dwa uzupełniające się wykresy: **kołowy** (szybka ocena proporcji) oraz **słupkowy** (precyzyjne porównanie kategorii). Takie zestawienie pozwala jednocześnie uchwycić obraz całości i dostrzec różnice między kategoriami odpowiedzi.",
        "Analyzing response distributions for individual questions is the core of descriptive analysis. For each question we present two complementary charts: a **pie chart** (quick proportion assessment) and a **bar chart** (precise category comparison). Together they capture the overall picture and highlight differences between response categories.",
    ),
    (
        "Pytanie 1 mierzy, w jakim stopniu pracownicy zgadzają się ze stwierdzeniem dotyczącym dostępności materiałów szkoleniowych. Zastosowano **pięciostopniową skalę Likerta** z opcją neutralną („Nie mam zdania\"), co pozwala respondentom wyrazić brak wyrobionego zdania bez zmuszania ich do arbitralnego wyboru.",
        "Question 1 measures the extent to which employees agree with a statement about the availability of training materials. A **five-point Likert scale** with a neutral option (\"No opinion\") allows respondents to express no firm view without forcing an arbitrary choice.",
    ),
    (
        "**Analiza:** Równoległe zestawienie obu wykresów umożliwia wielowymiarową ocenę rozkładu opinii. Dominacja odpowiedzi pozytywnych („Zgadzam się\" i „Zdecydowanie zgadzam się\") świadczyłaby o satysfakcji pracowników z dostępności materiałów szkoleniowych. Jednak istotny udział odpowiedzi neutralnych („Nie mam zdania\") może wskazywać na niewystarczającą świadomość dostępnych zasobów -- pracownicy nie korzystają z materiałów nie dlatego, że je oceniają negatywnie, lecz dlatego, że nie wiedzą o ich istnieniu. Jest to sygnał do działań komunikacyjnych (np. kampania informacyjna o platformie e-learningowej). Wysoki odsetek odpowiedzi negatywnych wymagałby natomiast audytu jakości i dostępności zasobów szkoleniowych.",
        "**Analysis:** Presenting both charts side by side enables a multidimensional assessment of opinion distribution. Dominance of positive responses (\"Agree\" and \"Strongly agree\") would indicate satisfaction with training material availability. However, a substantial share of neutral responses (\"No opinion\") may indicate insufficient awareness of available resources — employees may not use materials because they do not know they exist, not because they rate them negatively. This signals a need for communication (e.g. an e-learning platform campaign). A high share of negative responses would call for an audit of training resource quality and accessibility.",
    ),
    (
        "Pytanie 2 ocenia, czy realizowane szkolenia odpowiadają potrzebom rozwojowym pracowników i wspierają ich ścieżkę kariery. W odróżnieniu od pytania 1 zastosowano **wymuszoną skalę czterostopniową** (bez opcji neutralnej), co skłania respondentów do jednoznacznego opowiedzenia się po stronie aprobaty lub krytyki. Takie podejście jest stosowane celowo, gdy badacz chce uniknąć skupiania się odpowiedzi w środku skali.",
        "Question 2 assesses whether training meets employees' development needs and supports their career paths. Unlike question 1, a **forced four-point scale** (no neutral option) encourages respondents to take a clear stance for or against. This is used deliberately when the researcher wants to avoid responses clustering in the middle of the scale.",
    ),
    (
        "**Analiza:** Wymuszona skala czterostopniowa wyraźnie polaryzuje odpowiedzi, ułatwiając identyfikację dominującego nastroju. Jeśli pytanie 2 wypada gorzej niż pytanie 1, oznacza to, że pracownicy doceniają dostępność materiałów (PYT_1), ale uważają, że szkolenia słabo przekładają się na ich realne możliwości awansu i nie odpowiadają ich indywidualnym potrzebom (PYT_2). Jest to częsty problem w organizacjach oferujących ustandaryzowane, „katalogowe\" programy szkoleniowe zamiast ścieżek skrojonych pod konkretne role i ambicje pracowników. Taki wynik powinien skłonić dział HR do wdrożenia **indywidualnych planów rozwoju (IDP)** oraz regularnych rozmów menedżer--pracownik o potrzebach szkoleniowych.",
        "**Analysis:** The forced four-point scale clearly polarizes responses, making it easier to identify the dominant mood. If question 2 scores worse than question 1, employees appreciate material availability (PYT_1) but feel training poorly translates into promotion opportunities and individual needs (PYT_2). This is common in organizations offering standardized catalog programs instead of paths tailored to roles and ambitions. Such a result should prompt HR to implement **individual development plans (IDPs)** and regular manager–employee discussions about training needs.",
    ),
    (
        "Tablice krzyżowe (kontyngencji) pozwalają zbadać związek między zmiennymi demograficznymi i organizacyjnymi a ocenami szkoleń wyrażonymi w pytaniu 1. Dla każdej pary zmiennych tworzymy dwie tabele: **liczebności** (ile osób w danej grupie udzieliło danej odpowiedzi) oraz **profil kolumnowy** (jaki odsetek danej grupy udzielił danej odpowiedzi). Profil kolumnowy jest kluczowy -- pozwala porównywać grupy o różnych liczebnościach na wspólnej skali procentowej.",
        "Cross-tabulations (contingency tables) examine relationships between demographic and organizational variables and training ratings in question 1. For each variable pair we create two tables: **counts** (how many in each group gave each response) and **column profile** (what percentage of each group gave each response). The column profile is key — it compares groups of different sizes on a common percentage scale.",
    ),
    (
        "Interpretacja: jeśli profile kolumnowe wyraźnie różnią się między grupami (np. pracownicy IT są wyraźnie bardziej zadowoleni niż pracownicy HR), mamy do czynienia ze **zróżnicowaniem wewnętrznym** wymagającym pogłębionej analizy i zróżnicowania oferty szkoleniowej.",
        "Interpretation: if column profiles differ clearly between groups (e.g. IT employees are much more satisfied than HR employees), there is **internal differentiation** requiring deeper analysis and differentiated training offerings.",
    ),
    (
        "Porównanie ocen między działami pozwala ocenić, czy oferta szkoleniowa jest jednakowo dobrze dopasowana do specyfiki pracy w różnych częściach organizacji. Działy różnią się profilem zawodowym, tempem zmian technologicznych i kulturą organizacyjną, co może przekładać się na odmienne oczekiwania wobec szkoleń.",
        "Comparing ratings across departments assesses whether training is equally well matched to work specifics across the organization. Departments differ in professional profile, pace of technological change, and organizational culture, which may lead to different training expectations.",
    ),
    (
        "**Wnioski:** Jeżeli profile kolumnowe są zbliżone między działami, oferta szkoleniowa jest postrzegana równomiernie w całej organizacji. Jeśli natomiast jeden dział wyraźnie odbiega od pozostałych (szczególnie w kierunku negatywnym), warto zbadać, czy szkolenia są odpowiednio dostosowane do jego specyfiki. Dział IT może np. oczekiwać bardziej zaawansowanych technicznie szkoleń, dział HR -- szkoleń miękkich i z zakresu prawa pracy, a dział marketingu (MK) -- szkoleń z narzędzi cyfrowych i analityki.",
        "**Conclusions:** If column profiles are similar across departments, training is perceived evenly across the organization. If one department clearly diverges (especially negatively), investigate whether training is suited to its specifics. IT may expect more advanced technical training, HR soft skills and labor law training, and marketing (MK) digital tools and analytics training.",
    ),
    (
        "Staż pracy jest jednym z najważniejszych moderatorów oceny szkoleń. Pracownicy z krótkim stażem oceniają szkolenia przez pryzmat wdrożenia i zdobywania podstawowych kompetencji, podczas gdy weterani oczekują szkoleń zaawansowanych, specjalistycznych i przekładających się na konkretne projekty.",
        "Tenure is one of the most important moderators of training ratings. Short-tenure employees evaluate training through onboarding and basic skills acquisition, while veterans expect advanced, specialized training tied to concrete projects.",
    ),
    (
        "**Wnioski:** Różnice w profilach kolumnowych między grupami stażu wskazują na potrzebę **segmentacji programów szkoleniowych**. Jeśli pracownicy z najdłuższym stażem oceniają szkolenia najgorzej, może to świadczyć o braku oferty dla ekspertów lub o tym, że istniejące szkolenia są zbyt podstawowe dla tej grupy. Z kolei nowi pracownicy, jeśli oceniają pozytywnie, potwierdzają skuteczność programu onboardingowego. Firma powinna rozważyć stworzenie odrębnych ścieżek szkoleniowych: wdrożeniowej (dla osób z krótkim stażem) i zaawansowanej (dla weteranów).",
        "**Conclusions:** Differences in column profiles across tenure groups indicate a need for **training program segmentation**. If longest-tenure employees rate training worst, this may reflect a lack of expert-level offerings or training that is too basic for them. If new employees rate positively, that confirms onboarding effectiveness. The company should consider separate paths: onboarding (short tenure) and advanced (veterans).",
    ),
    (
        "Menedżerowie i pracownicy szeregowi uczestniczą w różnych typach szkoleń i mają odmienne potrzeby -- pierwsi skupiają się na kompetencjach przywódczych i zarządzaniu, drudzy na umiejętnościach technicznych i branżowych. Analiza tej zmiennej pozwala ocenić, czy oba segmenty są jednakowo dobrze obsługiwane przez dział szkoleń.",
        "Managers and non-managerial staff participate in different types of training and have different needs — the former focus on leadership and management, the latter on technical and industry skills. This variable helps assess whether both segments are equally well served by the training function.",
    ),
    (
        "**Wnioski:** Duże różnice między kierownikami a pracownikami szeregowymi w profilach kolumnowych wskazują na asymetrię w postrzeganiu wartości szkoleń. Jeśli menedżerowie oceniają wyżej, może to wynikać z faktu, że mają większy wpływ na dobór szkoleń (sami je wybierają lub zamawiają) i uczestniczą w droższych, lepiej dopasowanych programach zewnętrznych. Jeśli oceniają niżej, może to sygnalizować, że firma inwestuje głównie w szkolenia operacyjne, zaniedbując rozwój kompetencji menedżerskich.",
        "**Conclusions:** Large differences between managers and non-managers in column profiles indicate asymmetry in perceived training value. Higher manager ratings may reflect greater influence over training selection and participation in better-matched external programs. Lower manager ratings may signal investment mainly in operational training at the expense of management development.",
    ),
    (
        "Analiza różnic między kobietami a mężczyznami w ocenie materiałów szkoleniowych pozwala ocenić, czy polityka szkoleniowa firmy jest neutralna pod względem płci, czy też jedna z grup jest systematycznie gorzej obsługiwana.",
        "Analyzing differences between women and men in training material ratings assesses whether training policy is gender-neutral or whether one group is systematically underserved.",
    ),
    (
        "**Wnioski:** Brak istotnych różnic między kobietami a mężczyznami w profilach kolumnowych świadczyłby o neutralności płciowej polityki szkoleniowej -- co jest pożądanym wynikiem. Jeśli jednak jedna z grup wyraźnie gorzej ocenia dostępność materiałów szkoleniowych, warto zbadać przyczyny: mogą one tkwić w strukturze zatrudnienia (kobiety i mężczyźni koncentrują się w różnych działach lub na różnych stanowiskach) lub w treści szkoleń (programy nieuwzględniające perspektywy jednej z płci). Wyniki tej tablicy powinny być interpretowane łącznie z rozkładem płci w poszczególnych działach, aby wykluczyć efekty interakcji między zmiennymi.",
        "**Conclusions:** No significant gender differences in column profiles would indicate gender-neutral training policy — a desirable outcome. If one group rates material availability clearly worse, investigate causes: employment structure (gender concentration in different departments or roles) or training content (programs not reflecting one gender's perspective). Interpret this table together with gender distribution by department to rule out interaction effects.",
    ),
    (
        "Zgodnie z poleceniem, przed przystąpieniem do analizy inferencyjnej (estymacji i testowania hipotez), konstruujemy binarne zmienne określające zadowolenie ze szkoleń. Zmienne `CZY_ZADOW` oraz `CZY_ZADOW_2` powstaną poprzez zagregowanie pozytywnych i negatywnych odpowiedzi na pytania, odpowiednio, `PYT_2` oraz `PYT_3`.",
        "As instructed, before inferential analysis (estimation and hypothesis testing), we construct binary variables for training satisfaction. `CZY_ZADOW` and `CZY_ZADOW_2` aggregate positive and negative responses to `PYT_2` and `PYT_3`, respectively.",
    ),
    (
        "Przedział ufności Cloppera-Pearsona (tzw. przedział dokładny) opiera się na rozkładzie dwumianowym. Wykorzystuje on kwantyle rozkładu Beta do wyznaczenia dolnej i górnej granicy. Poniżej zdefiniowano funkcję `clopper_pearson`, która jako argumenty przyjmuje poziom ufności, ułamek sukcesów i liczbę prób (lub opcjonalnie wektor danych, z którego sama oblicza te wartości).",
        "The Clopper-Pearson confidence interval (exact interval) is based on the binomial distribution. It uses Beta distribution quantiles for lower and upper bounds. Below we define `clopper_pearson`, which takes confidence level, number of successes, and sample size (or optionally a data vector from which it computes these values).",
    ),
    (
        "Wykorzystując utworzoną funkcję wyznaczamy przedziały ufności dla prawdopodobieństwa zadowolenia ze szkoleń w pierwszym okresie (`CZY_ZADOW`) oraz po modyfikacji szkoleń (`CZY_ZADOW_2`), na poziomie ufności $1-\\alpha = 0.95$. \\newpage{}",
        "Using the function we compute confidence intervals for the probability of training satisfaction in the first period (`CZY_ZADOW`) and after training modification (`CZY_ZADOW_2`), at confidence level $1-\\alpha = 0.95$. \\newpage{}",
    ),
    (
        "**Wnioski:** Jak widać, szerokość przedziału w drugim okresie jest inna, co może wynikać z faktu, że zmienna `PYT_3` ma zmniejszoną liczbę obserwacji (nie wszyscy pracownicy uczestniczyli w drugiej turze, stąd większa niepewność). Odsetek osób zadowolonych ze szkoleń możemy jednakże z 95% pewnością umiejscowić w wyznaczonych przedziałach.",
        "**Conclusions:** The second-period interval width differs, likely because `PYT_3` has fewer observations (not all employees participated in the second wave, hence greater uncertainty). We can nonetheless locate the proportion satisfied with training within the computed intervals with 95% confidence.",
    ),
    (
        "Przeprowadzimy symulację porównującą przedziały ufności: Cloppera-Pearsona (dokładny), Walda (asymptotyczny) oraz przedział Wilsona dla różnych wielkości próby $n \\in \\{30, 100, 1000\\}$ oraz prawdopodobieństw sukcesu $p \\in (0, 1)$.",
        "We run a simulation comparing confidence intervals: Clopper-Pearson (exact), Wald (asymptotic), and Wilson for sample sizes $n \\in \\{30, 100, 1000\\}$ and success probabilities $p \\in (0, 1)$.",
    ),
    (
        "**Wnioski z symulacji:** 1. **Przedział Walda:** Posiada bardzo słabe właściwości w przypadku brzegowych prawdopodobieństw (bliskich 0 oraz 1), szczególnie dla małych prób ($n=30$). Jego pokrycie spada często drastycznie poniżej nominalnego 95%. Dodatkowo wariancja oszacowana staje się 0 na brzegach (długość przedziału spada do 0), co skutkuje całkowitym brakiem pokrycia. 2. **Przedział Cloppera-Pearsona:** Jest tzw. przedziałem zachowawczym (konserwatywnym) - prawdopodobieństwo pokrycia nie spada poniżej zakładanego $1-\\alpha$, i oscyluje powyżej wielkości 0.95. Odbywa się to jednak kosztem nieco szerszego przedziału w porównaniu do innych metod. 3. **Przedział Wilsona:** Stanowi bardzo dobre rozwiązanie i kompromis - charakteryzuje się pokryciem bliższym 95% w całym zasięgu $p$, a jego szerokość jest zadowalająco wąska. Dla danych rzeczywistych, takich jak w naszej ankiecie (n=200), korzystne byłoby wykorzystanie stabilnego przedziału Wilsona lub dokładnego Cloppera-Pearsona.",
        "**Conclusions from the simulation:** 1. **Wald interval:** Performs poorly at boundary probabilities (near 0 and 1), especially for small $n=30$. Coverage often falls well below nominal 95%. Estimated variance becomes 0 at boundaries (interval length 0), yielding no coverage. 2. **Clopper-Pearson interval:** Conservative — coverage does not fall below $1-\\alpha$ and tends to exceed 0.95, at the cost of slightly wider intervals. 3. **Wilson interval:** A strong compromise — coverage closer to 95% across $p$ with satisfactorily narrow width. For real data like our survey ($n=200$), Wilson or Clopper-Pearson is preferable.",
    ),
    (
        "Do weryfikacji układów hipotez korzystamy ze wbudowanych funkcji `binom.test` oraz `prop.test` z biblioteki `stats`. Przeprowadzamy testy na poziomie istotności $\\alpha = 0.05$.",
        "We use built-in `binom.test` and `prop.test` from `stats` for hypothesis testing at significance level $\\alpha = 0.05$.",
    ),
    (
        "**Wnioski z testowania hipotez:** Powyższa tabela prezentuje wyniki wszystkich testów (tzw. wartości *p-value* oraz podstawowe konkluzje przy poziomie istotności $5\\%$). Jeśli *p-value* spada poniżej ustalonego progu odrzucenia ($\\alpha = 0.05$), świadczy to o wystarczających dowodach na odrzucenie hipotezy zerowej $H_0$ i opowiedzenie się za hipotezą alternatywną, w innym wypadku nie mamy podstaw by odrzucić badane twierdzenie z testów proporcji. Na przykład w przypadku testu numer 2 badane jest czy satysfakcja wpisuje się w warunek $p \\ge 0.7$. Uzyskanie wysokiego *p-value* dowodzi o braku podstaw, na których mielibyśmy uznać że satysfakcja jest istotnie niższa (jeśli *p* jest mniejsze od poziomu błędu, skłaniałoby to do tezy o niższym poziomie satysfakcji).",
        "**Conclusions from hypothesis testing:** The table presents all test results (*p-values* and basic conclusions at 5% significance). If *p-value* falls below $\\alpha = 0.05$, there is sufficient evidence to reject $H_0$; otherwise we do not reject the proportion hypothesis. For test 2, we assess whether satisfaction satisfies $p \\ge 0.7$. A high *p-value* indicates insufficient evidence that satisfaction is significantly lower (a low *p* would support lower satisfaction).",
    ),
    (
        "Przeprowadzimy symulację Monte Carlo porównującą moc testu dokładnego (`binom.test`) oraz asymptotycznego (`prop.test`) przy weryfikacji hipotezy zerowej $H_0: p = 0.9$ przeciwko hipotezie alternatywnej $H_1: p \\neq 0.9$. Symulacja zostanie przeprowadzona dla trzech wielkości próby $n \\in \\{10, 100, 1000\\}$ oraz wartości rzeczywistego prawdopodobieństwa sukcesu $p \\in [0.7,\\; 0.99]$. Dla każdej kombinacji parametrów generujemy $B = 5000$ replikacji Monte Carlo, co zapewnia stabilność estymacji mocy.",
        "We run a Monte Carlo simulation comparing exact (`binom.test`) and asymptotic (`prop.test`) test power for $H_0: p = 0.9$ vs $H_1: p \\neq 0.9$, for $n \\in \\{10, 100, 1000\\}$ and true $p \\in [0.7, 0.99]$, with $B = 5000$ replications per parameter combination.",
    ),
    (
        "1.  **Wpływ wielkości próby na moc:** Wyniki symulacji wyraźnie ilustrują fundamentalną zależność -- moc testu rośnie wraz z wielkością próby $n$. Dla $n = 10$ krzywa mocy jest bardzo płaska -- nawet znaczne odstępstwa od $H_0$ (np. $p = 0.7$) są wykrywane z niewielkim prawdopodobieństwem, co czyni test praktycznie bezużytecznym w wykrywaniu subtelnych różnic. Dla $n = 100$ moc wyraźnie wzrasta w miarę oddalania się od $p = 0.9$, a dla $n = 1000$ krzywa jest niemal skokowo stroma -- test wykrywa nawet odchylenia rzędu 2--3 punktów procentowych.",
        "1.  **Effect of sample size on power:** Power increases with $n$. For $n = 10$ the power curve is very flat — even large deviations from $H_0$ (e.g. $p = 0.7$) are rarely detected. For $n = 100$ power rises as $p$ moves away from 0.9; for $n = 1000$ the curve is steep — the test detects deviations of 2--3 percentage points.",
    ),
    (
        "2.  **Porównanie testu dokładnego i asymptotycznego:** Dla małych prób ($n = 10$) test dokładny (Cloppera-Pearsona / `binom.test`) jest bardziej zachowawczy -- jego empiryczny poziom istotności przy $H_0$ jest mniejszy od nominalnych 5%, co skutkuje nieco niższą mocą w porównaniu z testem asymptotycznym. Wraz ze wzrostem $n$ różnica między oboma metodami zanika, ponieważ aproksymacja normalną staje się coraz dokładniejsza.",
        "2.  **Exact vs asymptotic test:** For small $n = 10$, the exact test is more conservative — empirical size under $H_0$ is below 5%, yielding slightly lower power than the asymptotic test. As $n$ grows, the difference vanishes as the normal approximation improves.",
    ),
    (
        "3.  **Praktyczne implikacje:** Dla danych ankietowych o wielkości zbliżonej do $n \\approx 200$ (jak w naszym badaniu) oba testy mają zbliżoną, wysoką moc do wykrywania odstępstw rzędu 10 p.p. od testowanej wartości. Wybór próby $n \\geq 100$ zapewnia solidną zdolność wykrywania praktycznie istotnych różnic.",
        "3.  **Practical implications:** For survey data near $n \\approx 200$ (as in our study), both tests have similar high power to detect 10 p.p. deviations from the tested value. Sample sizes $n \\geq 100$ provide solid power for practically important differences.",
    ),
    # --- report2 ---
    (
        "$p = (p_1,\\dots,p_5)$ jest wektorem prawdopodobieństw odpowiedzi\n\"very dissat.\", \"dissat.\", \"no opinion\", \"sat.\", \"very sat.\".\nOszacowanie to $\\hat p_i = X_i/n$.",
        "$p = (p_1,\\dots,p_5)$ is the probability vector for responses\n\"very dissat.\", \"dissat.\", \"no opinion\", \"sat.\", \"very sat.\".\nThe estimator is $\\hat p_i = X_i/n$.",
    ),
    (
        "- **Goodman (1965)** --- oparta na odwróceniu $\\chi^2$ z korektą Bonferroniego\n  (kwantyl $\\chi^2_{1,\\,\\alpha/k}$, gdzie $k$ = liczba kategorii). Dla każdej\n  składowej:",
        "- **Goodman (1965)** — based on inverted $\\chi^2$ with Bonferroni correction\n  (quantile $\\chi^2_{1,\\,\\alpha/k}$, where $k$ = number of categories). For each\n  component:",
    ),
    (
        "- **Sison, Glaz (1995)** --- przedział o jednakowej szerokości\n  $\\hat p_i \\pm d$, gdzie $d$ dobrane jest numerycznie tak, by\n  jednoczesny poziom ufności był $\\ge 1-\\alpha$.",
        "- **Sison, Glaz (1995)** — equal-width interval\n  $\\hat p_i \\pm d$, where $d$ is chosen numerically so that\n  simultaneous coverage is $\\ge 1-\\alpha$.",
    ),
    (
        "**Opis Tabeli 1.** Kolumna `p_hat` podaje estymator MNW, kolejne pary kolumn\nzawierają dolne i górne końce jednoczesnych 95\\% PU. Przedziały Sison--Glaz\nsą zauważalnie węższe od Goodmana (kosztem dokładności asymptotycznej, S--G\njest metodą o jednostajnej szerokości), lecz wnioski merytoryczne są zbieżne:\nkategoria \"zadowoleni\" dominuje ($p_4 \\in [0.4133, 0.5906]$ Goodman,\n$[0.4305,0.5705]$ S--G), zaś kategorie skrajnie niezadowolonych\n($p_1, p_2$) mają prawdopodobieństwa rzędu kilku procent i ich przedziały\nsą rozłączne z przedziałem kategorii dominującej.",
        "**Table description 1.** Column `p_hat` gives the MLE; subsequent column pairs contain lower and upper bounds of simultaneous 95% CIs. Sison--Glaz intervals are noticeably narrower than Goodman's (S--G is equal-width at the cost of asymptotic accuracy), but substantive conclusions agree: the \"satisfied\" category dominates ($p_4 \\in [0.4133, 0.5906]$ Goodman, $[0.4305,0.5705]$ S--G), while extremely dissatisfied categories ($p_1, p_2$) have probabilities of a few percent with intervals disjoint from the dominant category.",
    ),
    (
        "**Opis Rysunku 1.** Widać monotoniczny wzrost oszacowań od kategorii skrajnie\nnegatywnej do \"zadowolony\" i lekki spadek do \"bardzo zadowolony\". PU metody\nGoodmana są szersze dla kategorii o małej liczności (efekt asymptotyczny\nodwróconego $\\chi^2_1$).",
        "**Figure description 1.** Estimates rise monotonically from the most negative category to \"satisfied\" and dip slightly for \"very satisfied\". Goodman CIs are wider for low-count categories (asymptotic effect of inverted $\\chi^2_1$).",
    ),
    (
        "Przy $H_0$ obie statystyki mają asymptotycznie rozkład $\\chi^2_{k-1}$,\nzatem p-value $= 1 - F_{\\chi^2_{k-1}}(T_\\cdot(x))$.",
        "Under $H_0$ both statistics are asymptotically $\\chi^2_{k-1}$, so p-value $= 1 - F_{\\chi^2_{k-1}}(T_\\cdot(x))$.",
    ),
    (
        "Hypothesis $H_0: p = p_0 = (\\tfrac15,\\dots,\\tfrac15)$ (rozkład równomierny\nna 5 kategoriach), $\\alpha = 0{,}05$.",
        "Hypothesis $H_0: p = p_0 = (\\tfrac15,\\dots,\\tfrac15)$ (uniform distribution\nover 5 categories), $\\alpha = 0.05$.",
    ),
    (
        "**Opis Tabel 2--3.** W Tabeli 2 widać wyraźnie niejednorodny rozkład\nodpowiedzi: dominują odpowiedzi \"zadowolony\" (`PYT_1 = 1`), a obserwowane\nliczności znacznie odbiegają od wartości oczekiwanej\n$np_{0i} = 98/5 = 19{,}6$. W Tabeli 3 obie statystyki testowe przyjmują\nduże wartości, a p-wartości są znacznie mniejsze od $\\alpha = 0{,}05$.",
        "**Tables description 2--3.** Table 2 shows a clearly non-uniform response distribution: \"satisfied\" (`PYT_1 = 1`) dominates, and observed counts differ greatly from expected $np_{0i} = 98/5 = 19.6$. In Table 3 both test statistics are large and p-values are well below $\\alpha = 0.05$.",
    ),
    (
        "**Wniosek.** Odrzucamy $H_0$. Rozkład odpowiedzi na pytanie PYT_1 w Dziale\nProduktowym nie jest równomierny --- pracownicy PD udzielają odpowiedzi\npozytywnych istotnie częściej niż wynikałoby to z jednorodności.",
        "**Conclusion.** We reject $H_0$. The PYT_1 response distribution in the Product Department is not uniform — PD employees give positive responses significantly more often than uniformity would imply.",
    ),
    (
        "**Interpretation.** $p$-wartość $= `r signif(ft$p.value,3)`$.\nPrzy poziomie $\\alpha = 0.05$ **`r ifelse(ft$p.value < 0.05,\"reject\",\"we do not reject\")`**\nhipotezy zerowej o niezależności zmiennych PŁEĆ i CZY_KIER. Oszacowanie\nilorazu szans wynosi `r round(ft$estimate,3)` (95% PU:\n`r round(ft$conf.int[1],3)`--`r round(ft$conf.int[2],3)`).",
        "**Interpretation.** $p$-value $= `r signif(ft$p.value,3)`$.\nAt $\\alpha = 0.05$ we **`r ifelse(ft$p.value < 0.05,\"reject\",\"do not reject\")`**\nthe null hypothesis of independence between GENDER and CZY_KIER. The odds ratio estimate is `r round(ft$estimate,3)` (95% CI:\n`r round(ft$conf.int[1],3)`--`r round(ft$conf.int[2],3)`).",
    ),
    (
        "**Czy można wnioskować, że $P(K\\,|\\,\\mathrm{kier}) = P(M\\,|\\,\\mathrm{kier})$?**",
        "**Can we infer that $P(K\\,|\\,\\mathrm{mgr}) = P(M\\,|\\,\\mathrm{mgr})$?**",
    ),
    (
        "**Nie, bezpośrednio na podstawie testu Fishera nie można.** Test Fishera\nweryfikuje hipotezę **niezależności**:\n$P(K \\cap \\mathrm{kier}) = P(K)\\cdot P(\\mathrm{kier})$, czyli równoważnie\n$P(K\\,|\\,\\mathrm{kier}) = P(K)$. Dopiero gdyby $P(K) = 0{,}5$, niezależność\nimplikowałaby $P(K\\,|\\,\\mathrm{kier}) = 0{,}5 = P(M\\,|\\,\\mathrm{kier})$.\nW próbie $P(K) = `r round(mean(dane$PLEC==\"K\"),3)`$, a więc rozkład płci\nw populacji nie jest 1:1. Dla pytania\n\"czy wśród kierowników $p_K = p_M$\" stosuje się **test dla jednej\nproporcji** (dwumianowy lub $\\chi^2$ z $p_0 = 0{,}5$):",
        "**No, not directly from Fisher's test.** Fisher's test checks **independence**:\n$P(K \\cap \\mathrm{mgr}) = P(K)\\cdot P(\\mathrm{mgr})$, equivalently\n$P(K\\,|\\,\\mathrm{mgr}) = P(K)$. Only if $P(K) = 0.5$ would independence imply\n$P(K\\,|\\,\\mathrm{mgr}) = 0.5 = P(M\\,|\\,\\mathrm{mgr})$.\nIn the sample $P(K) = `r round(mean(dane$PLEC==\"K\"),3)`$, so the gender distribution\nis not 1:1. For \"among managers, is $p_K = p_M$?\" use a **single-proportion test**\n(binomial or $\\chi^2$ with $p_0 = 0.5$):",
    ),
    (
        "$p$-wartość dwumianowego testu `r signif(bt$p.value,3)` --- zatem\n**`r ifelse(bt$p.value<0.05,\"reject\",\"we do not reject\")`**\nhipotezy $P(K\\,|\\,\\mathrm{kier})=1/2$.",
        "Binomial test p-value `r signif(bt$p.value,3)` — therefore we **`r ifelse(bt$p.value<0.05,\"reject\",\"do not reject\")`**\n$P(K\\,|\\,\\mathrm{mgr})=1/2$.",
    ),
    (
        "Test Freemana--Haltona jest uogólnieniem testu Fishera na tablice\n$r\\times c$; w `R` uzyskujemy go wywołując `fisher.test(..., simulate.p.value = TRUE)`\n(z uwagi na koszt obliczeń ścisłych dla większych tablic).",
        "The Freeman--Halton test generalizes Fisher's test to $r\\times c$ tables; in `R` use `fisher.test(..., simulate.p.value = TRUE)`\n(because exact computation is costly for larger tables).",
    ),
    (
        "**Opis Tabeli 5.** Kolumna *p-wartość* zawiera wartości p uzyskane symulacyjnie;\nostatnia kolumna podaje decyzję na poziomie $\\alpha = 0{,}05$.",
        "**Table description 5.** The *p-value* column contains simulation-based p-values;\nthe last column gives the decision at $\\alpha = 0.05$.",
    ),
    (
        "**Porównanie PYT_2 vs CZY_ZADOW.** Zmienna `PYT_2` ma 4 kategorie\n(silniejsza moc różnicująca), zaś `CZY_ZADOW` jest binarną agregacją\n`PYT_1`. Zauważmy:",
        "**Comparison PYT_2 vs CZY_ZADOW.** `PYT_2` has 4 categories\n(stronger discriminating power), while `CZY_ZADOW` is a binary aggregation of\n`PYT_1`. Note:",
    ),
    (
        "- dla par PYT_2 vs (CZY_KIER, STAŻ, PŁEĆ, WIEK_KAT) zróżnicowanie\n  rozkładu jest zwykle silniejsze (więcej kategorii --- więcej stopni\n  swobody, bardziej szczegółowy obraz zależności);\n- po zastąpieniu PYT_2 $\\to$ CZY_ZADOW następuje agregacja i test\n  zazwyczaj traci moc (p-wartości rosną), a w zadaniu o \"opiniach\n  kontekstowych\" warto pozostać przy pełnej skali.",
        "- for PYT_2 vs (CZY_KIER, TENURE, GENDER, WIEK_KAT) distribution differentiation is usually stronger (more categories — more degrees of freedom, finer dependence picture);\n- replacing PYT_2 with CZY_ZADOW aggregates categories and the test usually loses power (p-values rise); for contextual opinions, the full scale is preferable.",
    ),
    (
        "P-wartość $= `r signif(chi6$p.value,3)`$. Przy $\\alpha = 0{,}01$\n**`r ifelse(chi6$p.value < 0.01,\"reject\",\"we do not reject\")`**\nhipotezy o niezależności. Wynik jest zgodny z testem Freemana--Haltona\nw punkcie c) zadania 5.",
        "P-value $= `r signif(chi6$p.value,3)`$. At $\\alpha = 0.01$ we **`r ifelse(chi6$p.value < 0.01,\"reject\",\"do not reject\")`**\nindependence. This agrees with the Freeman--Halton test in task 5c.",
    ),
    (
        "**Wykres asocjacyjny (reszty standaryzowane Pearsona)** pokazuje znak i\nwielkość wkładu każdej komórki do statystyki $\\chi^2$:",
        "**Association plot (Pearson standardized residuals)** shows the sign and\nmagnitude of each cell's contribution to $\\chi^2$:",
    ),
    (
        "**Opis Rysunku 2.** Prostokąty nad linią zerową (niebieskie) odpowiadają\nkomórkom, w których zaobserwowano więcej przypadków niż wynikałoby z\nniezależności; pod linią (czerwone) --- komórkom z mniejszą liczebnością.\nNajsilniejsze odchylenia pojawiają się dla kategorii skrajnych PYT_2\n(\"zdec. tak\"/\"zdec. nie\") w podgrupie kierowników, co sugeruje, że\nopinia na temat dopasowania szkoleń do potrzeb indywidualnych jest\nistotnie związana z zajmowanym stanowiskiem.",
        "**Figure description 2.** Rectangles above the zero line (blue) are cells with more cases than independence predicts; below (red) — fewer. Largest deviations occur for extreme PYT_2 categories (\"str. agree\"/\"str. disagree\") among managers, suggesting opinions on training fit are related to position.",
    ),
    (
        "Dla tablicy $r\\times c$ z liczebnościami $n_{ij}$ i sumą $n$ statystyka:",
        "For an $r\\times c$ table with counts $n_{ij}$ and total $n$, the statistic:",
    ),
    (
        "ma przy $H_0$ niezależności asymptotycznie rozkład $\\chi^2_{(r-1)(c-1)}$.",
        "under $H_0$ of independence is asymptotically $\\chi^2_{(r-1)(c-1)}$.",
    ),
    (
        "**Opis Tabeli 7.** Asymptotycznie statystyki $\\chi^2$ i $G^2$ mają ten\nsam rozkład graniczny, jednak w próbie skończonej mogą się istotnie\nróżnić --- szczególnie gdy niektóre komórki mają bardzo małe liczności\n(jak PYT_2 = 1 z tylko 2 obserwacjami w całej próbie). Tutaj:\n$\\chi^2 \\approx `r round(chi6$statistic,2)`$ ($p \\approx `r signif(chi6$p.value,2)`$),\n$G^2 \\approx `r round(lr$statistic,2)`$ ($p \\approx `r signif(lr$p_value,2)`$).\nNa poziomie $\\alpha = 0{,}05$ oba testy prowadzą do odrzucenia $H_0$,\n**ale na poziomie $\\alpha = 0{,}01$ test Pearsona odrzuca $H_0$, a test\nNW --- nie**. Rozbieżność wynika z niskiej liczności w niektórych\nkomórkach (ostrzeżenie funkcji `chisq.test`); w takich przypadkach\nrekomenduje się sięgnięcie po test Fishera/Freemana--Haltona (zad. 5c),\nktóry zwraca p-wartość opartą na dokładnym lub symulowanym rozkładzie\nbez asymptotycznych założeń.",
        "**Table description 7.** Asymptotically $\\chi^2$ and $G^2$ share the same limiting distribution, but finite samples can differ — especially with very small cells (PYT_2 = 1 has only 2 observations). Here:\n$\\chi^2 \\approx `r round(chi6$statistic,2)`$ ($p \\approx `r signif(chi6$p.value,2)`$),\n$G^2 \\approx `r round(lr$statistic,2)`$ ($p \\approx `r signif(lr$p_value,2)`$).\nAt $\\alpha = 0.05$ both reject $H_0$,\n**but at $\\alpha = 0.01$ Pearson rejects while LR does not**. The discrepancy comes from low cell counts (`chisq.test` warning); then Fisher/Freeman--Halton (task 5c) with exact or simulated p-values is recommended.",
    ),
    (
        "Trzy miary związku (palenie = ekspozycja, choroba/zgon = skutek):",
        "Three association measures (smoking = exposure, disease/death = outcome):",
    ),
    (
        "- różnica proporcji $\\Delta = \\pi_1 - \\pi_2$,\n- ryzyko względne $\\mathrm{RR} = \\pi_1/\\pi_2$,\n- iloraz szans $\\mathrm{OR} = \\frac{\\pi_1/(1-\\pi_1)}{\\pi_2/(1-\\pi_2)}$.",
        "- proportion difference $\\Delta = \\pi_1 - \\pi_2$,\n- relative risk $\\mathrm{RR} = \\pi_1/\\pi_2$,\n- odds ratio $\\mathrm{OR} = \\frac{\\pi_1/(1-\\pi_1)}{\\pi_2/(1-\\pi_2)}$.",
    ),
    (
        "- **Rak płuc**: $\\mathrm{RR} = 14{,}0$ oznacza, że ryzyko zgonu z powodu raka\n  płuc wśród palaczy jest **14 razy większe** niż wśród niepalących; OR\n  jest praktycznie równe RR (bo $\\pi_i \\ll 1$). Różnica proporcji jest\n  niewielka (0{,}0013), ale ze względu na znikomą częstość bazową ($\\pi_2$\n  rzędu $10^{-4}$) wartość bezwzględna jest słabo informatywna.\n- **Choroba serca**: $\\mathrm{RR} \\approx 1{,}62$, $\\mathrm{OR} \\approx 1{,}62$.\n  Ryzyko palaczy jest o około 62\\% większe. $\\Delta = 0{,}00256$ --- w\n  liczbach bezwzględnych większe niż dla raka płuc (bo choroba serca jest\n  znacznie częstsza).",
        "- **Lung cancer**: $\\mathrm{RR} = 14.0$ means death risk from lung cancer among smokers is **14 times higher** than among non-smokers; OR ≈ RR (because $\\pi_i \\ll 1$). Proportion difference is small (0.0013), but baseline rate ($\\pi_2 \\sim 10^{-4}$) makes absolute difference weakly informative.\n- **Heart disease**: $\\mathrm{RR} \\approx 1.62$, $\\mathrm{OR} \\approx 1.62$. Smokers' risk is about 62% higher. $\\Delta = 0.00256$ — larger in absolute terms than lung cancer (heart disease is much more common).",
    ),
    (
        "**Siła związku.** Miary względne (RR, OR) jednoznacznie wskazują, że\n**związek palenia z rakiem płuc jest znacznie silniejszy** (RR = 14 vs\nRR $\\approx 1{,}62$), choć w liczbach bezwzględnych (różnica proporcji)\nwiększy wpływ populacyjny wywiera zależność palenie $\\to$ choroba serca.",
        "**Strength of association.** Relative measures (RR, OR) show **smoking–lung cancer association is much stronger** (RR = 14 vs RR $\\approx 1.62$), though in absolute terms (proportion difference) smoking $\\to$ heart disease has greater population impact.",
    ),
    (
        "Współczynnik gamma Goodmana--Kruskala:\n$\\gamma = (C - D)/(C + D)$, gdzie $C, D$ to liczba par zgodnych i niezgodnych.",
        "Goodman--Kruskal gamma:\n$\\gamma = (C - D)/(C + D)$, where $C, D$ are concordant and discordant pair counts.",
    ),
    (
        "**Opis Tabeli 9.** Wartości $\\gamma \\in [-1,1]$; znak wskazuje kierunek\nmonotonicznej zależności, moduł jej siłę. Analogicznie dla $\\tau_b$\n(skorygowane o powiązania). Interpretacja:",
        "**Table description 9.** Values $\\gamma \\in [-1,1]$; sign indicates direction of monotonic association, magnitude its strength. Similarly for $\\tau_b$ (tie-corrected). Interpretation:",
    ),
    (
        "- **PYT_2 vs CZY_KIER** --- wartość gamma odmienna od 0 świadczy o\n  zależności monotonicznej (zgodnie z testem z zad. 6),\n- **PYT_2 vs STAŻ** --- siła zależności bliska 0 sugeruje, że opinie o\n  dopasowaniu szkoleń do potrzeb nie układają się monotonicznie względem\n  stażu pracy,\n- **CZY_KIER vs STAŻ** --- zgodność kierunkowa przynależności do\n  kierownictwa ze stażem.",
        "- **PYT_2 vs CZY_KIER** — gamma away from 0 indicates monotonic association (consistent with task 6),\n- **PYT_2 vs TENURE** — strength near 0 suggests training-fit opinions do not align monotonically with tenure,\n- **CZY_KIER vs TENURE** — directional alignment of management role with tenure.",
    ),
    (
        "Przedziały ufności zawierające 0 wskazują na brak istotności danej\nmiary współzmienności.",
        "Confidence intervals containing 0 indicate non-significance of the association measure.",
    ),
    (
        "Correspondence analysis (CA) to metoda graficznej eksploracji tablicy\ndwudzielczej. Niech $N$ będzie tablicą o wymiarach $r\\times c$, $n = \\sum n_{ij}$,\nmacierz częstości względnych $P = N/n$, wektory mas $r = P\\mathbf 1$,\n$c = P^\\top\\mathbf 1$. Macierz reszt standaryzowanych:",
        "Correspondence analysis (CA) graphically explores a two-way table. Let $N$ be $r\\times c$, $n = \\sum n_{ij}$,\nrelative frequency matrix $P = N/n$, mass vectors $r = P\\mathbf 1$,\n$c = P^\\top\\mathbf 1$. Standardized residual matrix:",
    ),
    (
        "Rozkład SVD: $S = U \\Sigma V^\\top$. Współrzędne \"principal\":\nwiersze $F = D_r^{-1/2} U \\Sigma$, kolumny $G = D_c^{-1/2} V \\Sigma$.",
        "SVD: $S = U \\Sigma V^\\top$. Principal coordinates:\nrows $F = D_r^{-1/2} U \\Sigma$, columns $G = D_c^{-1/2} V \\Sigma$.",
    ),
    (
        "**Opis Tabeli 10 i Rysunku 3.** Sumaryczna inercja pierwszych dwóch\nwymiarów wyjaśnia łącznie\n$`r round(sum(ca$explained[1:2])*100,1)`\\%$ zróżnicowania. Na wykresie\npunkty bliskie sobie oznaczają kategorie silnie ze sobą powiązane\n(np. określony staż częściej niż losowo współwystępuje z określoną\nodpowiedzią PYT_2). Pierwsza oś zwykle oddaje główne przeciwstawienie\nopinii pozytywnej vs negatywnej, druga ujawnia niemonotoniczne\nkonfiguracje.",
        "**Table description 10 and Figure 3.** Combined inertia of the first two dimensions explains\n$`r round(sum(ca$explained[1:2])*100,1)`\\%$ of variation. Nearby points indicate strongly associated categories\n(e.g. a tenure level co-occurs with a PYT_2 response more than chance). The first axis usually contrasts positive vs negative opinions; the second reveals non-monotonic patterns.",
    ),
    (
        "Korelacja odległości Székely--Rizzo: $\\mathrm{dCor}(X,Y) = 0 \\iff X \\perp Y$.\nTest permutacyjny p-wartości:",
        "Székely--Rizzo distance correlation: $\\mathrm{dCor}(X,Y) = 0 \\iff X \\perp Y$.\nPermutation test p-value:",
    ),
    (
        "**Opis Tabeli \\*1.** Dla niezależnych $X, Y_1$ dCor jest bliski 0 i p-wartość\nduża. Dla zależności nieliniowej $Y_2 = X^2$ (której Pearson nie wykrywa),\ndCor wykrywa silną zależność (p-wartość $\\ll 0{,}05$).",
        "**Table description *1.** For independent $X, Y_1$, dCor is near 0 with large p-value. For nonlinear $Y_2 = X^2$ (undetected by Pearson), dCor detects strong dependence (p-value $\\ll 0.05$).",
    ),
    (
        "co oznacza, że **RR nie jest bardziej oddalone od 1 niż OR**; równość\nzachodzi dla $\\pi_1 \\to 0$.",
        "so **RR is not farther from 1 than OR**; equality holds as $\\pi_1 \\to 0$.",
    ),
    (
        "**(a)** $\\mathrm{AR} = [P(D) - P(D|E')]/P(D)$ --- jest to\n**frakcja zachorowań w populacji, którą można przypisać ekspozycji $E$**.\nLicznik to przyrost ryzyka w populacji względem scenariusza, w którym\nnikt nie jest eksponowany ($P(D|E')$). Dzieląc przez $P(D)$ otrzymujemy\nudział w całkowitej chorobowości.",
        "**(a)** $\\mathrm{AR} = [P(D) - P(D|E')]/P(D)$ is the\n**fraction of cases in the population attributable to exposure $E$**.\nThe numerator is population risk increase vs. nobody exposed ($P(D|E')$). Dividing by $P(D)$ gives share of total disease burden.",
    ),
    (
        "co kończy dowód. $\\blacksquare$",
        "which completes the proof. $\\blacksquare$",
    ),
    (
        "- Jednoczesne 95\\% PU dla wektora prawdopodobieństw odpowiedzi na PYT_1\n  wskazują na zdecydowaną dominację kategorii \"zadowolony\".\n- Napisana funkcja `p_value_multinom()` pozwala sprawnie testować\n  hipotezy o dopasowaniu do rozkładu $p_0$; rozkład odpowiedzi PYT_1\n  w dziale PD nie jest równomierny.\n- Dla par zmiennych PYT_2 × CZY_KIER wyniki testów Fishera/Freemana--Haltona,\n  $\\chi^2$ Pearsona oraz NW są zgodne: istnieje istotna zależność.\n  Agregacja PYT_2 do CZY_ZADOW zwykle osłabia moc testu.\n- Związek palenia z rakiem płuc jest znacznie silniejszy (RR $\\approx 14$)\n  niż z chorobą serca (RR $\\approx 1{,}62$).\n- Współczynniki gamma/tau oraz mapa CA dostarczają narzędzi eksploracyjnych\n  zgodnych z wynikami testów formalnych.",
        "- Simultaneous 95% CIs for the PYT_1 response probability vector show clear dominance of the \"satisfied\" category.\n- The `p_value_multinom()` function efficiently tests fit to $p_0$; PYT_1 in PD is not uniform.\n- For PYT_2 × CZY_KIER, Fisher/Freeman--Halton, Pearson $\\chi^2$, and LR agree: significant association exists. Aggregating PYT_2 to CZY_ZADOW usually reduces power.\n- Smoking–lung cancer association is much stronger (RR $\\approx 14$) than smoking–heart disease (RR $\\approx 1.62$).\n- Gamma/tau coefficients and the CA map provide exploratory tools consistent with formal tests.",
    ),
]
