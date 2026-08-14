function openTab(evt, tabName) {
    let i, tabcontent, tablinks;
    
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.add("hidden");
        tabcontent[i].classList.remove("active");
    }
    
    tablinks = document.getElementsByClassName("tab-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    
    document.getElementById(tabName).classList.remove("hidden");
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.className += " active";
}

// TODO: oswaldsly (Silvya) - Implement UI error handling here. Display a red alert card if the API returns a 404 or record not found.
function displayError(elementId, message) {
    const element = document.getElementById(elementId);

    if (!element) {
        return;
    }

    element.classList.remove("hidden");
    element.classList.remove("result-card");
    element.classList.add("error-card");

    element.textContent = message;
}

function displayResult(elementId, data) {
    // Write your code here to show a successful result in the DOM
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchOrderStatus() {
    const orderId = document.getElementById('orderIdInput').value;
    // Write your fetch code here targeting /api/orders/{orderId}
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchReturnStatus() {
    const returnOrderId = document.getElementById('returnOrderIdInput').value;
    // Write your fetch code here targeting /api/returns/{orderId}
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchStock() {
    const sku = document.getElementById('skuInput').value;
    // Write your fetch code here targeting /api/stock/{sku}
}
