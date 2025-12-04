async function sendMood(){
    const mood = document.getElementById("mood").value;
    const res = await fetch("/mood", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ mood })
    });
    const data = await res.json();
    document.getElementById("reply").innerText = data.message;
}
