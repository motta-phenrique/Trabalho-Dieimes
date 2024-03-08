let index = 0;
const imagens = document.querySelectorAll('.carousel img');

function mostrarImagem() {
    imagens.forEach(img => img.classList.remove('active'));
    imagens[index].classList.add('active');
    index = (index + 1) % imagens.length;
}

setInterval(mostrarImagem, 4000); // Troca de imagem a cada 3 segundos (3000 milissegundos)