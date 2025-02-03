function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    if (name == "" || email == "" || subject == "" || message == "") {
        alert("All fields are required!");
        return false;
    }
    return true;
}
