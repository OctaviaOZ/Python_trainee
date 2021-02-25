const filterNums1 = (arr, number=0, parameter='greater') => {
    let newArr = arr.filter(value => (parameter === 'greater' && value > number)
    || (parameter === 'less' && value < number));
    return newArr
};

const filterNums = (arr, number=0, parameter='greater') => {
    return arr.filter(el => parameter == 'less' ? el < number : el > number);
};

function getCond(num, greater){
    if(greater == 'greater')
        return (el) => el > num
    else
        return (el) => el < num
}

const filterNums2 = (arr, num=0, greater='greater') => {
    return arr.filter(getCond(num, greater));

}


console.log(filterNums2([-2, 2, 3, 0, 43, -13, 6], 6, 'less'));

const howMuchSec = (seconds_=0, minutes_=0, hours_=0, days_=0, weeks_=0, months_=0, years_=0) =>{
    let val = {
        min_to_sec   : 60,
        hour_to_sec  : 3600,
        day_to_sec   : 86400,
        week_to_sec  : 604800,
        month_to_sec : 2592000,
        year_to_sec  : 31536000
    }
    //3600*24=86400 seconds per day
    //3600*24*7=604800 seconds per week
    //3600*24*30=2592000 seconds per months
    //3600*24*365=31536000 seconds per year
    return seconds_ + minutes_* val.min_to_sec + hours_* val.hour_to_sec + days_* val.day_to_sec +
        weeks_* val.week_to_sec + months_* val.month_to_sec + years_* val.year_to_sec
}

console.log(howMuchSec(12, 3))

const maxInterv1 = (...arr) => {
    var MaxInterval = arr.reduce(
        (maxInt, currentValue, index) => {
             return (maxInt > Math.abs(currentValue - arr[index-1]) ?
                 maxInt : Math.abs(currentValue - arr[index-1]));
        }
        , 0);
    if(isNaN(MaxInterval)) MaxInterval = 0;
    return MaxInterval;
 }

const maxInterv = (...arr) => {
    let interval = 0;
    for(let i = 1; i < arr.length; i++){
        const interv = Math.abs(arr[i - 1] - arr[i]);
        if(interv > interval){
            interval = interv;
        }
    }
    return interval;
}

console.log( maxInterv(8))

const sumOfLen = (...strings) => {
     return strings.reduce(
        (sum, currentString) => sum + currentString.length, 0);
 }

//console.log(sumOfLen('hello', 'hi'));