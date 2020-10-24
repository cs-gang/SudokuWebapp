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
  variants: {
    backgroundColor: ['responsive', 'focus', 'hover', 'active']
  },
  plugins: [],
  purge: {
    enabled: false,
    content: ['../your-django-folder/path-to-your-templates/**/*.html'],
  },
}

