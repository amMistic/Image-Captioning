const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const generateBtn = document.getElementById('generateBtn');
const result = document.getElementById('result');
const captionText = document.getElementById('caption');
const errorDiv = document.getElementById('error');

// Drag and drop handlers
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    handleFile(file);
});

dropZone.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFile(file);
});

function handleFile(file) {
    if (file && (file.type === 'image/jpeg' || file.type === 'image/png')) {
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
            generateBtn.disabled = false;
            errorDiv.style.display = 'none';
        };
        reader.readAsDataURL(file);
    } else {
        showError('Please upload a valid JPEG or PNG image.');
    }
}

generateBtn.addEventListener('click', async () => {
    try {
        const formData = new FormData();
        formData.append('image', fileInput.files[0]);

        generateBtn.disabled = true;
        generateBtn.classList.add('loading');
        generateBtn.textContent = 'Generating...';

        const response = await fetch('http://localhost:8000/generate', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to generate caption');
        }

        const data = await response.json();
        result.style.display = 'block';
        captionText.textContent = data.caption;
        errorDiv.style.display = 'none';

    } catch (error) {
        showError('Error generating caption. Please try again.');
    } finally {
        generateBtn.disabled = false;
        generateBtn.classList.remove('loading');
        generateBtn.textContent = 'Generate Caption';
    }
});

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    result.style.display = 'none';
}
