const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "Admin" && password === "160803") {
        window.location.href = "mainhub.html"; 
    }else if (username === "Vitcc" && password === "123456") {
        window.location.href = "mainhub.html"; 
    } else {
        alert("Invalid Username or Password.");

    }
})