document.addEventListener('DOMContentLoaded', function() {
  const signupForm = document.getElementById('signupForm');
  const signinForm = document.getElementById('signinForm');

  signupForm.addEventListener('submit', function(event) {
    const nameInput = document.getElementById('name-input');
    const usernameInput = document.getElementById('username-input');
    const passwordInput = document.getElementById('password-input');

    if (!nameInput.value || !usernameInput.value || !passwordInput.value) {
      event.preventDefault();
      alert('請填寫所有欄位');
    }
  });

  signinForm.addEventListener('submit', function(event) {
    const usernameInput = document.getElementById('signin-username-input');
    const passwordInput = document.getElementById('signin-password-input');

    if (!usernameInput.value || !passwordInput.value) {
      event.preventDefault();
      alert('請填寫所有欄位');
    }
  });
});
