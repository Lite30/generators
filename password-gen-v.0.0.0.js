/*
    author : Liteboho Maseli
    date   : 02/02/24
    title  : Password Generator
    javascript
*/

const UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const lowercase = 'abcdefghijklmnopqrstuvwxyz';
const digits = '0123456789';
const symbols = '!@#$%^&*()_+=-[]{}|;:,.<>/?';

const characters = UPPERCASE + lowercase + digits + symbols;

// Prompt user for password details
console.log('Password Generator');
console.log('================');
console.log();

console.log('Enter the length of your password: ');
const length = parseInt(prompt());

console.log('Where will the password be used?');
const designation = prompt();

// Generate password
console.log();
console.log('Generating password...');

function generatePassword(){

    function getRandom_UPPERCASE(){
        let index = Math.floor(Math.random() * UPPERCASE.length);
        return (UPPERCASE[index]);
    }
    function getRandom_LOWERCASE(){
        let index = Math.floor(Math.random() * lowercase.length);
        return (lowercase[index]);
    }
    function getRandom_DIGITS(){
        let index = Math.floor(Math.random() * digits.length);
        return (digits[index]);
    }
    function getRandom_SYMBOLS(){
        let index = Math.floor(Math.random() * symbols.length);
        return (symbols[index]);
    }
    function getRandom_CHARACTER(){
        let index = Math.floor(Math.random() * characters.length);
        return (characters[index]);
    }
    

    let $password = getRandom_DIGITS() + getRandom_SYMBOLS() + 
    getRandom_UPPERCASE() + getRandom_LOWERCASE();

    let char = ''
    function shuffle($password,char){

        for(let i = 0; i<(length - $password.length);i++)
        {
            char += getRandom_CHARACTER();
        }
        return char;
    }


    $password += "".concat(shuffle($password, char));

    return $password;

}
const $password0 = generatePassword();

// Display password
console.log();
console.log('Your password is:');
console.log($password0);
