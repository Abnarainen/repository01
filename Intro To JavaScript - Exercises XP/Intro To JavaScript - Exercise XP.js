
// Exercise 1 starts
// 1,Store your favorite food into a variable.
let myFavoriteFood = "Fried Noodle";
// 2,Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)
let myFavoriteMeal = "Dinner";
// 3,Console.log I eat <favorite food> at every <favorite meal>
console.log = (`I eat ${myFavoriteFood} at every ${myFavoriteMeal}`);
// Exercise 1 ends


// Exercise 2 starts
// part 1 start

// 1,Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
myWatchedSeriesLength = myWatchedSeries.length;
console.log(myWatchedSeriesLength);

// 2,Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

let myWatchedSeriesSentence = `${myWatchedSeries [0]}, ${myWatchedSeries [1]} and ${myWatchedSeries [2]}`;

// 3,Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory
console.log("I watched 3 series", myWatchedSeriesSentence);
// part 1 ends


// part 2 starts
//  Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
let index = myWatchedSeries.indexOf ("the big bang theory");
myWatchedSeries [index] = "Friends";

// Add, at the end of the array, the name of another series you watched.
myWatchedSeries.push ("Peaky Blinders");

// Add, at the beginning of the array, the name of your favorite series.
myWatchedSeries.unshift ("Narcos Mexico");

// Delete the series “black mirror”.
let indexBlack = myWatchedSeries.indexOf ("black mirror");
myWatchedSeries.splice (indexBlack,1);

// Console.log the third letter of the series “money heist”.
console.log (myWatchedSeries [1] [2]);

// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.
 console.log (myWatchedSeries);
// part 2 ends
// Exercise 2 ends


// Exercise 3 starts
// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32
let culsiusTemperature= prompt("Select your temperature");
let fahrenheitTemperature = (culsiusTemperature * 1.8) + 32;
console.log (`${culsiusTemperature}°C is ${fahrenheitTemperature}°F`);
// Exercise 3 ends

// Exercise 4 starts
let c;
let a = 34;
let b = 21;

console.log(a+b) //First expression
// Prediction:  It will output 55, because 34 and 21 are numbers
 // Actual: 55
 a = 2;

 console.log(a+b) //second expression
 // Prediction: It will output 23, because a is now 21
 // Actual: 23

 console.log(3 + 4 + '5');
 // Prediction:  It will output 75 because 3 and 4 are numbers, and '5' is a string
 // Actual: 75
// Exercise 4 ends

// Exercise 5 starts
typeof(15)
// Prediction: It will output number because it is a number
// Actual: number

typeof(5.5)
// Prediction: It will output number because it is a number
// Actual: number

typeof(NaN)
// Prediction: It will output number because it is a number
// Actual: number

typeof("hello")
// Prediction: It will output string because it is a text
// Actual: string

typeof(true)
// Prediction: It will output boolean because it can only take values "True or False"
// Actual: boolean

typeof(1 != 2)
// Prediction: It will output boolean because it is "True or False"
// Actual: boolean

"hamburger" + "s"
// Prediction: It will output hamburgers as both are strings and they will concatenate
// Actual: hamburgers

"hamburgers" - "s"
// Prediction: It will output NaN as both are not numbers
// Actual: Nan

"1" + "3"
// Prediction: It will output 13 as both are strings are and they will concatenate
// Actual: 13

"1" - "3"
// Prediction: It will output -2 JS is smart enough to change the type despite they were string
// Actual: -2 

"johnny" + 5
// Prediction: It will output Johnny5 as Johnny is a string and 5 a nummber.
// Actual: Johnny5

"johnny" - 5
// Prediction: It will output NaN as both are not numbers
// Actual: NaN

99 * "hello"
// Prediction: It will output NaN as Hello are not numbers
// Actual: NaN

1 != 1
// Prediction: It will output False as 1 is equal to 1
// Actual: False

1 == "1"
// Prediction: It will output True as JS converse the string "1"
// Actual: True

1 === "1"
// Prediction: It will output False as "1" is a is string (different type)
// Actual: False

// Exercise 5 ends


// Exercise 6 starts

5 + "34"
// Prediction: It will output 534 as "34" is a string and 5 is a nummber.
// Actual: 534

5 - "4"
// Prediction: It will output 1 as JS is smart enough to change the type despite "4" was a string
// Actual: 1

10 % 5
// Prediction: It will output 0 as there is no remainder
// Actual: 0

5 % 10
// Prediction: It will output 5 as there is a remainder of 5
// Actual: 5 

"Java" + "Script"
// Prediction: It will output JavaScript as both are strings and they will concatenate
// Actual: JavaScript

" " + " "
// Prediction: It will output '  ' as the addition will make 2 spaces
// Actual: '  '

" " + 0
// Prediction: It will output ' 0' 
// Actual: ' 0'

true + true
// Prediction: It will output 2 because it is a boolean and will make an addtion instead of concatenate
// Actual: 2

true + false
// Prediction: It will output 1 because it is a boolean and will make an addtion instead of concatenate
// Actual: 1

false + true
// Prediction: It will output 1 because it is a boolean and will make an addtion instead of concatenate
// Actual: 1

false - true
// Prediction: It will output -1 because it is a boolean and will make a subtraction. It is same as (0-1)
// Actual: -1

!true
// Prediction: It will output false because it is a not operator and it call for the opposite of true
// Actual: false

3 - 4
// Prediction: It will output -1 because both are numbers
// Actual: -1

"Bob" - "bill"
// Prediction: It will output NaN as both are not numbers
// Actual: Nan

// Exercise 6 ends