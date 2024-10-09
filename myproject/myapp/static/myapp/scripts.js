document.getElementById('uploadDataTab').onclick = function () {
    window.location.href = '/upload-data/';
};

document.getElementById('queryBuilderTab').onclick = function () {
    window.location.href = '/query-builder/';
};

document.getElementById('usersTab').onclick = function () {
    window.location.href = '/users/';
};

document.getElementById('uploadForm').onsubmit = function (event) {
    event.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const progressBar = document.getElementById('progressBar');
    const progressDiv = document.getElementById('progress');
    progressDiv.style.display = 'block';

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload/', true);

    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            const percentComplete = (event.loaded / event.total) * 100;
            progressBar.value = percentComplete;
        }
    };

    xhr.onload = function () {
        if (xhr.status === 200) {
            alert('File uploaded successfully!');
            progressDiv.style.display = 'none';
        } else {
            alert('Error uploading file.');
        }
    };

    xhr.send(formData);
};
