
// Exercise 1 starts

// 1,Remove Banana from the array.
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift ();
// 2,Sort the array in alphabetical order.
fruits.sort ();

// 3,Add “Kiwi” to the end of the array.
fruits.push ("Kiwi");
// 4,Remove “Apples” from the array. Don’t use the same method as in part 1.
let deleteitem = fruits.indexOf ("Apples"); 
fruits.splice (deleteitem,1); // Alternative: splice (0,1);

// 5,Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.reverse ();
// 6,At the end you should see this outcome:
console.log (fruits);
// Exercise 1 ends


// Exercise 2 starts
// Access and then console.log “Oranges”.
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log=(moreFruits [1][1][0]);
// Exercise 2 ends

