// QuerySelector:  é um método que captura um elemento no DOM e permite pegar o elemento por: Tag, Class ou ID
document.querySelector('h1').textContent = 'Aula de DOM'

// getElementsByClassName: Modifica um único elemento por vez 
document.getElementsByClassName('subtitulo')[0].innerText = 'QuerySelector: '

document.getElementsByClassName('subtitulo')[1].innerText = 'getElementsByClassName: '

document.getElementsByClassName('subtitulo')[2].innerText = 'querySelectorAll: '

// getElementByID: Pega o elemento raiz através da ID
document.getElementsByClassName('texto')[0].innerText = 'É um método que captura um elemento no DOM e permite pegar o elemento por: Tag, Class ou ID'

document.getElementsByClassName('texto')[1].innerText = 'getElementsByClassName: Modifica um único elemento por vez '

document.getElementsByClassName('texto')[2].innerText = 'querySelectorAll: Pega todoas as "classes" e atribui o valor indicado ao mesmo tempo.'

// Documentação para Propriedades de Utilização do DOM
document.querySelector('a').textContent = 'https://www.w3schools.com/jsref/dom_obj_style.asp'

// querySelectorAll: Pega todoas as 'classes' e atribui o valor indicado ao mesmo tempo.
document.querySelectorAll('.exemplo').forEach(element => {
    element.innerText = 'Exemplo: : '
});