async function uploadCV(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (response.status === 201) {
        window.location.href = `/confirmation/${result.confirmation_id}`;
    } else {
        alert(result.error);
    }
}