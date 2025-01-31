const imagens = [
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965324.png"},
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965410.png"},
    {img: "https://cdn-icons-png.flaticon.com/256/5965/5965331.png"},
]

function Main() {
    return (
        <main>
            <section>
                {
                    imagens.map(
                        (imagem) => <img src={imagem.img}/>
                    )
                }
            </section>
        </main>
    )
}

export default Main;