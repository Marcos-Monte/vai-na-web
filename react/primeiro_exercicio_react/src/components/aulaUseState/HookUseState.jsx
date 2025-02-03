// Importando a função 'useState' da biblioteca react
// Armazena um valor, que será manipulado posteriormente
import { useState } from "react";

export default function HookState(){

    // Sintaxe (hook useState) -> const [1º valor, 2º valor] = hook useState(valor inicial)
    // cantor é o estado e o setCantor é a forma de modificar o estado
    const [cantor, setCantor] = useState('Zeca Pagodinho');

    // Função de alteração de estado
    const alterarCantor = () => {

        // Condicional ternária
        cantor === 'Zeca Pagodinho'? setCantor('Alcione'): setCantor('Zeca Pagodinho')

    }


    return(
        <>

            <h1>Estado manipulado por useState: {cantor}</h1>
            {/* Eveto de Click que desencadeia na mudança de Estado */}
            <button onClick={alterarCantor}>Mudar Cantor</button>

        </>
    )
}