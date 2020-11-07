// Write a function to return true if a number is prime and
// false if it isn't

function isPrime(number) {
    // first check the data type of the input
   if (typeof number !== 'number' || !Number.isInteger(number)) {
      return false;
   }

   // negative numbers, 0 and 1 are not prime
   if (number < 2) {
      return false;
   }

   // the number 2 is prime, and anything divisible by 2 is not prime
   if (number === 2) {
      return true;
   } else if (number % 2 === 0) {
      return false;
   }

   // only test numbers up to the square root
   var squareRoot = Math.sqrt(number);
   for(var i = 3; i <= squareRoot; i += 2) {
      if (number % i === 0) {
         return false;
      }
   }

   return true;
}

console.log(isPrime(6));
console.log(isPrime(11));
console.log(isPrime("a"));
