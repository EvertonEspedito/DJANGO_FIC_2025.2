// Menu Flutuante via clique no menu mobile
// comportamento: abrir/fechar apenas ao clicar no botão; ao clicar em uma opção, fecha.

const menuMobile = document.querySelector('.menu-mobile');
const menuFlutuante = document.querySelector('.menu-flutuante');

if (menuMobile) {
    menuMobile.addEventListener('click', () => {
        if (!menuFlutuante) return;
        menuFlutuante.classList.toggle('visivel');
        menuMobile.classList.toggle('ativo');
    });
}

// fecha o menu quando o usuário clica em um link dentro do menu flutuante
if (menuFlutuante) {
    menuFlutuante.addEventListener('click', (event) => {
        const link = event.target.closest('a');
        if (link) {
            menuFlutuante.classList.remove('visivel');
            if (menuMobile) menuMobile.classList.remove('ativo');
        }
    });
}