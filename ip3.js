function validate() {
    let x1 = document.forms["myform"]["fname"].value;
    if (x1 === "") {
        alert("Please enter your first name");
        return false;
    }

    let x2 = document.forms["myform"]["mname"].value;
    if (x2 === "") {
        alert("Please enter your middle name");
        return false;
    }

    let x3 = document.forms["myform"]["lname"].value;
    if (x3 === "") {
        alert("Please enter your last name");
        return false;
    }

    let phone = document.forms["myform"]["number"].value;
    if (phone === "") {
        alert("Please enter your phone number");
        return false;
    }
    if (!/^\d{10}$/.test(phone)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }

    let username = document.forms["myform"]["username"].value;
    if (username === "") {
        alert("Please choose a username");
        return false;
    }
    
    if (!/^[a-zA-Z0-9]+$/.test(username)) {
        alert("Username can only contain letters and numbers");
        return false;
    }

    let x4 = document.forms["myform"]["pass"].value;
    if (x4 === "") {
        alert("Please enter the password");
        return false;
    }
    if (x4.length > 15) {
        alert("Password must not exceed 15 characters");
        return false;
    }
    if (x4.length < 8) {
        alert("Password must be at least 8 characters");
        return false;
    }
    
}
