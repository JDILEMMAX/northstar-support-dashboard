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

// TODO: oswaldsly (Silvya) - Implement UI error handling.
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
    const element = document.getElementById(elementId);
    if (!element) return;
    
    element.classList.remove("hidden");
    element.classList.remove("error-card");
    element.classList.add("result-card");
    
    let html = "";
    if (data.order_id && data.status && !data.return_id) {
        html = `<h3>Order: ${data.order_id}</h3>
                <p><strong>Customer:</strong> ${data.customer_name}</p>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Shipping Date:</strong> ${data.shipping_date || 'N/A'}</p>`;
        if (data.tracking_number) {
            html += `<p><strong>Tracking:</strong> ${data.tracking_number}</p>`;
        }
    } else if (data.return_id) {
        html = `<h3>Return: ${data.return_id}</h3>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Reason:</strong> ${data.reason}</p>
                <p><strong>Date:</strong> ${data.return_date || 'N/A'}</p>`;
    } else if (data.product_id) {
        const badge = data.in_stock ? '<span style="color: green;">In Stock</span>' : '<span style="color: red;">Out of Stock</span>';
        html = `<h3>Product: ${data.product_name}</h3>
                <p><strong>Price:</strong> $${data.price}</p>
                <p><strong>Quantity:</strong> ${data.quantity}</p>
                <p><strong>Availability:</strong> ${badge}</p>`;
    }
    element.innerHTML = html;
}

// TODO: peakaykush (Peter) - Write fetch API calls.
async function fetchOrderStatus() {
    const orderId = document.getElementById('orderIdInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/orders/${orderId}`);
        if (!response.ok) {
            throw new Error(`Error ${response.status}`);
        }
        const data = await response.json();
        displayResult('orderResult', data);
    } catch (error) {
        displayError('orderResult', error.message);
    }
}

// TODO: peakaykush (Peter) - Write fetch API calls.
async function fetchReturnStatus() {
    const returnOrderId = document.getElementById('returnOrderIdInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/returns/${returnOrderId}`);
        if (!response.ok) {
            throw new Error(`Error ${response.status}`);
        }
        const data = await response.json();
        displayResult('returnResult', data);
    } catch (error) {
        displayError('returnResult', error.message);
    }
}

// TODO: peakaykush (Peter) - Write fetch API calls.
async function fetchStock() {
    const sku = document.getElementById('skuInput').value;
    try {
        const response = await fetch(`http://localhost:8000/api/stock/${sku}`);
        if (!response.ok) {
            throw new Error(`Error ${response.status}`);
        }
        const data = await response.json();
        displayResult('stockResult', data);
    } catch (error) {
        displayError('stockResult', error.message);
    }
}
