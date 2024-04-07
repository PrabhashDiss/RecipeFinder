async function fetchData(url) {
  const response = await fetch(url);
  return await response.json();
}

function displayRecipes(recipes) {
  // Display the received recipes on the UI
}

async function findRecipes() {
  const userInput = document.getElementById("userInput").value;
  const url = "/api/recipes?preferences=" + userInput;
  const recipes = await fetchData(url);
  displayRecipes(recipes);
}