/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#FAF7F5",
          100: "#F5EFEB",
          200: "#E8DCD3",
          300: "#D6C3B4",
          400: "#BD9E87",
          500: "#A57E65",
          600: "#8C634B",
          700: "#6F4B36",
          800: "#553726",
          900: "#3D2417",
          950: "#1A0F0A"
        },
        fashion: {
          black: "#111111",
          gold: "#D4AF37",
          sage: "#8A9A86",
          blush: "#E8C5C8",
          terracotta: "#C86D51"
        }
      },
      fontFamily: {
        serif: ["Playfair Display", "Georgia", "serif"],
        sans: ["Inter", "system-ui", "sans-serif"]
      }
    },
  },
  plugins: [],
};
