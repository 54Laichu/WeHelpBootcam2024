window.onload = function() {
  let form = document.querySelector("#signinForm");
  form.onsubmit = function(event) {
    let checkbox = document.querySelector("#checkbox");
    if (!checkbox.checked) {
      event.preventDefault();
      alert("Please check the checkbox first");
    }
  };
};
