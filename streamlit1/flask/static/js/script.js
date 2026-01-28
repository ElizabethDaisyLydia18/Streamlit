document.addEventListener('DOMContentLoaded', () => {
	const deleteButtons = document.querySelectorAll('.delete-btn');

	deleteButtons.forEach(button => {
		button.addEventListener('click', event => {
			const targetUrl = button.dataset.deleteUrl;
			if (!targetUrl) return;

			const confirmed = window.confirm('Are you sure you want to delete this student?');
			if (confirmed) {
				window.location.href = targetUrl;
			} else {
				event.preventDefault();
			}
		});
	});
});