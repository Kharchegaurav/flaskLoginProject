document.addEventListener("DOMContentLoaded", function () {
    let registerForm = document.getElementById("registerForm");

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission

            let email = document.getElementById("email").value.trim();
            let password = document.getElementById("password").value.trim();
            let confirmPassword = document.getElementById("confirmPassword").value.trim();
            let message = document.getElementById("message");

            // ✅ Basic Validation
            if (!email || !password || !confirmPassword) {
                message.textContent = "All fields are required!";
                message.style.color = "red";
                return;
            }

            if (password.length < 6) {
                message.textContent = "Password must be at least 6 characters!";
                message.style.color = "red";
                return;
            }

            if (password !== confirmPassword) {
                message.textContent = "Passwords do not match!";
                message.style.color = "red";
                return;
            }

   
            firebase.auth().createUserWithEmailAndPassword(email, password)
                .then((userCredential) => {
                    let user = userCredential.user;
                    message.textContent = "✅ Account created successfully! You can now log in.";
                    
                    message.style.color = "black";

                    // Disable form and button after success
                    registerForm.reset();
                    registerForm.querySelector("button").disabled = true;

                    // Show a login button instead of redirecting
                    setTimeout(() => {
                        message.innerHTML += `<br><a href="/" style="color: blue;">Go to Login</a>`;
                    }, 1000);
                })
                .catch((error) => {
                    message.textContent = "❌ Error: " + error.message;
                    message.style.color = "red";
                });
        });
    }
});
