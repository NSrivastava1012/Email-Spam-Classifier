
// Mock data for demonstration purposes
const weatherData = {
    temperature: "22°C",
    condition: "Sunny",
    humidity: "45%",
    windSpeed: "10 km/h"
};

const governmentSchemesData = [
    {
        name: "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        description: "Provides income support to small and marginal farmers.",
        eligibility: "Small and marginal farmers with less than 2 hectares of land.",
        benefits: "Direct cash transfer of ₹6,000 per year."
    }
];

const cropData = [
    { name: "Tomato", status: "Growing well, expected harvest in 2 weeks" },
    { name: "Corn", status: "Healthy, monitoring for pests" },
    { name: "Carrot", status: "Maturing, water level ideal" }
];

// Function to populate weather data
function displayWeather() {
    const weatherSection = document.getElementById("weather-details");
    weatherSection.innerHTML = `
        <p><strong>Temperature:</strong> ${weatherData.temperature}</p>
        <p><strong>Condition:</strong> ${weatherData.condition}</p>
        <p><strong>Humidity:</strong> ${weatherData.humidity}</p>
        <p><strong>Wind Speed:</strong> ${weatherData.windSpeed}</p>
    `;
}

displayWeather();

// Function to populate government schemes data
function displayGovernmentSchemes() {
    const schemesSection = document.getElementById("government-schemes-details");
    schemesSection.innerHTML = governmentSchemesData.map(scheme => `
        <div>
            <h3><strong>${scheme.name}</strong></h3>
            <p><strong>Description:</strong> ${scheme.description}</p>
            <p><strong>Eligibility:</strong> ${scheme.eligibility}</p>
            <p><strong>Benefits:</strong> ${scheme.benefits}</p>
        </div>
    `).join("");
}

// Call this function to display the data when needed
displayGovernmentSchemes();

// Function to populate crop data
function displayCrops() {
    const cropSection = document.getElementById("crop-details");
    cropSection.innerHTML = cropData.map(crop => `
        <p><strong>${crop.name}:</strong> ${crop.status}</p>
    `).join("");
}

displayCrops();

// Load the data when the page loads
window.onload = function() {
    displayWeather();
    displaySoil();
    displayCrops();
};