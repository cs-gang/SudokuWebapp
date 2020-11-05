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
        },
        falling:{
          '0%':{
              transform: "translateY(-315px);",
              'animation-timing-function': 'ease-in;'
          },
          '15%':{
              transform: 'translateY(0);',
              'animation-timing-function': 'ease-out;'
          },
          '19%':{
              transform: 'translateY(-30px);',
              'animation-timing-function': 'ease-in;'
          },
          '26%':{
              transform: 'translateY(0);'
          }
        }
      },
      animation:{
        typeanim: 'type 4s steps(100, end)',
        fall: 'falling 3s linear'
      },
      spacing: {
        'rem18': '18rem',
        'rem20': '20rem',
        'rem21': '21rem',
      },
      fontSize: {
        '7xl':'5rem',
        '8xl':'6rem',
        '9xl':'7rem',
        '10xl':'8rem',
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

