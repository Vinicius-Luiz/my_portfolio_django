const params = new URLSearchParams(window.location.search);
const parametro = [...params.keys()];
const projectElement = document.getElementById(parametro);
console.log('entrou', projectElement);
const linkElement = document.querySelector(`a[href='#${parametro}']`)
linkElement.addEventListener("click", function (event) {
    event.preventDefault();
    projectElement.scrollIntoView({ behavior: "smooth" });
});
linkElement.click();
// console.log(`Nomes dos parametros: ${parametro}`);