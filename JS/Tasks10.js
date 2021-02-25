//coveralls.io 

function modifyArray(arr) {
  arr[0] = "Start";
  arr[arr.length - 1] = "End";
  return arr
}

//console.log(modifyArray([12, 6, 22, 0, -8]));

function combineArray(arr1, arr2) {
    const newArr = arr1.filter(n => typeof(n)==='number').concat(arr2.filter(n => typeof(n)==='number'));
    return newArr

}

//console.log(combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]))

let longestLogin = function(loginList){
     var MaxValue = loginList.reduce(
        (max, currentValue) => {
             return (max.length > currentValue.length ? max : currentValue);
        }
    );

     return MaxValue;
 }

//console.log(longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]))

function factorial(n) {
    return (n != 1) ? n * factorial(n - 1) : 1;
}

function factorial(n) {
    if (n < 2)
        return 1;
    let result = 1;
    for (let i = 1; i != n+1; i++) {
 			result *= i;
   }
    return result;
}

function processArray(arr, func) {
    const newArr = arr.map( function (x) {
        return func(x);
    });
    return newArr
}

function checkAdult(age)  {
    try {
        switch (True) {
            case (age === undefined):
                throw new Error("Please, enter your age");
            case (age < 0):
                throw new Error("Please, enter positive number");
            case (!typeof (age) === 'number'):
                throw new Error("Please, enter number");
            case !Number.isInteger(age):
                throw new Error("Please, enter Integer number");
            case (age < 18):
                throw new Error("Access denied - you are too young!");

            default:
                console.log("Access allowed");
        }
    }
    catch (exception) { // error object
        console.log(exception.name + " " + exception.message);
    }
     finally {
        console.log("Age verification complete");
    }
}


const salary = [550, 900, 1800, 2200];
salary.unshift(1000, 1350);
//console.log(salary)

const arr1 = ["User1", "User2"]
const arr2 = [1, 2, 3]
//arr.concat(arr1, arr2);
let arr = [...arr1, ...arr2]
console.log(arr)

//console.log(Math.floor(16.5))
//console.log("a"+"a"+ +"a"+"a")

