async function sendMood() {
    const mood = document.getElementById("moodInput").value;
    const resultBox = document.getElementById("result");

    if (!mood) {
        resultBox.innerHTML = "請先輸入心情！";
        return;
    }

    try {
        const response = await fetch("http://localhost:8000/mood", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mood })
        });

        const data = await response.json();
        resultBox.innerHTML = "回應：" + data.message;
    } catch (error) {
        resultBox.innerHTML = "無法連接到 API";
    }
}
