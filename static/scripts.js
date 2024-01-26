
const src= {
    saveText, discardText, closePopup, openPopup
};
    function openPopup()
{
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
    // Clear the text in the textarea
    document.getElementById('bioValue').value = '';

    // Close the popup
    closePopup();
}
