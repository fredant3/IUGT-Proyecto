function displayFileName(input) {
	const files = input.files;
	const fileNames = Array.from(files).map(file => file.name).join(', ');
	input.dataset.text = fileNames;
}

const checkboxes = document.querySelectorAll('.input__checkbox');
checkboxes.forEach(checkbox => {
	checkbox.parentNode.parentElement.classList.add('input--checkbox')
})
