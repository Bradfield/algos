window.addEventListener('load', () => {
  Array.from(document.getElementsByClassName('concealed')).forEach(section => {
    section.addEventListener('click', event => event.target.className = '')
  })
})
