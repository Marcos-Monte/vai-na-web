// Estrutura básica de uma função tradicional

// Function: Palavra chave usada para criar a função

// nomeDaFuncao: Esse nome é o nome da função. Geralmente, escolhemos nomes que descreva o que a função faz, como: mostrarMensagem, calcularSoma, mostrarDesenho...

// Parenteses(): É onde colocamos os parametros (ou seja, os valores que a função vai receber)

// chaves {}: Dentro das chaves fica o codigo que a função vai executar

// Sintaxe: function nomeDaFuncao(){ ...código }

function nomeDaFuncao(){
    // Retorno da função
}

nomeDaFuncao() // Ativando (chamando) a função

// ---------- Exemplos ------------
// Mostrar a mensagem: SEXTOU GALERINHA
function mensagem(){
    document.getElementById('mensagem').innerHTML = 'Sextou Galerinha!'
}

mensagem()