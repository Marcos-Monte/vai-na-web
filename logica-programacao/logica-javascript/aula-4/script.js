// Métodos: são gatilhso de funções que já tem uma funcionalidade embutida em JS. Métodos de inclusão e exclusão de itens.

// Array 
let cantoras = [
    "Beyoncé",
    "Alicia Keys",
    "Jennifer Lopez",
    "Shakira",
    "Madonna",
    "Avril Lavigne",
    "Mariah Carey",
    "Pink",
    "Britney",
    "Ariana Grande",
    "Lary Gaga", 
];

// Relembrando Métodos Principais de Array
// push() - Adiciona elemento no final do array
// pop() - Remove elemento no final do array
// unshift() - Adiciona elemento no inicio do array
// shift() - Remove elemento no inicio do array

cantoras.push('Taylor Swift'); // Adiciona elemento no final do array
cantoras.unshift('Adelle'); // Adiciona elemento no inicio do array
cantoras.pop(); // Remove elemento no final do array
cantoras.shift(); // Remove elemento no inicio do array

// Métodos Length = Diz a quantidade de itens que existem dentro do array
let quantidadeItens = cantoras.length

// console.log(quantidadeItens);
// console.log(cantoras)

// Método SLICE = tem o poder de substituir, adicionar e remover itens
// Indices:             0           1        2       3
let instrutoress = ['Karynne', 'Samuel', 'João', 'Joy']

console.log(instrutoress)
// ['Karynne', 'Samuel', 'João', 'Joy']

// Exemplo 1 SPLICE -> Substituir: O 1º é o Indice, o 2º é a quantidade e o 3º vai ser o 'valor'
instrutoress.splice(3, 1, 'Marcos', )

console.log(instrutoress)
//  ['Karynne', 'Samuel', 'João', 'Marcos']

// Exemplo 2 SLICE -> Adicionar: O 1º é o Indice, o 2º deve ser ZERO (0 quer dizer que não quero remover nenhum item) 3º é o 'valor
instrutoress.splice(2, 0, 'Godofredo', 'Veho')

console.log(instrutoress)
// ['Karynne', 'Samuel', 'Godofredo', 'Veho', 'João', 'Marcos']

// Exemplo 3 SLICE -> Remover: O 1º é o Indice, o 2º é a quantidade
const indiceInstrutor = instrutoress.indexOf('Godofredo');
const qtde = instrutoress.length
instrutoress.splice(indiceInstrutor, qtde)

console.log(instrutoress)
//  ['Karynne']

// Método SLICE = retorna uma cópia do Array sem alterar o Original.

console.log(cantoras.slice(1,3)) // A partir do indice 1, retorn 3 itens
// ['Alicia Keys', 'Jennifer Lopez']

