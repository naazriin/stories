window.addEventListener('load', async function() {
    let resCats = await fetch('http://127.0.0.1:8000/api/cats/')
    let resCatsData = await resCats.json()
    let catList = document.getElementById('cat-list')
    for(cat of resCatsData){
        catList.innerHTML += `
        <option value="${cat.id}">${cat.name}</option>
        `
    }

    let resTags= await fetch('http://127.0.0.1:8000/api/tags/')
    let resTagsData = await resTags.json()
    let tagList = document.getElementById('tag-list')
    for(tag of resTagsData){
        tagList.innerHTML += `
        <option value="${tag.id}">${tag.name}</option>
        `
    }
            
})


let accessToken = localStorage.getItem('token')
let form = document.getElementById('create-form')
form.addEventListener('submit', async function(event){
    event.preventDefault()
    let newForm = new FormData(form)
    await fetch('http://127.0.0.1:8000/api/recipes/',
        {
            method: 'POST',
            body: newForm,
            headers:{
                'Authorization': `Bearer ${accessToken}`
            }
        }
    )

})