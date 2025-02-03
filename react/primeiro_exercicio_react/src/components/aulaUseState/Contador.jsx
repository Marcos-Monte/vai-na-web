import { useState } from "react";

export default function Contador(){

    const [valor, setValor] = useState(0);

    return(
        <section>
        
            <h2>{valor}</h2>

            <div>
                <button onClick={() => setValor(valor - 1)}> - </button>
                <button onClick={() => setValor(valor + 1)}> + </button>
                <button onClick={() => setValor(0)}> Resetar </button>
            </div>
            
        </section>
    )
}