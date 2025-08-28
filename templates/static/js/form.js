function form_errors(errors) {
  $.each(errors, function (key, value) {
    const input = $(`#id_${key}`);
    input.addClass("is-invalid");
    input.next().text(value[0].message);
  });
}

// Validar el formulario por parte del cliente
(function () {
  "use strict";
  const form = document.getElementById("form");

  form.addEventListener(
    "submit",
    function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add("was-validated");
    },
    false
  );
})();

