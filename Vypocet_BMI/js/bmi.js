/* Využití pole objektů k zachycení tabulky BMI podle věkových kategorií */
const bmiCategories = [
    /* Každý objekt v poli obsahuje atribut age (určení věkové kategorie) 
       a atribut weight (hraniční váhy pro označení stavu, v němž se dotyčná osoba nachází).
       V případě atributu weight bylo opět využito pole, aby mohly být na jednom místě shromážděny všechny hodnoty. */
    { age: '18-24', weight: [19, 24, 29, 39] },
    { age: '25-34', weight: [20, 25, 30, 40] },
    { age: '35-44', weight: [21, 26, 31, 41] },
    { age: '45-54', weight: [22, 27, 32, 42] },
    { age: '55-64', weight: [23, 28, 33, 43] },
    { age: '65+', weight: [24, 29, 34, 44] }
];

/* Testovací příklady, jak v poli bmiCategories najít objekt pro určitou věkovou kategorii. */
/* a) Varianta s použitím tzv. callback funkce předané metodě find. */
console.log(bmiCategories.find(function(obj) { return obj.age === '18-24'} ));
/* b) Novější "zkrácená" varianta využívající tzv. arrow funkce */
console.log(bmiCategories.find(obj => obj.age === '65+'));

/* Proměnná person obsahuje typ objekt tvořený atributy a metodami. */
let person = {
    /* Atributy objektu */
    firstname: '',
    sex: '',
    age: '',
    weight: 0,
    height: 0,
    /* Metody objektu */
    /* Pomocná metoda cmToMetres() převádí údaj z [cm] na [m]. */
    cmToMetres: function(cm) {
        return cm / 100;
    },
    /* Metoda bmi() vypočítá hodnotu BMI pro danou osobu. */
    /* Parametr w je přednastaven podle aktuální váhy osoby, parametr h podle její výšky. */
    bmi: function(w = this.weight, h = this.height) {
        /* Metoda Math.pow() umožňuje umocnění, metoda toFixed() zajistí zaokrouhlení na určitý počet 
           desetinných míst. */
        return (w / Math.pow(this.cmToMetres(h),2)).toFixed(2); 
    },
    /* Metoda state() slouží k vyhodnocení stavu BMI dané osoby podle zjištěné hodnoty. */
    state: function() {
        /* Do proměnné bmi je uložena hodnota BMI dané osoby. */
        let bmi = this.bmi();
        /* Do proměnné bmiCategory je vyhledán objekt odpovídající věkové kategorii dané osoby. */
        let bmiCategory = bmiCategories.find(obj => obj.age === this.age);
        /* Podmínky otestují, v jakém stavu je z pohledu BMI s ohledem na věkovou kategorii daná osoba. */
        /* Klíčové slovo return zajistí okamžité ukončení metody (funkce) s potřebnou návratovou hodnotou. */
        if (bmi < bmiCategory.weight[0]) return 'podváha';
        if ((bmi >= bmiCategory.weight[0]) && (bmi < bmiCategory.weight[1])) return 'optimální váha';
        if ((bmi >= bmiCategory.weight[1]) && (bmi < bmiCategory.weight[2])) return 'nadváha';
        if ((bmi >= bmiCategory.weight[2]) && (bmi < bmiCategory.weight[3])) return 'obezita';
        return 'silná obezita';
    }
}

/* Test metody bmi() */
console.log(person.bmi(90,180));
/* Test funkčnosti objektu person */
person.firstname = 'Ruda';
person.sex = 'muž';
person.age = '65+';
person.weight = 85;
person.height = 171;
/* Test výpisu objektu */
console.log(person);
/* Test metody bmi() */
console.log(person.bmi());
/* Test metody state() */
console.log(person.state());

/* Ohlasová metoda - kliknutí na tlačítko "Vypočítat" */
document.getElementById('calc').addEventListener('click', function() {
    /* Předání hodnot z formuláře do atributů objektu person */
    person.firstname = document.getElementById('firstname').value;
    /* Použití ternárního operátoru pro ověření stavu přepínače */
    person.sex = document.getElementById('woman').checked ? 'žena' : 'muž';
    person.age = document.getElementById('age').value;
    person.weight = document.getElementById('weight').value;
    person.height = document.getElementById('height').value;
    /* Výpis informací do oddílu určeného pro výstup aplikace */
    document.getElementById('result').innerHTML = `${person.firstname} (${person.sex}): BMI = ${person.bmi()}, ${person.state()}`;        
});