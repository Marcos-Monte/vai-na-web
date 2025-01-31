// Import dos Componentes
import Footer from "./components/footer/Footer";
import Header from './components/header/Header';
import Main from "./components/main/Main";

function App(){

  // Quando se retorna com (parenteses) significa que quer retornar um HTML
  return (

    // <> ... </> = Fragmento, não ocupa espaço no HTML e envolve os valores.
    // Muito usado no Componente Principal (App)
    <>
      {/* Renderizando os Componentes: Header, Main e Footer */}
      <Header />
      <Main />
      <Footer />
    </>

  )

}

export default App;