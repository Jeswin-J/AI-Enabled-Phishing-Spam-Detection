const generateHTML = (riskScore) => {
    return `
        <div class="container">
            <h1>This Website is Suspicious</h1>
            <p>This Website have high risk Score of ${riskScore}</p>
        </div>
    `;
};

const generateCSS = () => {
    return `
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #ff6347;
        }
    </style>
    `;
};


function checkURL(url) {
    alert (url)
    return new Promise((resolve, reject) => {
        fetch('http://localhost:5000/extn/detect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            resolve({ status: data.status, risk_score: data.risk_score });
        })
        .catch(error => {
            reject(error);
        });
    })
    .then(({ status, risk_score }) => {

        if (status === "Phishing") {
            document.head.innerHTML = generateCSS();
            document.body.innerHTML = generateHTML(risk_score);
        }else if (status === "Suspicious") {
            document.head.innerHTML = generateCSS();
            document.body.innerHTML = generateHTML(risk_score);
        }

    });
}


var currentUrl = window.location.href;
checkURL(currentUrl);

// alert(currentUrl);

// switch (window.location.hostname) {
//     case "github.com":
//         document.head.innerHTML = generateCSS();
//         document.body.innerHTML = generateHTMl("github");
//         break;
//     case "www.youtube.com":
//         alert("good")
//         break;
// }