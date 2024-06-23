import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  resolve: { alias: { "@": "/src" } },
  plugins: [react()],
  server: {
    port: 5173,
    strictPort: true,
    host: true,
    origin: "http://localhost:5173",
  },
});
