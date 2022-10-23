/** 
 * Write a function called countdown that accepts a number as a parameter and every 1000 milliseconds 
 * decrements the value and console.logs it. Once the value is 0 it should log “DONE!” and stop.
 */

const countdown = (num) => {
    let x = num;
    let cd = setInterval(() => {
        if (x == 0) {
            console.log("Done!");
            clearInterval(cd);
        } else {
            console.log(x);
            x--;
        }
    }, 1000);
}

countdown(10)