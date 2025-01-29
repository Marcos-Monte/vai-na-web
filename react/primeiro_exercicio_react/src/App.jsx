function App(){

  const titulo = 'Olá. Galerinha!';
  const subtitulo = 'Bom dia!'
  
  // Quando se retorna com (parenteses) significa que quer retornar um HTML
  return (

    // <> ... </> = Fragmento, não ocupa espaço no HTML e envolve os valores.
    // Muito usado no Componente Principal (App)
    <>
      <h1>{ titulo }</h1>
      <h2>{ subtitulo }</h2>
    </>

  )

}

export default App;