// TODO:
// retain latest in stack-like structure
// litjs

const languageName = {
  javascript: 'JavaScript',
  python: 'Python',
}

const languageAttribute = 'data-language'

const unique = (values) =>
  Array.from(new Set(values).values())

const getLanguageValue = (namedNodeMap) =>
  namedNodeMap.attributes[languageAttribute].nodeValue

const querySelectionArray = (selector) =>
  Array.from(document.querySelectorAll(selector))

const getContentForAllLanguages = () =>
  querySelectionArray(`[${languageAttribute}]`)

const getContentForLanguage = (language) =>
  querySelectionArray(`[${languageAttribute}=${language}]`)

// An array of all languages defined on the page
const getUniqueLanguages = () =>
  unique(getContentForAllLanguages().map(getLanguageValue)).sort()

// Hide content other than the specified language
const switchLanguageTo = (language) => {
  getContentForAllLanguages().forEach(node => node.hidden = true)
  getContentForLanguage(language).forEach(node => node.hidden = false)
}

// When the user changes the prefered language, reflect the change
const handleSwitchLanguage = (event) =>
  switchLanguageTo(event.target.value)

// Populate the language switcher <select> element and bind change callback
window.addEventListener('load', () => {
  const switcher = document.getElementById('language-switcher')
  const languages = getUniqueLanguages()

  languages.forEach(language => {
    const element = document.createElement('option')
    element.setAttribute('value', language)
    element.innerHTML = languageName[language] || language
    switcher.appendChild(element)
  })

  if (languages.length > 0) {
    switcher.style.visibility = 'visible'
    getContentForAllLanguages().forEach(node => node.style.visibility = 'visible')
    switcher.addEventListener('change', handleSwitchLanguage)
    switchLanguageTo(languages[0])
  }
})
