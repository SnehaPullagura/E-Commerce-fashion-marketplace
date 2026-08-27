"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { CompleteTheLookWidget } from "@/components/CompleteTheLookWidget";
import { FashionDNAModal } from "@/components/FashionDNAModal";
import { Star, ShieldCheck, Truck, RotateCcw, Heart, ShoppingBag, Sparkles, Ruler, Check } from "lucide-react";

export default function ProductDetailPage({ params }: { params: { slug: string } }) {
  const [selectedSize, setSelectedSize] = useState("M");
  const [selectedColor, setSelectedColor] = useState("Midnight Black");
  const [addedToCart, setAddedToCart] = useState(false);
  const [addedToWishlist, setAddedToWishlist] = useState(false);
  const [dnaModalOpen, setDnaModalOpen] = useState(false);

  const product = {
    title: "Black Velvet Bodycon Party Dress",
    brand: "Maison Velvet",
    price: 3499,
    mrp: 4999,
    discount: 30,
    rating: 4.9,
    reviews: 38,
    fitType: "SLIM",
    fabric: "Silk Velvet (100% Mulberry Silk base)",
    occasion: "PARTY",
    description: "Sartorially sculpted from rich silk velvet with an asymmetrical neckline and subtle contour panelling. Tailored for high-impact evening and cocktail occasions.",
    images: [
      "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=1000&q=80",
      "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=1000&q=80",
      "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?auto=format&fit=crop&w=1000&q=80"
    ],
    sizes: [
      { label: "XS", inStock: true, chest: "32-34 in" },
      { label: "S", inStock: true, chest: "34-36 in" },
      { label: "M", inStock: true, chest: "36-38 in" },
      { label: "L", inStock: true, chest: "38-40 in" },
      { label: "XL", inStock: false, chest: "40-42 in" }
    ],
    colors: [
      { name: "Midnight Black", hex: "#111111" },
      { name: "Royal Ruby", hex: "#9B111E" },
      { name: "Imperial Emerald", hex: "#046307" }
    ]
  };

  const sampleOutfit = {
    main_product_id: "prod-1",
    main_product_title: product.title,
    outfit_style_theme: "Glamour Party Cocktail Ensemble",
    occasion: "Party",
    bundle_total_mrp: 14997.0,
    bundle_discount_price: 9898.0,
    bundle_savings: 5099.0,
    bundle_discount_percentage: 10.0,
    outfit_items: [
      {
        id: "prod-1",
        title: product.title,
        category_role: "MAIN_PIECE",
        brand_name: product.brand,
        price: product.price,
        mrp: product.mrp,
        image_url: product.images[0],
        fit_type: product.fitType,
        match_reason: "Primary Statement Piece"
      },
      {
        id: "prod-2",
        title: "Gold Polki Drop Earrings",
        category_role: "ACCESSORY",
        brand_name: "Heritage Atelier",
        price: 2499.0,
        mrp: 3999.0,
        image_url: "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=600&q=80",
        fit_type: "REGULAR",
        match_reason: "Antique gold tones harmonize with velvet sheen"
      },
      {
        id: "prod-3",
        title: "Stiletto Velvet Heeled Pumps",
        category_role: "FOOTWEAR",
        brand_name: "Milano Footwear",
        price: 3900.0,
        mrp: 6000.0,
        image_url: "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=600&q=80",
        fit_type: "REGULAR",
        match_reason: "Matching velvet texture elongates silhouette"
      }
    ]
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header
        onOpenFashionDNA={() => setDnaModalOpen(true)}
        cartCount={addedToCart ? 1 : 0}
        wishlistCount={addedToWishlist ? 1 : 0}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12">
        {/* Breadcrumb */}
        <nav className="text-xs text-gray-500 flex items-center gap-2">
          <Link href="/" className="hover:text-black">Home</Link>
          <span>/</span>
          <Link href="/shop" className="hover:text-black">Dresses</Link>
          <span>/</span>
          <span className="text-gray-900 font-medium">{product.title}</span>
        </nav>

        {/* Product Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          {/* Images */}
          <div className="space-y-4">
            <div className="aspect-[3/4] rounded-3xl overflow-hidden bg-gray-100 border border-gray-200">
              <img
                src={product.images[0]}
                alt={product.title}
                className="w-full h-full object-cover object-top"
              />
            </div>
            <div className="grid grid-cols-3 gap-3">
              {product.images.map((img, idx) => (
                <div key={idx} className="aspect-[3/4] rounded-xl overflow-hidden border border-gray-200">
                  <img src={img} alt="Product view" className="w-full h-full object-cover" />
                </div>
              ))}
            </div>
          </div>

          {/* Details */}
          <div className="space-y-6">
            <div>
              <span className="text-xs font-bold uppercase tracking-widest text-brand-700 bg-brand-50 px-2.5 py-1 rounded">
                {product.brand}
              </span>
              <h1 className="font-serif text-3xl font-bold text-gray-950 mt-2">{product.title}</h1>
              
              <div className="flex items-center gap-3 mt-3">
                <div className="flex items-center gap-1 bg-amber-50 px-2 py-0.5 rounded text-xs font-bold text-amber-900 border border-amber-200">
                  <Star size={13} className="fill-amber-500 text-amber-500" />
                  <span>{product.rating}</span>
                </div>
                <span className="text-xs text-gray-500 font-medium">({product.reviews} verified reviews)</span>
                <span className="text-gray-300">|</span>
                <span className="text-xs text-emerald-700 font-bold uppercase">{product.fitType} FIT</span>
              </div>
            </div>

            {/* Price */}
            <div className="flex items-baseline gap-3 pb-6 border-b border-gray-200">
              <span className="text-3xl font-extrabold text-gray-950">₹{product.price.toLocaleString("en-IN")}</span>
              <span className="text-base line-through text-gray-400">₹{product.mrp.toLocaleString("en-IN")}</span>
              <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                {product.discount}% OFF
              </span>
            </div>

            {/* Color Swatches */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">
                Color: <span className="text-gray-900 font-semibold">{selectedColor}</span>
              </label>
              <div className="flex gap-3">
                {product.colors.map((c) => (
                  <button
                    key={c.name}
                    onClick={() => setSelectedColor(c.name)}
                    className={`w-8 h-8 rounded-full border-2 transition ${
                      selectedColor === c.name ? "ring-2 ring-black scale-110 border-white" : "border-gray-300"
                    }`}
                    style={{ backgroundColor: c.hex }}
                    title={c.name}
                  />
                ))}
              </div>
            </div>

            {/* Size Selector */}
            <div>
              <div className="flex items-center justify-between mb-2">
                <label className="text-xs font-bold uppercase tracking-wider text-gray-700">
                  Select Size
                </label>
                <Link href="/size-guide" className="text-xs text-brand-700 hover:underline flex items-center gap-1 font-semibold">
                  <Ruler size={13} /> Size Chart & Advisor
                </Link>
              </div>

              <div className="flex flex-wrap gap-2.5">
                {product.sizes.map((s) => (
                  <button
                    key={s.label}
                    disabled={!s.inStock}
                    onClick={() => setSelectedSize(s.label)}
                    className={`px-4 py-2.5 rounded-xl text-xs font-bold uppercase tracking-wider border transition ${
                      !s.inStock
                        ? "border-gray-200 bg-gray-50 text-gray-300 line-through cursor-not-allowed"
                        : selectedSize === s.label
                        ? "bg-brand-950 border-brand-950 text-white shadow-md scale-105"
                        : "border-gray-200 bg-white text-gray-800 hover:border-gray-400"
                    }`}
                  >
                    {s.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Actions */}
            <div className="flex gap-4 pt-4">
              <button
                onClick={() => setAddedToCart(true)}
                className="flex-1 py-4 bg-brand-950 hover:bg-brand-900 text-white rounded-2xl text-xs font-bold uppercase tracking-widest flex items-center justify-center gap-2 shadow-xl transition active:scale-95"
              >
                {addedToCart ? (
                  <>
                    <Check size={18} className="text-emerald-400" /> Added to Bag
                  </>
                ) : (
                  <>
                    <ShoppingBag size={18} /> Add to Bag
                  </>
                )}
              </button>

              <button
                onClick={() => setAddedToWishlist(!addedToWishlist)}
                className={`p-4 rounded-2xl border transition ${
                  addedToWishlist ? "border-rose-300 bg-rose-50 text-rose-600" : "border-gray-200 text-gray-700 hover:bg-gray-50"
                }`}
              >
                <Heart size={20} className={addedToWishlist ? "fill-rose-600" : ""} />
              </button>
            </div>

            {addedToCart && (
              <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-xs text-emerald-900 font-medium flex items-center justify-between">
                <span>Item added to your shopping bag!</span>
                <Link href="/cart" className="font-bold underline">View Bag</Link>
              </div>
            )}

            {/* Fashion Attributes Card */}
            <div className="bg-stone-50 p-6 rounded-2xl border border-stone-200 space-y-3 text-xs">
              <h3 className="font-bold uppercase tracking-wider text-gray-900">Fashion DNA & Textile Specifications</h3>
              <div className="grid grid-cols-2 gap-2 text-gray-700">
                <div><span className="text-gray-400">Fabric:</span> {product.fabric}</div>
                <div><span className="text-gray-400">Silhouette:</span> Asymmetrical Slip</div>
                <div><span className="text-gray-400">Occasion:</span> Cocktail / Gala</div>
                <div><span className="text-gray-400">Care:</span> Dry Clean Only</div>
              </div>
            </div>
          </div>
        </div>

        {/* Complete the Look Section */}
        <section className="pt-8 border-t border-gray-200">
          <CompleteTheLookWidget
            outfitData={sampleOutfit}
            onAddBundleToCart={() => {
              window.location.href = "/cart";
            }}
          />
        </section>
      </main>

      <FashionDNAModal
        isOpen={dnaModalOpen}
        onClose={() => setDnaModalOpen(false)}
      />

      <Footer />
    </div>
  );
}
