// Operadores Aritméticos
let numero = 5;

console.log(`Adição: ${numero + numero}`)
console.log(`Subtração: ${numero - numero}`)
console.log(`Multiplicação: ${numero * numero}`)
console.log(`Divisão: ${numero / numero}`)
console.log(`Resto da Divisão: ${numero % numero}`)

// Operadores de Comparação
let num1 = 8;
let num2 = "8";

console.log(`Valores: ${num1, num2}`);
console.log(`Comparando valores: ${num1 == num2}`); // true
console.log(`Comparando valores e tipo: ${num1 === num2}`); // false
console.log(`Comparando (dif) valores: ${num1 != num2}`); // false
console.log(`Comparando (dif) valores e tipo: ${num1 !== num2}`); // true

console.log(`Maior que 2: ${num1 > 2}`); // true
console.log(`Menor que 2: ${num1 < 2}`); // false

console.log(`Maior ou igual a 2: ${num1 >= 2}`); // true
console.log(`Menor ou igual a 2: ${num1 <= 2}`); // false

// Condicionais

    // IF - ELSE
    let numeroDaSorte = 7;

    if(numeroDaSorte == 8){
        console.log('Boooaaaa....')
    } else {
        console.log('Errrrrooouuu')
    }

    // IF - ELSE IF - ELSE
    let carro = 'logan';
    let placa = 1234

    if(carro === 'uno' && placa === "1234"){

        console.log('Carro é seu!!!')

    } else if(carro === 'uninho' || placa === "1234") {

        console.log('Medidas administrativas!!!')

    } else {

        console.log('Perdeu, carro clonado!!!')
        
    }
