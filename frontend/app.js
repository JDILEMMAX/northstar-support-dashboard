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
    // Write your code here to show an error message in the DOM
}

function displayResult(elementId, data) {
    // Write your code here to show a successful result in the DOM
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchOrderStatus() {
    const orderId = document.getElementById('orderIdInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/orders/${orderId}`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        displayResult('orderResult', data);
    } catch (error) {
        displayError('orderResult', error.message);
    }
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchReturnStatus() {
    const returnOrderId = document.getElementById('returnOrderIdInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/returns/${returnOrderId}`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        displayResult('returnResult', data);
    } catch (error) {
        displayError('returnResult', error.message);
    }
}

// TODO: peakaykush (Peter) - Write the fetch API call here to connect the UI inputs to the backend routes.
async function fetchStock() {
    const sku = document.getElementById('skuInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/stock/${sku}`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        displayResult('stockResult', data);
    } catch (error) {
        displayError('stockResult', error.message);
    }
}
