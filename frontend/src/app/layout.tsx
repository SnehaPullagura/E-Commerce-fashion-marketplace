import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Atelier — Multi-Vendor Fashion Marketplace & Intelligence",
  description: "Discover curated designer looks, smart size recommendations, occasion styling and Complete-the-Look outfit engines.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased selection:bg-brand-900 selection:text-white">
        {children}
      </body>
    </html>
  );
}
