function prepare (title, message, date) {
  const toastHtml = document.getElementById('toast')
  document.getElementById('toast-title').textContent = title
  document.getElementById('toast-date').textContent = date
  document.getElementById('toast-message').textContent = message
  const toast = new bootstrap.Toast(toastHtml)
  toast.show()
}

function toast (title, message, date = 'Hace un momento') {
  prepare(title, message, date)
}

function toastSecondary (title, message, date = 'Hace un momento') {
  changeClass(`bg-secondary`)
  prepare(title, message, date)
}

function toastInfo (title, message, date = 'Hace un momento') {
  changeClass(`bg-info`)
  prepare(title, message, date)
}

function toastSuccess (title, message, date = 'Hace un momento') {
  changeClass(`bg-success`)
  prepare(title, message, date)
}

function toastWarning (title, message, date = 'Hace un momento') {
  changeClass(`bg-warning`)
  prepare(title, message, date)
}

function toastError (title, message, date = 'Hace un momento') {
  changeClass(`bg-danger`)
  prepare(title, message, date)
}

function changeClass (className) {
  $('#toast').removeClass('bg-primary bg-secondary bg-info bg-success bg-warning bg-danger').addClass(className)
}
