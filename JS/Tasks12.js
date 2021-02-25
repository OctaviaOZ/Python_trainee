function getMin1(numbers) {
    {min_prop : return numbers.reduce(
        (min, currentValue) => min < currentValue ? min : currentValue)}
    return this.min_prop;
}

const getMin = function(numbers) {
    return [].reduce.call(numbers, function(min, elem){return min < elem ? min : elem;
    }, this.getMin);
};

//console.log(getMin([12, 6, 22, 13, 7]));

const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
      return res * elem;
    }, this.product);
};

const contextObj = { product: 2 * 3 };

const getProduct = function() {
     return product.apply(contextObj, arguments);
}

//console.log(getProduct(4,5));

//const Checker = require('./Checker.js');

class Movie {
    constructor(name, category, startShow) {
    this.name = name;
    this.category = category;
    this.startShow = startShow;
    }

    watchMovie(){
        return `I watch the movie ${this.name}!`;
    }
}

// let movie1 = new Movie("Titanic", "drama",1997);
// let movie2 = new Movie("Troya", "historical",2004);
// console.log(movie1.watchMovie())

class Student  {
    constructor(fullName, direction){
        this._fullName = fullName;
        this._direction = direction;
    }
    showFullName(){
        return `${this._fullName}`;
    }
    nameIncludes(data){
        return this._fullName.includes(data);
    }
    static studentBuilder(){
        return new Student("Ihor Kohut", "qc");
    }
    get direction() {
        return this._direction;
    }
    set direction(value){
        this._direction = value;
    }
}

// let stud1 = new Student("Ivan Petrenko", "web");
// let stud2 = new Student("Sergiy Koval", "python");
// let stud3 = Student.studentBuilder()
//
// console.log(stud1.nameIncludes('Ivan'));   // true


function mapCreator(keys, values) {
   const map = new Map();
   for(let i = 0; i < keys.length; i++){
       if(typeof values[i] === 'string')
           map.set(keys[i], values[i]);
    }
   return map;
}

const map = mapCreator([1, 2, 3, 4, 5, 6, 7],["Lviv", "Rivne", "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", "Ivano-Frankivsk"]);