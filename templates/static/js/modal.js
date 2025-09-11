const modal = document.getElementById('suciModal').firstElementChild;
const btnChangeScreen = document.getElementById('changeScreen');

btnChangeScreen.addEventListener("click", () => {
  if (modal.classList.contains('modal-fullscreen')) {
    minimize (modal);
  } else {
    maximize (modal);
  }
});

function minimize (modal) {
  modal.classList.remove('modal-fullscreen');
  modal.classList.add('modal-dialog-centered');
  btnChangeScreen.classList.add('maximize');
  btnChangeScreen.classList.remove('minimize');
}

function maximize (modal) {
  modal.classList.add('modal-fullscreen');
  modal.classList.remove('modal-dialog-centered');
  btnChangeScreen.classList.remove('maximize');
  btnChangeScreen.classList.add('minimize');
}

minimize (modal);