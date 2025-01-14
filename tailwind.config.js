/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}", // Templates at the project level
    "./**/templates/**/*.html" // Templates inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

