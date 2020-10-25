module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
      keyframes:{
        type: {
          '0%': {width: '0%'},
          '100%': {width: '100%'},
        }
      },
      animation:{
        typeanim: 'type 4s steps(60, end)'
      }
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

