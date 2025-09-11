function getCookie (name) {
  const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"))
  if (match) return match[2]
}

function csrfSafeMethod (method) {
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
}

function setLocalStorage (key, value) {
  localStorage.setItem(key, JSON.stringify(value))
}

function getLocalStorage (key) {
  const storage = localStorage.getItem(key)
  return storage && storage !== 'undefined' ? JSON.parse(storage) : `${key} not found in localSotrage`
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain)
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))

    const token = getLocalStorage("jwt")
    if (token && token.access)
      xhr.setRequestHeader("Authorization", `Bearer ${token.access}`)
  },
});
