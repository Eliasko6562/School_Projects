let person = {
    firstname: '',
    gender: 'man',
    age: 17,
    weight: 70,
    height: 170,

    cmToMetres: function(cm) {
        return Number.isInteger(cm) ? cm / 100: false;
    },
    bmi: function(w = this.weight, h = this.height) {
        return (w / Math.pow(this.cmToMetres(h),2)).toFixed(2); 
    },

    state: function() {
        let bmi = this.bmi();
        if (bmi < 18.5) return 'underweight';
        if ((bmi >= 18.5) && (bmi < 25)) return 'optimal weight';
        if ((bmi >= 25) && (bmi < 30)) return 'overweight';
        if ((bmi >= 30 ) && (bmi < 40)) return 'obesity';
        return 'severe obesity';
    }
}

console.log(person.bmi());
console.log(person.state());