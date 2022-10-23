/**
* Write a function called randomGame that selects a random number 
* between 0 and 1 every 1000 milliseconds and each time that a random number 
* is picked, add 1 to a counter. If the number is greater than .75, 
* stop the timer and console.log the number of tries it took before we 
* found a number greater than .75.
*/

const randomGame = () => {
    let counter = 0;
    let newNum = 0;

    let myInterval = setInterval(() => {
        newNum = Math.random();
        console.log(newNum);
        if (newNum >= 0.75) {
            clearInterval(myInterval)
            console.log(`It took ${counter} tries.`)
        } else {
            counter++;
        }
    }, 1000);
}

randomGame();
