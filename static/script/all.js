$(document).ready(function() {
    // Show hide password
    function showPassword() {
        $("#showPassword").change(function() {
            if(this.checked) {
                document.getElementById("password").type="text"; 
                document.getElementById("c_password").type="text"; 
            }
            else {
                document.getElementById("password").type="password"; 
                document.getElementById("c_password").type="password";
            }
        });
    }
    showPassword()
})
