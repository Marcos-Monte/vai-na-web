let aluno = 'Marcos'; // Caixinha que guarda um único valor

// Objeto {} é uma coleção de informações ou propriedades. As propriedades podem ser de diferentes tipos de dados (number, string, boolean, array, object, etc). 
// const alunos = {
//     nome: 'Marcos',
//     idade: 36,
//     cor: 'preto',
//     nacionalidade: 'brasileira',
//     filhos: ['Shima', 'Morgana'],
//     professor: true
// };

// Exemplo 1: Criando um novo Objeto
let eu = {
    nome: 'Marcos',
    sobrenome: 'Monte',
    nascimento: 1988,
};

console.log(eu)

// Adicionando propriedades para dentro do Objeto.
eu.fruta = 'abacaxi';
eu.amigo = 'Jones';

console.log(eu)

// Seletando propriedades de um Objeto
delete eu.amigo; 

console.log(eu)

// Exemplo 2: Criando um novo Objeto
let carro = {
    marca: 'Fiat',
    modelo: 'Uno',
    pesoKg: 1500,
    velocidade: 120,
    pesoComEscadaKg: 50,
    velocidadeComEscada: 1000,
    cor: 'branco',
    preco: 50000
}

// Imprimir
console.log(carro.preco)

// Deletando propriedades
delete carro.velocidade && carro.velocidade
console.log(carro)

// Atualizando Propriedades
carro.marca = 'Musk'

console.log(carro)


// Array []: são estruturas que permitem armazenar diversos tipos de dados, diferentes ou não. Pode colocar quantos itens quiser, é inifito.
let compras = [
    'x-tudo',
    'video game',
    'churrasco',
    'uninho com escada',
    'sorvete',
    'agua de coco',
    'café',
    'agua gelada',
    'pai de alho',
    'farofa',
    'bebida',
    'pagode',
    'coca gelada',
    true,
    1988
];

// Adicionar um elemento no 'final' do Array -> Array.push(elemento)
compras.push('Jones');

// Adicionar um elemento no 'inicio' do Array -> Array.unshift(elemento)
compras.unshift('Ah la')

// Remover o 'ultimo' elemento do Array -> Array.pop()
compras.pop();

// Remover o 'primeiro' elemento do Array -> Array.shift()
compras.shift()

// Alterando elemento no array, pelo indice --> Array[indice] = novoElemento
compras[0] = 2025;

// Retorna o numero de elementos que existe dentro de um Array -> 
console.log(compras.length)

// Ordenar os elementos de um Array -> Array.sort()
compras.sort((a, b) => a + b);

// Imprimindo Resultado
console.log(compras)