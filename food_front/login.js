let form = document.getElementById('login-form')
form.addEventListener('submit', async function(event){
    event.preventDefault()

    let username = document.getElementById('username').value
    let password = document.getElementById('password').value

    let response = await fetch('http://127.0.0.1:8000/auth/token/',
        {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    )

    if (response){
        let resData = await response.json()
        localStorage.setItem('token', resData.access)
    }



})