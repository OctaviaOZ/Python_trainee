
function showName(userName) {
	     console.log( 'Your name:' + userName);
	}

//showName("Peter"); 	// function call

function multiplication() {
   let result = 1;
   for (let i = 0; i < arguments.length; i++) {
 			result *= arguments[i];
   }
   console.log(result);
}

// multiplication(3); 			// 3
// multiplication(3, 5); 		// 15
// multiplication(3, 5, 7); 	// 105

function multiplication(a, b) {
   let result = a * b;
   return result;
}
// let result = multiplication(3, 6);
// console.log(result); // 18

function sayHello() {
   console.log("Hi!");
}
// let hello = sayHello;
// hello();    // "Hi!"

function sayHello1() {
   console.log("Hi!");
}

// sayHello1 = null;
// sayHello1();    // error
//let sendMessage = function f(){ alert('Some message');};
//sendMessage();
// try {
//       console.log('Try block start');
//       // ... Code without  errors
//       console.log('Try block end');
// } catch(error) {
//       console.log('Catch is ignored, because there are no errors');
// } finally { console.log('Finally block'); }
//
// try {
//       console.log('Try block start');
//       c = a + b; // some logic in code
//       console.log('Try block end');
// } catch(error) {
//       console.log('Error has occurred!');
// } finally { console.log('Finally block'); }

function enterPIN() {
    let pin = prompt("Enter PIN-number (max length 4):", "");
    if (pin.length > 4) {
         throw new Error("Line length greater than 4 characters");
    }
    return pin;
}
try {
    let result = enterPIN();
    console.log(result);
} catch (exception) { // error object
    console.log(exception.name); // “Error”
    console.log(exception.message); // “Line length greater than 4 characters”  
}




