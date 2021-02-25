//String Number Boolean Undefined Null Symbol Object
let x; // type undefined
console.log(x); // undefined

x = 45; // type number
console.log(x); // 45

x = "45"; // type string
console.log(x); // "45"


let num =+ x //convert to number
console.log(typeof num)

let a = 20;
let data = String(a);
console.log(data); 			 // "20"
console.log(typeof data); // "string"

let data1 = a + "";
console.log(data1); 			 // "20"
console.log(typeof data1); // "string"

console.log(parseInt("7")); // 7
console.log(parseInt("7.5")); // 7
console.log(parseInt("7nm")); // 7
console.log(parseInt("nm")); // NaN

console.log(parseFloat("7")); // 7
console.log(parseFloat("7.125")); // 7.125
console.log(parseFloat("7nm")); // 7
console.log(parseFloat("nm")); // NaN

console.log(isNaN(1)); // false
console.log(isNaN("1")); // false
console.log(isNaN("1m")); // true
console.log(isNaN(null)); // false
console.log(isNaN(undefined)); // true

let a2 = "1";
let bln = Boolean(a2);
console.log(bln); // true
console.log(typeof bln); // "boolean"

let a1 = "1";
let bln1 = !!a1;
console.log(bln1); // true
console.log(typeof bln1); // "boolean"

const arr = [];
const arr1 = new Array();

const cities = ["Rome", "Lviv", "Warsaw"];
for (let i of cities) {  // run 3 times
   console.log(i); // Rome, Lviv, Warsaw
}

const cities1 = ["Rome", "Lviv", "Warsaw"];
for (let i = 0; i < cities1.length; i++) {   // run 3 times
   console.log(cities1[i]);  } // Rome, Lviv, Warsaw

// Arrays provide many methods:
// push(... items) - adds items to the end of the array
// pop() - removes the element at the end of the array and returns it.
// shift() - removes the element at the beginning of the array and returns it.
// unshift(... items) - adds items to the beginning of the array.
// slice(start, end) – creates a new array, copying elements from start to end (not including end) into it.
// splice(pos, deleteCount, ...items) – starting at the pos index, removes deleteCount items and inserts items.
// concat(...items) – returns a new array: copies all members of the current array and adds items to it.
// forEach(func) – calls func for each element (enumeration)
// map() – creates a new array with the results of calling a function for every array element.

const cities2 = ["Rome", "Lviv", "Warsaw"];
const newArr = cities2.filter(function(citie) { return citie.length < 5 });
console.log(newArr); // ["Rome", "Lviv"]

const newArr1 = cities2.map( function(city) { return city + "Capital" });
console.log(newArr1); [ 'RomeCapital', 'LvivCapital', 'WarsawCapital' ]

//The reduce() method performs the reducer function you specified for each element of the array and returns a single value.
const data2 = [2, 4, 6, 8];
function reducer(total, value) { return total + value; }
const sum = data2.reduce(reducer); // 20
console.log(sum);



