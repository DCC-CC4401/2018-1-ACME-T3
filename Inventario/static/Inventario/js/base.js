$(document).ready(function () {
    $('html').show();
    window.setTimeout(function () {
        showAlert();
    }, 100);
});

function showAlert() {
    $("#myAlert").addClass("show");
}