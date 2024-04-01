const burgerMenu = document.querySelector('.burger-menu');
const popupMenu = document.querySelector('.popup-menu');

burgerMenu.addEventListener('click', function() {
  burgerMenu.classList.toggle('active');
  popupMenu.classList.toggle('active');
});

const closeIcon = document.querySelector('.close-icon');

closeIcon.addEventListener('click', function() {
  burgerMenu.classList.remove('active');
  popupMenu.classList.remove('active');
});
