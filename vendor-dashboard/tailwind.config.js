/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#FAF7F5",
          100: "#F5EFEB",
          500: "#A57E65",
          900: "#3D2417",
          950: "#1A0F0A"
        }
      }
    },
  },
  plugins: [],
}
