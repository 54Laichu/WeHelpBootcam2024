window.onload = function () {
  let form = document.querySelector("#signinForm");

  form.addEventListener('submit', function (event) {
    let checkbox = document.querySelector("#checkbox");

    if (!checkbox.checked) {
      window.alert("Please check the checkbox first");
      event.preventDefault()
    }
  });
}
