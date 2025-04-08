const form = document.getElementById("FL");
const resultado = document.getElementById("resultado");

const nome = document.getElementById("nome");
const senha = document.getElementById("senha"); // <-- agora com "s" minúsculo

form.addEventListener("submit", function(event) {
  event.preventDefault(); // Evita que a página recarregue

  resultado.innerHTML = `
    <h2>Dados Recebidos:</h2>
    <p><strong>Usuário:</strong> ${nome.value}</p>
    <p><strong>Senha:</strong> ${senha.value}</p>
  `;
});
