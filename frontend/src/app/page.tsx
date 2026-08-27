"use client";

import React, { useState, useEffect } from "react";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { ProductCard, ProductCardData } from "@/components/ProductCard";
import { CompleteTheLookWidget } from "@/components/CompleteTheLookWidget";
import { FashionDNAModal } from "@/components/FashionDNAModal";
import { Sparkles, ArrowRight, Filter, SlidersHorizontal, Check } from "lucide-react";
import { fetchHomeCatalog, searchCatalog } from "@/lib/api";

const OCCASIONS_LIST = [
  { name: "Wedding Edit", count: "140+ looks", image: "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=600&q=80" },
  { name: "Office Essentials", count: "210+ styles", image: "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?auto=format&fit=crop&w=600&q=80" },
  { name: "Party & Night Out", count: "185+ outfits", image: "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=600&q=80" },
  { name: "Minimalist Streetwear", count: "95+ looks", image: "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?auto=format&fit=crop&w=600&q=80" }
];

export default function HomePage() {
  const [dnaModalOpen, setDnaModalOpen] = useState(false);
  const [selectedGender, setSelectedGender] = useState<string>("ALL");
  const [selectedOccasion, setSelectedOccasion] = useState<string>("ALL");
  const [selectedFit, setSelectedFit] = useState<string>("ALL");

  const [products, setProducts] = useState<ProductCardData[]>([]);
  const [personalizedFeed, setPersonalizedFeed] = useState<ProductCardData[]>([]);
  const [loading, setLoading] = useState(true);

  // Sample dynamic Complete the Look data
  const sampleOutfit = {
    main_product_id: "prod-1",
    main_product_title: "Classic Mandarin Linen Shirt",
    outfit_style_theme: "Minimalist Smart Casual Ensemble",
    occasion: "Office",
    bundle_total_mrp: 11497.0,
    bundle_discount_price: 7468.0,
    bundle_savings: 4029.0,
    bundle_discount_percentage: 10.0,
    outfit_items: [
      {
        id: "prod-1",
        title: "Mandarin Collar Pure Linen Shirt",
        category_role: "MAIN_PIECE",
        brand_name: "Noir Atelier",
        price: 1999.0,
        mrp: 2999.0,
        image_url: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=600&q=80",
        fit_type: "SLIM",
        match_reason: "Breathable pure linen base layer in Off-White"
      },
      {
        id: "prod-2",
        title: "Tailored Chino Trousers",
        category_role: "BOTTOMWEAR",
        brand_name: "Sartorial Men",
        price: 1799.0,
        mrp: 2499.0,
        image_url: "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=600&q=80",
        fit_type: "SLIM",
        match_reason: "Structured cotton chinos in rich Khaki/Olive"
      },
      {
        id: "prod-3",
        title: "Handmade Suede Penny Loafers",
        category_role: "FOOTWEAR",
        brand_name: "Milano Leather",
        price: 3499.0,
        mrp: 4999.0,
        image_url: "https://images.unsplash.com/photo-1533867617858-e7b97e060509?auto=format&fit=crop&w=600&q=80",
        fit_type: "REGULAR",
        match_reason: "Italian suede loafers in Tobacco Brown"
      },
      {
        id: "prod-4",
        title: "Minimalist Leather Chronograph",
        category_role: "ACCESSORY",
        brand_name: "Horology Studio",
        price: 999.0,
        mrp: 1999.0,
        image_url: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=600&q=80",
        fit_type: "ACCESSORY",
        match_reason: "Tan leather strap with sapphire dial"
      }
    ]
  };

  const loadData = async () => {
    setLoading(true);
    try {
      const data = await fetchHomeCatalog();
      if (data.trendingProducts.length > 0) {
        setProducts(data.trendingProducts);
      } else {
        // Fallback curated mock products if backend DB is fresh
        setProducts([
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
            primary_image: "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80",
            fashion_dna_match_score: 98.5
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
            primary_image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
            fashion_dna_match_score: 96.0
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
            primary_image: "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?auto=format&fit=crop&w=800&q=80",
            fashion_dna_match_score: 94.2
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
            primary_image: "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
            fashion_dna_match_score: 97.8
          }
        ]);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header
        onOpenFashionDNA={() => setDnaModalOpen(true)}
        cartCount={1}
        wishlistCount={2}
      />

      <main className="flex-grow">
        {/* 1. Hero Campaign Banner */}
        <section className="relative overflow-hidden bg-brand-950 text-white">
          <div className="absolute inset-0 opacity-40 mix-blend-overlay">
            <img
              src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=2000&q=80"
              alt="Fashion Runway"
              className="w-full h-full object-cover object-center scale-105 animate-pulse"
            />
          </div>
          <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 sm:py-32 flex flex-col items-start justify-center">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-400/20 border border-amber-400/30 text-amber-300 text-xs font-semibold uppercase tracking-widest mb-6 backdrop-blur-md">
              <Sparkles size={14} className="text-amber-400" />
              Fashion Intelligence Platform
            </div>

            <h1 className="font-serif text-4xl sm:text-6xl md:text-7xl font-black tracking-tight text-stone-100 max-w-3xl leading-[1.1]">
              Elevate Your <span className="italic font-normal text-amber-300">Sartorial</span> Persona.
            </h1>

            <p className="text-stone-300 text-sm sm:text-base max-w-xl mt-6 leading-relaxed">
              Curated multi-vendor boutiques, size intelligence, and AI-powered Complete-the-Look outfit discovery tailored to your unique Fashion DNA.
            </p>

            <div className="flex flex-wrap items-center gap-4 mt-8">
              <a
                href="#trending"
                className="px-8 py-4 bg-amber-400 hover:bg-amber-300 text-black font-bold text-xs uppercase tracking-widest rounded-xl shadow-xl transition flex items-center gap-2"
              >
                Explore Curated Looks <ArrowRight size={16} />
              </a>

              <button
                onClick={() => setDnaModalOpen(true)}
                className="px-8 py-4 bg-white/10 hover:bg-white/20 border border-white/30 text-white font-bold text-xs uppercase tracking-widest rounded-xl backdrop-blur-md transition flex items-center gap-2"
              >
                <Sparkles size={16} className="text-amber-400" />
                Customize Fashion DNA
              </button>
            </div>
          </div>
        </section>

        {/* 2. Shop by Occasion Grid */}
        <section id="occasions" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="flex items-center justify-between mb-8">
            <div>
              <div className="text-xs font-bold uppercase tracking-widest text-brand-700">Styling Guidance</div>
              <h2 className="font-serif text-2xl sm:text-3xl font-bold text-gray-950 mt-1">Shop by Occasion</h2>
            </div>
            <a href="#all" className="text-xs font-semibold text-brand-900 hover:underline flex items-center gap-1">
              View All Occasions <ArrowRight size={14} />
            </a>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {OCCASIONS_LIST.map((occ) => (
              <div
                key={occ.name}
                className="group relative rounded-2xl overflow-hidden aspect-[4/5] cursor-pointer shadow-md hover:shadow-xl transition-all"
              >
                <img
                  src={occ.image}
                  alt={occ.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-6">
                  <span className="text-[11px] font-semibold uppercase tracking-wider text-amber-300">
                    {occ.count}
                  </span>
                  <h3 className="font-serif text-xl font-bold text-white mt-1 group-hover:text-amber-200 transition">
                    {occ.name}
                  </h3>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* 3. Complete-the-Look Outfit Engine Widget */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <CompleteTheLookWidget outfitData={sampleOutfit} />
        </section>

        {/* 4. Curated Trending Catalog with Live Filters */}
        <section id="trending" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
            <div>
              <div className="text-xs font-bold uppercase tracking-widest text-brand-700 flex items-center gap-1">
                <Sparkles size={14} className="text-amber-600" />
                Personalized Feed & Catalog
              </div>
              <h2 className="font-serif text-2xl sm:text-3xl font-bold text-gray-950 mt-1">
                Trending Fashion Looks
              </h2>
            </div>

            {/* Quick Filter Buttons */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2 sm:pb-0">
              {["ALL", "WOMEN", "MEN", "SLIM FIT", "OVERSIZED", "ETHNIC"].map((filter) => (
                <button
                  key={filter}
                  onClick={() => setSelectedOccasion(filter)}
                  className={`px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider whitespace-nowrap transition ${
                    selectedOccasion === filter
                      ? "bg-brand-950 text-white shadow-md"
                      : "bg-white border border-gray-200 text-gray-700 hover:bg-gray-50"
                  }`}
                >
                  {filter}
                </button>
              ))}
            </div>
          </div>

          {/* Product Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {products.map((prod) => (
              <ProductCard key={prod.id} product={prod} />
            ))}
          </div>
        </section>
      </main>

      <Footer />

      {/* Fashion DNA Quiz Modal */}
      <FashionDNAModal
        isOpen={dnaModalOpen}
        onClose={() => setDnaModalOpen(false)}
        onSaved={() => loadData()}
      />
    </div>
  );
}
