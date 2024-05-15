document.addEventListener('DOMContentLoaded', function() {
  const signupForm = document.querySelector('#signupForm');
  const signinForm = document.querySelector('#signinForm');

  signupForm.addEventListener('submit', function(event) {
    const nameInput = document.querySelector('#name-input');
    const usernameInput = document.querySelector('#username-input');
    const passwordInput = document.querySelector('#password-input');

    if (!nameInput.value || !usernameInput.value || !passwordInput.value) {
      event.preventDefault();
      alert('請填寫所有欄位');
    }
  });

  signinForm.addEventListener('submit', function(event) {
    const usernameInput = document.querySelector('#signin-username-input');
    const passwordInput = document.querySelector('#signin-password-input');

    if (!usernameInput.value || !passwordInput.value) {
      event.preventDefault();
      alert('請填寫所有欄位');
    }
  });
});
