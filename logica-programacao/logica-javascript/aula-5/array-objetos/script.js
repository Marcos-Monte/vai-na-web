document.getElementById('nome').innerText = 'Marcos'
document.getElementById('nome').style.backgroundColor = 'red'

// Array de Objetos [{}, {}, {}...]
// Exemplo 1 - Estilos Musicais

// Cada 'bolsa / objeto' tem seu índice
// let estilosMusicais = [
//     { 
//         estilo:'rock', 
//         surgiu: 1950, 
//         cantores: ['Chorão', 'Rita Lee']
//     },
//     { 
//         estilo:'mpb', 
//         surgiu: 1960, 
//         cantores: ['Elis Regina', 'Caetano Veloso']
//     },
//     { 
//         estilo:'pagode', 
//         surgiu: 1970, 
//         cantores: ['Péricles', 'Thiaguinho']
//     },
    
// ]

// console.log(typeof estilosMusicais) // Mostra o tipo da variavel

// console.log(estilosMusicais) // Mostrou toda as colbsas que estão guardadas no array. Indices: 0 = rock, 1 = mpb, 2 = pagode

// console.log(estilosMusicais[0]) // Mostra o que tem no indice indicado

// console.log(estilosMusicais[1].estilo) // Mostra uma propriedade do Objeto selecionado pelo Indice

// console.log(estilosMusicais[2].cantores[0]) // Mostra 

// console.log('Estilos Musicais')
// // Percorre a lista de Objetos
// for(let tipo in estilosMusicais){
//     // Mostra na tela a propriedade 'estilo' de cada Objeto
//     console.log(`Estilo Musical: ${estilosMusicais[tipo].estilo}`)

// }

//---------------------------------------------------------------

// Exemplo 2 - A senhora da feira

let carrinho = [
    {
        barraca: 'peixes',
        vendedor: 'João', 
        produtos: ['sardinha', 'corvina'] 
    },
    {
        barraca: 'temperos',
        vendedor: 'Maria', 
        produtos: { produto1: 'paprica', produto2: 'cominho' }
    },
    {
        barraca: 'legumes',
        vendedor: 'José', 
        produtos: ['cenoura', 'abobora'] 
    },
]

console.log(carrinho) // Mostra as 3 'bolsas' que tem no carrinho

console.log(carrinho[1].produtos.produto2) // Entra na bolsa de indice [1], acesse a bolsinha produtos, pegue o produto2 = cominho

console.log(carrinho[2].vendedor) // Mostra o nome do vendedor da barraca de indice 2 = José

