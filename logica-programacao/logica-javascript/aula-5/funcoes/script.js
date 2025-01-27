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
// 1º: Mostrar a mensagem: SEXTOU GALERINHA
function mostrarMensagem(){
    document.getElementById('mensagem1').innerHTML = 'Sextou, Galerinha!'
}

mostrarMensagem()// Ativando (chamando) a função

// 2º: Mostrar a mensagem: Segundou GALERINHA (Usando Parametros)
function mostrarMensagemParametro(texto){
    document.getElementById('mensagem2').innerHTML = texto
}

mostrarMensagemParametro('Segundou, Galerinha!')

// Função Usando Parametros e Argumentos
// Parametros: são valores que a função espera receber ()
// Argumentos: são valores que são passados para a função, preenchendo os marcadores de posição definidos pelos parâmetros ()

// Reservando o espaço pra receber um valor (parametro)
function mostrarFruta(fruta){
    console.log(fruta)
} 

mostrarFruta('Morango') // Argumento preenchendo o espaço do parâmetro

// Com valores pré definidos
function mostrarAnimais(animal1 = 'lobo', animal2 = 'lagarto'){
    console.log(`Animais: ${animal1} e ${animal2}`)
}

mostrarAnimais(animal2 = 'Leão') // Argumento preenchendo o espaço do parâmetro

// Exemplos com operadores matemáticos

// --------Soma
function somar(a, b){
    console.log(`Soma de ${a} e ${b} é ${a + b}`)
}

somar(22, +'7')

// --------Subtração
function subtrair(a, b){
    console.log(`Subtração de ${a} por ${b} é ${a - b}`)
}

subtrair(1, '5')

// --------Multiplicação
function multiplicar(a, b){
    console.log(`Produto de ${a} e ${b} é ${a * b}`)
}

multiplicar(2, 8)

// --------Divisão
function dividir(a, b){
    console.log(`Produto de ${a} e ${b} é ${a / b}`)
}

dividir(0, 8)

// Função Anônima: É uma função que não tem ome, ou seja, voce cria uma função e não dá um nome pra ela.

// Uso de 'const' para declarar a função anonima, é usado para segurança (nada pode alterar a funcionalidade dela)

// --- Ex1
const somarAnonima = function(a, b){
    return a + b // Retornando um valor que será tratado fora da função
}
console.log(`Soma de ${2} e ${2} é ${somarAnonima(2,2)}`)

// --- Ex2
const comprarIngresso = function(nome, idade){
    const resposta = idade >= 18? 
        `${nome} comprou o ingresso`: 
        `${nome} é menor e não pode comprar ingresso`

    return console.log(resposta)
}

comprarIngresso('Marcos', 36)

// --- Ex3: Usando Let
let fazerFeira = function(fruta, legume){
    console.log(fruta, legume)
}

fazerFeira('Uva', 'Brocolis')

fazerFeira = 'redefinido' // A variável que guarda a função foi redefinida e guarda outro valor

console.log(fazerFeira)

// Arrow Function => Função de flecha () => {...}
    // Variavel const: nome da variavel = recebe uma arrow function () => {...}

    
    const nome = (nome) => {
        return nome
    }
    
    console.log(nome('Marcos'))
    
    // Sem usar o 'return': Mais compacto e simples sem a necessidade de utilizar o return ou chaves {}
    const diminuir = (a, b) => a - b;

    console.log(diminuir(2,1))

// Declarando uma arrowFunction dentro de uma outra função

function funcaoPai(){

    // Declarando a ArrowFunction
    const arrow = () => {
        // Retorno da ArrowFunction
        console.log('Oi') 

    }
    // Invocando a ArrowFunction
    arrow()

}

// Invocando a Função
funcaoPai()
