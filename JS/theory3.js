let employee = {
    firstName: "Peter", lastName: "Peterson",
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}

//console.log(employee.fullName());   // Peter Peterson

let a = this;
//console.log(a);  // Window

"use strict";
function userFunction() {
    return this;
} // undefined}

//console.log(userFunction())

// In HTML event handlers, this refers to the HTML element that received the event:
//<button onclick="this.style.display='none'">
//    Click to Remove Me!
//</button>

const person = {
  firstName: "John",
  lastName: "Brzenk"
};
function getFullName() {
  console.log( this.firstName + " " + this.lastName );
}
// function is called with this=person
//getFullName.call(person) // "John Brzenk"

const existArr = ['John', 'Peter', 'Sam', 'Kate'];
const newArr = [1, 2, 3, 4];
existArr.push.apply(existArr, newArr);
//console.log(existArr); // ["John", "Peter", "Sam", "Kate", 1, 2, 3, 4]

const module_ = {
  	    x: 42,
  	    getX: function() {
    	       return this.x;
  	    }
	};
const unboundGetX = module_.getX;
//console.log(unboundGetX()); // The function gets invoked at the global scope
// expected output: undefined

const boundGetX = unboundGetX.bind(module_);
//console.log(boundGetX());

class Student {
  constructor(name) {
    this.name = name;
  }
  showName() {
    //alert(this.name);
      console.log(this.name);
  }
}
// Using:
let student = new Student("Sam");
//student.showName();  // Sam

class Book {
  static publishingYear = 2015;
  constructor(author) {
    this.bookname = author;
  }
  static readBook() {
    return "You reading new book!";
  }
};
let newbook = new Book("Dumas");
//console.log(newbook.readBook());  // Error
//console.log(Book.readBook());   // "You reading new book!“
//console.log(Book.publishingYear); // 2015

class User {
  constructor(name) { this._name = name; }
  get _name() {
    return this._name;
  }
  set _name(value) {
      console.log(value.length)
    if (value.length < 4) {
      //alert("Name is too short");
      console.log("Name is too short");
      return;
    }
    this._name = value;
  }
}
//let user = new User("Garry");
//console.log(user.name); // Garry call getter
//let user2 = new User("Bob"); // Name is too short
//user2.name = "David"; // call setter
//console.log(user2.name);

let sym = Symbol();
//console.log( Symbol("name") == Symbol("name") );  // false

let data1 = Symbol.for("data");
let data2 = Symbol.for("data");
//console.log(data1 === data2); // true

let key = Symbol("key");
let person_ = {
    position: "webDev",
 experience: 3,
    [key]: 100
};
// for (let props in person_) {
// console.log(props);	// position, experience
// }
// console.log(person_[key]); // 100

//const set = new  Set( [args] ); add(value) delete(value) has(value) clear() size

const cities = new Set();
const kyiv = "Kyiv";
const rome = "Rome";
const berlin = "Berlin";
const madrid = "Madrid";
cities.add(kyiv);
cities.add(rome);
cities.add(berlin);
cities.add(madrid);
cities.add(kyiv);

// console.log(cities.size); // 4
// console.log(cities.has(berlin)); // true
// // Iterator
// for (let city of cities) {
//     console.log(city);
// }
//   // Kyiv Rome Berlin 			  // Madrid

let set = new WeakSet(); // containes objects
key = {};
// add the object to the set
set.add(key);

//const newMap = new  Map( [args] ); set(key,value) get(key) delete(key) has(key) clear() size

// const map	= new Map();
// map.set("name", "Nicholas");
// map.set("age",	25);
// console.log(map.size);			//	2
// console.log(map.has("name"));		//	true
// console.log(map.get("name"));		//	"Nicholas"
// console.log(map.has("age"));		//	true
// console.log(map.get("age"));		//	25
// map.delete("name");
// console.log(map.has("name"));		//	false
// console.log(map.get("name"));		//	undefined
// console.log(map.size);			//	1
// map.clear();
// console.log(map.has("age"));		//	false
// console.log(map.get("age"));		//	undefined
// console.log(map.size);			//	0

// const recipeMap = new Map([
//   ['cucumber', 500],
//   ['tomatoes', 350],
//   ['onion',    50]
// ]);
// for (let vegetable of recipeMap.keys()) {
//   //alert(vegetable); // cucumber, tomatoes, onion
//     console.log(vegetable);
// }
// for (let amount of recipeMap.values()) {
//   //alert(amount); // 500, 350, 50
//     console.log(amount);
// }
// for (let entry of recipeMap) { // the same as
// // of recipeMap.entries()
//   //alert(entry); // cucumber,500 (and so on)
//     console.log(entry);
// }

// const weakMap = new WeakMap(); //set(key,value) get(key) delete(key) has(key)
// const obj = {};
// weakMap.set(obj, "data");  // works fine (object key)
// // incorrectly use string as a key
// weakMap.set("key", "value");// error, because "key" is not an object


