module.exports = {
  content: ['../mainapp/templates/mainapp/*.html'],
  css: ['../mainapp/static/mainapp/tailwind-output.css'],
  defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
}