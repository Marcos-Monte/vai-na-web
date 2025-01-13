## OBS

Se eu quiser mexer em uma tag, sempre pedir permissão para o elemento PAI dessa tag
- Exemplo: Se quero mexer no Header, preciso pedir pro Body

## Linkar o arquivo de estilização

o SCSS, é uma versão mais potente do CSS. Por isso devemos linkar o arquivo '.css' que será gerado após clicar na extensão: Watch SASS

- Linkar sempre o arquivo '.css'

## Primeiros passos na Estilização
* Resetar os estilos
* Usando o seletor universal '*'.

## Seletores, Propriedades e Valores

- Sintaxe
Seletor {
    propriedade: valor
}

## Médidas

Vamos ver muito medidas fixas , como: PX, CM, etc

- Para melhor renderização, vamos usar sempre medidas relativas, como: Porcentagem ou Relacionada a página

- Porcentagem: Relacionada a caixa pai:
- Sintaxe
Seletor{
    width: 50%
}

- Exmplicação:
O Seletor vai ter 50% da largura do seu elemento pai


- Referenciando o tamanho da tela:
- Sintaxe
Seletor{
    width: 50vw
    height: 50vh
}

- Exmplicação:
O Seletor vai ter 50% da largura da tela (vw = View Width), assim como 50% da altura da tela (vh = View Height)

### REM e EM
São medidas relativas. Ambos tem a medida default de 16px

* EM: É baseada na medida do elemento Raiz
    - Se não existir estipulação, mantem a medida de 16px
    - Usada também para espaçamentos.
* REM: É baseada na medida do elemento pai
    - Se não existir estipulação, mantem a medida de 16px

- Link de Conversor (de PX para REM): https://nekocalc.com/px-to-rem-converter


### VW e VH
- VW: Viewport Width (Largura)
- VH: Viewport Height (Altura)

Similar a porcentagem.
Mas tem como referencia a tela inteira.

### Estilização de Listas
Propriedade CSS: list-style
- Tem o comportamento similar a estilização direto no HTML.
