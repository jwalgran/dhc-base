(function () {
    if (document.querySelector(".heading-component")) {
        document.querySelector(".heading-component").onclick = function (e) {
            alert("Clicked header with content: " + e.target.innerHTML);
        };
    }
}());
