window.addEventListener('load', async function() {

    let response = await fetch('http://127.0.0.1:8000/api/recipes/')
    let responseData = await response.json()
    let recipeList = document.getElementById('recipe-list')
    for(recipe of responseData){
        recipeList.innerHTML += `
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <img src="${recipe.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${recipe.title}</h5>
                      <p class="card-text">${recipe.description}</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
        `
    }
        

})