let objekt = {
    distance: 0,
    time: 0,

    speed: function() {
        return this.distance / this.time;
    }
};

const distance = document.getElementById('distance');
const time = document.getElementById('time');
const result = document.getElementById('result');
const errorTime = document.getElementById('errorTime');
const calculate = document.getElementById('calculate');

calculate.addEventListener('click', function() {
    if (time.value < 1){
        errorTime.innerHTML = ('Čas musí být větší než 0');
        document.getElementById('time').style.border = '1px solid red';
        document.getElementById('time').style.animation = 'none';
        setTimeout(() => {
            document.getElementById('time').style.animation = 'shake 0.2s ease-in-out 0s 2';
        }, 0);
        return;
    }
    if (time.value <= 1){
        errorTime.innerHTML = ('');
        document.getElementById('time').style.border = 'none';
    }

    objekt.distance = distance.value;
    objekt.time = time.value;

    result.innerHTML = objekt.speed();
});