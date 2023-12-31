/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        dark: "#151520",
      },
    },
  },
  safelist: [
    "border-red-500",
    "border-orange-500",
    "border-yellow-500",
    "border-green-500",
    "border-sky-500",
    "border-violet-500",
    "text-red-500",
    "text-orange-500",
    "text-yellow-500",
    "text-green-500",
    "text-sky-500",
    "text-violet-500",
  ],
  plugins: [],
};
