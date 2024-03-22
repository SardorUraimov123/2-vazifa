// Static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');

    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        const preview = document.querySelector('.image-preview');

        if (file) {
            const reader = new FileReader();

            reader.addEventListener('load', function() {
                preview.innerHTML = `<img src="${reader.result}" alt="Preview Image" style="max-width: 100%;">`;
            });

            reader.readAsDataURL(file);
        } else {
            preview.innerHTML = '';
        }
    });

    const videoInput = document.querySelector('input[type="file"]');

    videoInput.addEventListener('change', function() {
        const file = this.files[0];
        const preview = document.querySelector('.video-preview');

        if (file) {
            const reader = new FileReader();

            reader.addEventListener('load', function() {
                preview.innerHTML = `<video width="400" controls><source src="${reader.result}" type="video/mp4">Your browser does not support the video tag.</video>`;
            });

            reader.readAsDataURL(file);
        } else {
            preview.innerHTML = '';
        }
    });
});
