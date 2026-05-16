const animalSelect = document.getElementById("animal");

async function loadAnimals(){

    const response = await fetch("/animals");
    const data = await response.json();

    animalSelect.innerHTML = "";

    data.animals.forEach(animal => {

        const option = document.createElement("option");

        option.value = animal;
        option.textContent = animal;

        animalSelect.appendChild(option);

    });

}

loadAnimals();

async function predictFood(){

    const animal = document.getElementById("animal").value;
    const weight = document.getElementById("weight").value;
    const height = document.getElementById("height").value;
    const age = document.getElementById("age").value;

    const response = await fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            animal: animal,
            weight: parseFloat(weight),
            height: parseFloat(height),
            age: parseInt(age)
        })

    });

    const data = await response.json();

    const result = document.getElementById("result");

    if(data.error){

        result.innerHTML = data.error;
        result.style.color = "red";

    }
    else{

        result.innerHTML = `Predicted Food Per Day: ${data.prediction} KG`;
        result.style.color = "green";

    }

}
