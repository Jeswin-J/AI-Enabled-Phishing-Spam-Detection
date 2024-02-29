const generateHTML = (pageName) => {
    return `
        <h1 class="heading">${pageName} Website is not safe</h1>
    `;
};

const generateCSS = () => {
    return `
    <style>
    .heading {
            color: blue;
            font-size: 100px;
            text-align:center
        }
    </style>    
    `;
};


function checkURL(url) {
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
            resolve(data.status);
        })
        .catch(error => {
            reject(error);
        });
    })
    .then(status => {

        if (status === "Phishing") {
            document.head.innerHTML = generateCSS();
            document.body.innerHTML = generateHTML("github");
        }else if (status === "Suspicious") {
            document.head.innerHTML = generateCSS();
            document.body.innerHTML = generateHTML("github");
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