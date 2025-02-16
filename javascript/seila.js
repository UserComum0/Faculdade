const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let valorTemporario; // Variável global

rl.question("Digite um valor temporário: ", (input) => {
  valorTemporario = input; // Atribui o valor digitado à variável
  console.log("Valor armazenado na sessão do programa:", valorTemporario);
  
  // Chama outra função ou faz algo com `valorTemporario`
  fazerAlgoComValor(valorTemporario);

  rl.close(); // Fecha o readline após o uso
});