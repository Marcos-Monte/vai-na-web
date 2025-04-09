// Dicionários

let banco_de_dados = [
    {'id': 1, 'nome': 'Xaropinho', 'cargo': 'Gerente de vendas'},
    {'id': 2, 'nome': 'Naruto Uzumaki', 'cargo': 'Especialista em IA'},
    {'id': 3, 'nome': 'Caroline Mota', 'cargo': 'CTO'},
    {'id': 4, 'nome': 'Alessandra Cotta', 'cargo': 'CEO'}
]

for(let colaborador of banco_de_dados){
    console.log(`Colaborador(a): ${colaborador.nome}`)
}

console.log('***'.repeat(30))

banco_de_dados.map(
    (colaborador) => {
        console.log(`Colaborador(a): ${colaborador.nome}`)
    }
)

console.log('***'.repeat(30))

let i = 0

while( i < banco_de_dados.length){
    console.log(`Colaborador(a): ${banco_de_dados[i].nome}`)
    i++
}