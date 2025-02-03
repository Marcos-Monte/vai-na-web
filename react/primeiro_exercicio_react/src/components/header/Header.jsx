const itens = ['AUTOMÓVEIS', 'VENDAS', 'SERVIÇOS']

// function Header(){
//     return (
//         <header>
//             <ul>
//                 {
//                     itens.map(
//                         (item) => <li>{ item }</li>
//                     )
//                 }
//             </ul>
//         </header>
//     )
// }

const Header = () => {
    return (
        <header>
            <ul>
                {
                    itens.map(
                        (item, index) => <li key={index}>{ item }</li>
                    )
                }
            </ul>
        </header>
    )
}

export default Header;