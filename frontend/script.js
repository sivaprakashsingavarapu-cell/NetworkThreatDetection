async function predictThreat() {

    document.getElementById("result").innerText =
        "Predicting...";

    const data = {
        "Init Fwd Win Bytes": Number(document.getElementById("Init Fwd Win Bytes").value),
        "Bwd Packet Length Mean": Number(document.getElementById("Bwd Packet Length Mean").value),
        "Bwd Packet Length Std": Number(document.getElementById("Bwd Packet Length Std").value),
        "Fwd IAT Mean": Number(document.getElementById("Fwd IAT Mean").value),
        "Flow IAT Max": Number(document.getElementById("Flow IAT Max").value),
        "Flow IAT Mean": Number(document.getElementById("Flow IAT Mean").value),
        "Bwd Packets/s": Number(document.getElementById("Bwd Packets/s").value),
        "Avg Bwd Segment Size": Number(document.getElementById("Avg Bwd Segment Size").value),
        "Bwd Header Length": Number(document.getElementById("Bwd Header Length").value),
        "Fwd Packet Length Max": Number(document.getElementById("Fwd Packet Length Max").value),
        "Fwd IAT Max": Number(document.getElementById("Fwd IAT Max").value),
        "Init Bwd Win Bytes": Number(document.getElementById("Init Bwd Win Bytes").value),
        "Packet Length Variance": Number(document.getElementById("Packet Length Variance").value),
        "Fwd IAT Min": Number(document.getElementById("Fwd IAT Min").value),
        "Fwd IAT Total": Number(document.getElementById("Fwd IAT Total").value),
        "Flow Packets/s": Number(document.getElementById("Flow Packets/s").value),
        "PSH Flag Count": Number(document.getElementById("PSH Flag Count").value),
        "Fwd Header Length": Number(document.getElementById("Fwd Header Length").value),
        "Bwd Packets Length Total": Number(document.getElementById("Bwd Packets Length Total").value),
        "Bwd Packet Length Max": Number(document.getElementById("Bwd Packet Length Max").value)
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        const resultBox = document.getElementById("result");

if (result.prediction === "Benign") {

    resultBox.innerText = "🟢 BENIGN TRAFFIC";

} else {

    resultBox.innerText =
        "🔴 THREAT DETECTED: " + result.prediction;
}
loadHistory();
loadStats();

    } catch (error) {

        document.getElementById("result").innerText =
            "Error connecting to Flask server.";

        console.error(error);
    }
}
async function loadHistory() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predictions"
        );

        const predictions = await response.json();

        const historyBody =
            document.getElementById("historyBody");

        historyBody.innerHTML = "";

        predictions.forEach(function(item) {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${item.id}</td>
                <td>${item.prediction}</td>
                <td>${item.created_at}</td>
            `;

            historyBody.appendChild(row);

        });

    } catch (error) {

        console.error(error);

    }
}
async function loadStats() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/stats"
        );

        const stats = await response.json();

        document.getElementById("totalPredictions").innerText =
            stats.total;

        document.getElementById("benignPredictions").innerText =
            stats.benign;

        document.getElementById("threatPredictions").innerText =
            stats.threats;

            let threatRate = 0;

if (stats.total > 0) {
    threatRate = (stats.threats / stats.total) * 100;
}

document.getElementById("threatRate").innerText =
    threatRate.toFixed(1) + "%";
    

    } catch (error) {

        console.error("Error loading statistics:", error);

    }
}
function resetInputs() {

    const inputs = document.querySelectorAll(
        ".input-grid input"
    );

    inputs.forEach(function(input) {
        input.value = 0;
    });

    document.getElementById("result").innerText =
        "Prediction will appear here";
}
async function checkSystemStatus() {

    const statusText = document.querySelector(".system-status span:last-child");
    const statusDot = document.querySelector(".status-dot");

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/health"
        );

        const data = await response.json();

        if (data.status === "online") {

            statusText.innerText = "System Online";
            statusDot.style.backgroundColor = "#2e7d32";

        }

    } catch (error) {

        statusText.innerText = "System Offline";
        statusDot.style.backgroundColor = "#d32f2f";

    }
}
async function clearHistory() {

    const confirmClear = confirm(
        "Are you sure you want to clear prediction history?"
    );

    if (!confirmClear) {
        return;
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/clear-history",
            {
                method: "DELETE"
            }
        );

        const result = await response.json();

        alert(result.message);

        loadHistory();
        loadStats();

    } catch (error) {

        alert("Error clearing history.");
        console.error(error);

    }
}
loadHistory();
loadStats();
checkSystemStatus();
document.getElementById("lastUpdated").innerText =
        "Last updated: " + new Date().toLocaleTimeString();

setInterval(function() {

    loadHistory();
    loadStats();
    checkSystemStatus();

    document.getElementById("lastUpdated").innerText =
        "Last updated: " + new Date().toLocaleTimeString();

}, 10000);

async function refreshDashboard() {

    await loadHistory();
    await loadStats();
    await checkSystemStatus();

    document.getElementById("lastUpdated").innerText =
        "Last updated: " + new Date().toLocaleTimeString();
}