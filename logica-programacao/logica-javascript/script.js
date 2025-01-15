// Let: Variáveis que podem ser alteradas no decorrer da aplicação.
let nome = 'Marcos';
let Nome = 'Mariá';

// Simbologia nas variavels, somente _ e $
let _nome = 'George';
let $nome = 'Norberto';

// Case Sensitive: O uso de letras maiusculas e minusculas faz diferenteça

// Camel Case: É uma escrita que lembra a corcunda de um camelo. A primeira palavra minuscula, a primeira letra das palavras seguintes, maiusculas.
let sobreNome = 'Monte';

// Imprimindo no Console as Variaveis
console.log(nome, sobreNome, Nome, sobreNome )

// Const: Variáveis imutáveis, não podem ser redeclaradas
const anoNascimento = 1988; // Tipo NUMBER
const _anoNascimento = '1988'; // Tipo STRING

// Saber o tipo da variavel
console.log(typeof anoNascimento);
console.log(typeof _anoNascimento);

// Tipos de Variáveis
let numero = 36; // Tipo numerico, não é envolvido por asppas
let texto = `Marcos Monte`; // Tipo texto, é envolvido por: '' ou "" ou ``
let boleana = true; // Tipo booleano, pode ser verdadeiro ou falso
let templateString = `${texto} acabou de fazer ${numero} anos!!!`

console.log(numero, texto, boleana)
console.log(templateString)

// Tipos de Erros ou mensagens:
let tipoNull = null // É algo, propositalmente, vazio.
let tipoUndefined = undefined // É algo sem valor definido. (Mensagem de erro: Está sendo chamado algo que ainda não foi definido)
let tipoNaN = NaN // Not a Number. Não é um valor numérico.

console.log(tipoNull, tipoUndefined, tipoNaN)