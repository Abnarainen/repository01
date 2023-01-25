// Exercise 1 starts

// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.
let x = 5;
let y = 2;
 if (x > y) {
    console.log ("X is the biggest number");
 } else if (x == y) {
    console.log ("Both are equal");
 } else {
    console.log ("Y is the biggest number");
 }
// Exercise 1 ends


// Exercise 2 starts

// 1,Create a variable called newDog where it’s value is “Chihuahua”.
const newDog = ("Chihuahua");

// 2,Check and display how many letters are in newDog.
Console.log=("The number of letters are:", newDog.length);

// 3,Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

// 4,Check if the variable newDog is equal to “Chihuahua”
// 5,if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// 6,else, console.log ‘I dont care, I prefer cats’
if (newDog === "Chihuahua"){
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats"); 
}
// Exercise 2 ends


// Exercise 3 starts

// 1,Prompt the user for a number and save it to a variable.
const result = prompt("Input a number");

// 2,Check whether the variable is even or odd.
// 3,If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// 4,If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
if (number(result) % 2 === 0){
    console.log (result + " is an even number");
} else {
    console.log (result + " is an odd number");
}
// Exercise 3 ends

// Exercise 4 starts
// 1,Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
// 2,If there is no users (the users array is empty), console.log “no one is online”.
// 3,If there is 1 user, console.log “<name_user> is online”.
// 4,If there are 2 users, console.log “<name_user1> and <name_user2> are online”.

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users.length === 0) {
    console.log ("No one is online");
} else if (users.length === 1) {
    console.log (users +" is online");
}  else if (users.length === 2) {
    console.log (users[0] +" and "+ users[1]+ " is online");
}

// 5,If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display:

if (users.length > 2) {
    console.log (`${users [0]}, ${users [1]} and ${users.length - 2} more are currently online`);
}
// Exercise 4 ends