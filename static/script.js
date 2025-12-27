function convert() {
    const appstate = document.getElementById("appstate").value;

    fetch("/convert", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ appstate })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerHTML =
                "<span style='color:red'>" + data.error + "</span>";
        } else {
            document.getElementById("result").innerHTML =
                "<b>Token:</b><br>" + data.token;
        }
    });
}
