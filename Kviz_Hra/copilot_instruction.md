Čtvrtletní projekt z programování v Pythonu

Interaktivní soutěžní aplikace pro znalostní soutěž základních škol

Kontext projektu

Škola připravuje znalostní soutěž pro tříčlenné týmy žáků základních škol. Jedním z cílů soutěže je zařadit moderní interaktivní úkoly, které budou soutěžící nejen zkoušet ze znalostí informačních technologií, ale také je zaujmou svou hravou formou.

Vaším úkolem bude navrhnout a vytvořit soutěžní aplikaci v jazyce Python. Aplikace musí být použitelná při skutečné soutěži, musí být přehledná pro obsluhu i soutěžící a musí obsahovat ochranu proti snadnému odhalení správných odpovědí.

Studenti si zvolí jednu ze dvou variant projektu, nebo po dohodě vytvoří rozšířenou verzi kombinující prvky obou variant.

Varianta A: Odhalování obrázku a tajenky

Aplikace pracuje s obrázkem známé osobnosti, loga, zařízení, historické fotografie, screenshotu nebo jiného objektu z oblasti IT. Obrázek je na začátku skrytý a rozdělený na mřížku 4 × 4. Soutěžící si postupně vybírají políčka, která chtějí odhalit. Současně mohou získávat i písmenové nápovědy ke správnému řešení.

Řešením může být například jméno osobnosti, název firmy, technologie, zařízení nebo pojmu. Pod obrázkem se zobrazují pole odpovídající jednotlivým znakům řešení. Aplikace musí umožnit odhalování částí obrázku i jednotlivých písmen. Každá nápověda snižuje bodový zisk. Za chybný pokus o vyřešení se odečítá výraznější počet bodů.

Typický průběh hry

Na začátku má tým například 120 bodů. První odkryté políčko obrázku může být zdarma, druhé za −1 bod, třetí za −2 body, čtvrté za −3 body atd. Stejný nebo podobný princip může být použit i pro odhalování písmen. Pokud tým zadá špatné řešení, ztratí například 20 bodů. Hra je časově omezená, například na 10 minut. Po vypršení času se kolo automaticky ukončí.