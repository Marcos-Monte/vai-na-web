const imagens = [
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965324.png"},
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965410.png"},
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965331.png"},
]

function Main({exemploUseState1, exemploUseState2}) {
    return (
        <main>
            <section>
                {
                    imagens.map(
                        (imagem, index) => <img src={imagem.img} key={index}/>
                    )
                }
            </section>
            <section>
                {exemploUseState1}
                {exemploUseState2}
            </section>
        </main>
    )
}

export default Main;