let person = {
    firstname: '',
    gender: 'man',
    age: 17,
    weight: 70,
    height: 170,
    cmToMetres: function(cm) {
        return cm / 100;
    },
    bmi: function(w = this.weight, h = this.height) {
        return (w / Math.pow(this.cmToMetres(h),2)).toFixed(2); 
    },
    state: function() {
        let bmi = this.bmi();
        let bmiCategory = bmiCategories.find(obj => obj.age === this.age);
        if (bmi < bmiCategory.weight[0]) return 'underweight';
        if ((bmi >= bmiCategory.weight[0]) && (bmi < bmiCategory.weight[1])) return 'optimal weight';
        if ((bmi >= bmiCategory.weight[1]) && (bmi < bmiCategory.weight[2])) return 'overweight';
        if ((bmi >= bmiCategory.weight[2]) && (bmi < bmiCategory.weight[3])) return 'obesity';
        return 'severe obesity';
    }
}