const src = {
    saveText, discardText, closePopup, openPopup, submitForm, deletePhoto, submitPhoto
};

function openPopup() {
    document.getElementById('overlay').style.display = 'block';
    disableFields();
}

function closePopup() {
    document.getElementById('overlay').style.display = 'none';
    activateFields();
}

function saveText() {
    console.log('saveText function called');
    // Get the text from the textarea
    let textValue = document.getElementById('bioValue').value;
    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/changed-bio', true);
    //xhr.open('POST', window.location.pathname, true); // Use the current URL
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Handle successful response if needed
            console.log(xhr.responseText);
            location.reload();
        }
    };
    let data = 'bioValue=' + encodeURIComponent(textValue);
    xhr.send(data);

    closePopup();
}

function discardText() {
    // Close the popup
    closePopup();
}

function submitForm() {
    setTimeout(function () {
        document.getElementById('profile_picture').submit();
    }, 0); // 1000 milliseconds = 1 second
}

function submitPhoto() {
    setTimeout(function () {
        document.getElementById('image_form').submit();
    }, 0); // 1000 milliseconds = 1 second
}

function deletePhoto(photoId, username) {
    window.location.href = "/profile/" + username + "/delete_photo/" + photoId;
    //window.location.href = "{% url 'delete_photo' username=request.user.username photo_id=photoId %}";
}

//imageContainer
function disableFields() {
    let fileInput = document.getElementById('upload-btn-wrapper');
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.disabled = true;
    imageContainer.style.pointerEvents = "none";
    fileInput.disabled = true;
    fileInput.style.pointerEvents = "none";
    imageContainer.classList.add('overlay');

}

function activateFields() {
    let fileInput = document.getElementById('upload-btn-wrapper');
    fileInput.disabled = false;
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.disabled = false;
    fileInput.classList.remove('overlay');
    imageContainer.style.pointerEvents = "auto";
}