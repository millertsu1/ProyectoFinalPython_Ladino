fetch("../static/libreria/js/productos.json")
  .then((res) => res.json())
  .then((response) => {
    /* console.log(response); */
    response.forEach((product) => {
      const article = document.createRange().createContextualFragment(
        `
    <div class="main-container">
        <div class="main-container container d-flex justify-content-center gap-4 flex-wrap">
            <div class="card bg-dark" style="width: 17rem;">
                <img class="card-img-top" src="${product.img}" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">${product.nombre}</h5>
                    <p class="card-text">${product.descripcion}</p>
                </div>
            </div>
        </div>
    </div>
          `
      );
      const main = document.querySelector("main");

      main.append(article);
    });
  });

  console.log('hola inmundo');