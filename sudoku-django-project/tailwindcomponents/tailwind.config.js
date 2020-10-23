module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
    },
  },
  variants: {},
  plugins: [],
  purge: {
    enabled: true,
    content: ['../your-django-folder/path-to-your-templates/**/*.html'],
  },
}

