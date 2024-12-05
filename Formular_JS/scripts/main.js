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


document.getElementById('calculate').addEventListener('click', function() {
    if (time.value < 1){
        errorTime.innerHTML = ('Cas musi byt vetsi nez 0');
        document.getElementById('time').style.animation = 'shake 0.2s ease-in-out 0s 2';
        return;
    }
    objekt.distance = distance.value;
    objekt.time = time.value;

    result.innerHTML = objekt.speed();
});

