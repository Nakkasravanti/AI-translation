// function translateText() {
//     let text = document.getElementById("inputText").value;
//     let targetLang = document.getElementById("languageSelect").value;
    
//     fetch("/translate", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ text: text, target_lang: targetLang })
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById("translatedText").innerText = data.translated_text;
//     });
// }
// function translateText() {
//     let text = document.getElementById("inputText").value;
//     let targetLang = document.getElementById("languageSelect").value;

//     fetch("/translate", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ text: text, target_lang: targetLang })
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById("translatedText").innerText = data.translated_text;
//     })
//     .catch(error => console.error("Error:", error));
// }
function translateText() {
    let text = document.getElementById("inputText").value;
    let targetLang = document.getElementById("languageSelect").value;

    fetch("/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text, target_lang: targetLang })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("translatedText").innerText = data.translated_text;
    })
    .catch(error => console.error("Error:", error));
}
