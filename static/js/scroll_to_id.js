const params = new URLSearchParams(window.location.search);
const parametro = [...params.keys()];
const projectElement = document.getElementById(parametro);
const linkElement = document.querySelector(`a[href='#${parametro}']`)
linkElement.addEventListener("click", function (event) {
    event.preventDefault();
    projectElement.scrollIntoView({ behavior: "smooth" });
});
linkElement.click();
// console.log(`Nomes dos parametros: ${parametro}`);