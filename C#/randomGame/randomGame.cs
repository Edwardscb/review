/*
Write a function called randomGame that selects a random number 
between 0 and 1 every 1000 milliseconds and each time that a random number 
is picked, add 1 to a counter. If the number is greater than .75, 
stop the timer and console.log the number of tries it took before we 
found a number greater than .75.
*/


Random rnd = new Random();
// states Random first to represent that it is of class Random, then new Random()
// states that it is a new Random instance

double newNum = 0;
int counter = 0;


while (newNum <= 0.75) {
    counter++;
    newNum = rnd.NextDouble();
    Console.WriteLine(newNum);
    await Task.Delay( TimeSpan.FromSeconds(1));
}
Console.WriteLine($"Number of tries to >= 0.75 = {counter}");
