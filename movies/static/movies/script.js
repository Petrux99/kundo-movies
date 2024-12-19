let resultArea

document.addEventListener("DOMContentLoaded", function(event) {
  const searchField = document.querySelector('#search-field')
  searchField.addEventListener('input', _.debounce(async ({ target: { value } }) => {
    presentResults(value.trim().length ? await (await fetch(`/api/search/${value}`)).json() : [])
  }, 200))
  searchField.focus()

  resultArea = document.querySelector('#results')
});

function renderResult({ Title, Year, Poster, imdbID }) {
  const container = document.createElement('a')
  container.className = 'result'
  container.href = `/details/${imdbID}`
  container.innerHTML += `<h2>${Title} <span class="year">${Year}</span></h2>`
  if (Poster !== 'N/A') {
    container.innerHTML += `<img src="${Poster} alt="Movie poster" />`
  } else {
    container.innerHTML += '<div class="poster-placeholder"></div>'
  }
  return container
}

function presentResults(results) {
  const list = new DocumentFragment()
  results.forEach(result => list.append(renderResult(result)))
  resultArea.innerHTML = ''
  resultArea?.append(list)
}
