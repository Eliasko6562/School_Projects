let objekt = {
    vzdalenost: "",
    cas: "",
    
    rychlost: function() {
        return (this.vzdalenost / this.cas).toFixed(2);
    }
}

console.log(objekt.rychlost());

