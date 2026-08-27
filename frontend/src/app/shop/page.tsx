"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { ProductCard } from "@/components/ProductCard";
import { SlidersHorizontal, ArrowLeft } from "lucide-react";

export default function ShopPage() {
  const [selectedOccasion, setSelectedOccasion] = useState("ALL");
  const [selectedFit, setSelectedFit] = useState("ALL");

  const products = [
    {
      id: "1",
      title: "Black Velvet Bodycon Party Dress",
      slug: "black-velvet-bodycon-party-dress",
      brand_name: "Maison Velvet",
      base_price: 3499,
      base_mrp: 4999,
      discount_percentage: 30,
      fit_type: "SLIM",
      occasion: "PARTY",
      fabric: "Silk Velvet",
      average_rating: 4.9,
      review_count: 38,
      primary_image: "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80"
    },
    {
      id: "2",
      title: "Mandarin Collar Pure Organic Linen Shirt",
      slug: "minimalist-linen-mandarin-shirt",
      brand_name: "Noir Atelier",
      base_price: 1999,
      base_mrp: 2999,
      discount_percentage: 33,
      fit_type: "SLIM",
      occasion: "OFFICE",
      fabric: "100% Linen",
      average_rating: 4.8,
      review_count: 54,
      primary_image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80"
    },
    {
      id: "3",
      title: "Oversized Heavyweight Graphic Streetwear Tee",
      slug: "oversized-graphic-tee",
      brand_name: "Tokyo Raw",
      base_price: 1299,
      base_mrp: 1999,
      discount_percentage: 35,
      fit_type: "OVERSIZED",
      occasion: "STREETWEAR",
      fabric: "280 GSM Cotton",
      average_rating: 4.7,
      review_count: 82,
      primary_image: "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?auto=format&fit=crop&w=800&q=80"
    },
    {
      id: "4",
      title: "Handcrafted Zari Embroidered Silk Kurta Set",
      slug: "silk-kurta-set",
      brand_name: "Anita Dongre",
      base_price: 7999,
      base_mrp: 11999,
      discount_percentage: 33,
      fit_type: "REGULAR",
      occasion: "WEDDING",
      fabric: "Mulberry Silk",
      average_rating: 5.0,
      review_count: 24,
      primary_image: "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80"
    }
  ];

  const filtered = products.filter((p) => {
    if (selectedOccasion !== "ALL" && p.occasion !== selectedOccasion) return false;
    if (selectedFit !== "ALL" && p.fit_type !== selectedFit) return false;
    return true;
  });

  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="flex items-center justify-between border-b border-gray-200 pb-6 mb-8">
          <div>
            <h1 className="font-serif text-3xl font-bold text-gray-950">Curated Designer Collection</h1>
            <p className="text-xs text-gray-500 mt-1">Discover designer pieces filtered by fashion attributes and occasions.</p>
          </div>
          <Link href="/" className="text-xs font-bold uppercase tracking-wider text-brand-900 flex items-center gap-1">
            <ArrowLeft size={14} /> Back to Runway
          </Link>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          {/* Filters */}
          <aside className="space-y-6">
            <div className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
              <div>
                <h3 className="text-xs font-bold uppercase tracking-wider text-gray-900 mb-3">Occasion</h3>
                <div className="space-y-2 text-xs font-medium text-gray-700">
                  {["ALL", "OFFICE", "PARTY", "WEDDING", "STREETWEAR"].map((occ) => (
                    <label key={occ} className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="radio"
                        name="occasion"
                        checked={selectedOccasion === occ}
                        onChange={() => setSelectedOccasion(occ)}
                        className="text-brand-950"
                      />
                      <span>{occ}</span>
                    </label>
                  ))}
                </div>
              </div>

              <div className="border-t border-gray-100 pt-6">
                <h3 className="text-xs font-bold uppercase tracking-wider text-gray-900 mb-3">Fit Profile</h3>
                <div className="space-y-2 text-xs font-medium text-gray-700">
                  {["ALL", "SLIM", "REGULAR", "OVERSIZED"].map((fit) => (
                    <label key={fit} className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="radio"
                        name="fit"
                        checked={selectedFit === fit}
                        onChange={() => setSelectedFit(fit)}
                        className="text-brand-950"
                      />
                      <span>{fit} FIT</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>
          </aside>

          {/* Grid */}
          <div className="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {filtered.map((p) => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}
