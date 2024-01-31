const src = {
    saveText, discardText, closePopup, openPopup, submitForm, displayImage
};

function openPopup() {
    document.getElementById('overlay').style.display = 'block';
}

function closePopup() {
    document.getElementById('overlay').style.display = 'none';
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
    }, 1000); // 1000 milliseconds = 1 second
}

function displayImage(input) {
    const container = input.parentElement;
    const file = input.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            container.style.backgroundImage = `url('${e.target.result}')`;
            container.style.backgroundSize = 'cover';
            container.style.backgroundPosition = 'center';
            container.innerHTML = ''; // Clear the text content
            submitForm(); // Automatically submit the form after displaying the image
        };

        reader.readAsDataURL(file);
    }
}