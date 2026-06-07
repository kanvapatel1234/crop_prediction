const form = document.getElementById("cropForm");
const resultBox = document.getElementById("result");
const resultCards = document.querySelectorAll(".result-card");
const secondCard = resultCards[1];

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const data = {
        N: Number(document.getElementById("N").value),
        P: Number(document.getElementById("P").value),
        K: Number(document.getElementById("K").value),
        temperature: Number(document.getElementById("temperature").value),
        humidity: Number(document.getElementById("humidity").value),
        ph: Number(document.getElementById("ph").value),
        rainfall: Number(document.getElementById("rainfall").value)
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        document.getElementById("bestCrop").textContent =
            result.best_crop;

        document.getElementById("bestProb").textContent =
            `${result.best_crop_probability}% confidence`;

        document.getElementById("secondCrop").textContent =
            result.second_crop;

        if (result.second_crop === "Not Recommended" || result.second_crop_probability === null) {

            secondCard.classList.add("hidden");

            document.getElementById("secondCrop").textContent =
                "Not Recommended";

            document.getElementById("secondProb").textContent = "";

        } else {

            secondCard.classList.remove("hidden");

            document.getElementById("secondProb").textContent =
                `${result.second_crop_probability}% confidence`;

        }

        resultBox.classList.remove("hidden");

    }
    catch(error){

        alert("Unable to connect to the API");

        console.error(error);
    }

});