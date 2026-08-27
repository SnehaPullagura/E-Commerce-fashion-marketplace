"use client";

import React from "react";
import Link from "next/link";
import { Heart, Star, Sparkles, ShoppingBag } from "lucide-react";

export interface ProductCardData {
  id: string;
  title: string;
  slug: string;
  brand_name?: string;
  base_price: number;
  base_mrp: number;
  discount_percentage: number;
  primary_image?: string;
  fit_type?: string;
  occasion?: string;
  fabric?: string;
  average_rating?: number;
  review_count?: number;
  colors?: string[];
  sizes?: string[];
  fashion_dna_match_score?: number;
}

interface ProductCardProps {
  product: ProductCardData;
  onQuickView?: (product: ProductCardData) => void;
  onAddToCart?: (product: ProductCardData) => void;
}

export const ProductCard: React.FC<ProductCardProps> = ({
  product,
  onQuickView,
  onAddToCart
}) => {
  const fallbackImg = "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80";
  const displayImg = product.primary_image || fallbackImg;

  return (
    <div className="group relative flex flex-col bg-white rounded-xl overflow-hidden border border-gray-100 hover:shadow-xl transition-all duration-300">
      {/* Image Container with Badges */}
      <div className="relative aspect-[3/4] w-full bg-gray-50 overflow-hidden">
        <Link href={`/products/${product.slug || product.id}`}>
          <img
            src={displayImg}
            alt={product.title}
            className="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500"
            loading="lazy"
          />
        </Link>

        {/* Fashion DNA Match Badge if present */}
        {product.fashion_dna_match_score && (
          <div className="absolute top-2.5 left-2.5 bg-brand-950/90 backdrop-blur-sm text-amber-300 text-[10px] font-bold tracking-wide px-2.5 py-1 rounded-full flex items-center gap-1 shadow-md">
            <Sparkles size={11} className="text-amber-400" />
            <span>{product.fashion_dna_match_score}% DNA Match</span>
          </div>
        )}

        {/* Occasion Badge */}
        {product.occasion && !product.fashion_dna_match_score && (
          <div className="absolute top-2.5 left-2.5 bg-white/90 backdrop-blur-sm text-gray-800 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded shadow-sm">
            {product.occasion}
          </div>
        )}

        {/* Wishlist Button */}
        <button
          className="absolute top-2.5 right-2.5 w-8 h-8 rounded-full bg-white/80 backdrop-blur-sm flex items-center justify-center text-gray-600 hover:text-rose-500 hover:bg-white shadow-sm transition"
          title="Add to Wishlist"
        >
          <Heart size={16} />
        </button>

        {/* Quick Add Overlay */}
        <div className="absolute inset-x-0 bottom-0 p-3 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex justify-center">
          <button
            onClick={() => onAddToCart && onAddToCart(product)}
            className="w-full py-2 bg-white text-black font-semibold text-xs rounded-lg hover:bg-brand-950 hover:text-white transition flex items-center justify-center gap-1.5 shadow-lg"
          >
            <ShoppingBag size={14} />
            Quick Add
          </button>
        </div>
      </div>

      {/* Product Information */}
      <div className="p-4 flex flex-col flex-grow">
        {/* Brand & Rating */}
        <div className="flex items-center justify-between text-xs text-gray-500 mb-1">
          <span className="font-semibold uppercase tracking-wider text-brand-700">
            {product.brand_name || "Atelier Atelier"}
          </span>
          {product.average_rating ? (
            <div className="flex items-center gap-1 font-medium text-gray-700 bg-gray-50 px-1.5 py-0.5 rounded">
              <Star size={12} className="text-amber-500 fill-amber-500" />
              <span>{product.average_rating.toFixed(1)}</span>
            </div>
          ) : null}
        </div>

        {/* Title */}
        <Link href={`/products/${product.slug || product.id}`}>
          <h3 className="text-sm font-medium text-gray-900 line-clamp-1 hover:text-brand-800 transition">
            {product.title}
          </h3>
        </Link>

        {/* Fashion Tags (Fit & Fabric) */}
        <div className="flex items-center gap-2 mt-2">
          {product.fit_type && (
            <span className="badge-fit text-[10px]">{product.fit_type} FIT</span>
          )}
          {product.fabric && (
            <span className="text-[11px] text-gray-500 truncate max-w-[120px]">
              {product.fabric}
            </span>
          )}
        </div>

        {/* Pricing */}
        <div className="mt-3 pt-2 border-t border-gray-50 flex items-center justify-between">
          <div className="flex items-baseline gap-2">
            <span className="text-base font-bold text-gray-950">
              ₹{product.base_price?.toLocaleString("en-IN")}
            </span>
            {product.base_mrp > product.base_price && (
              <span className="price-mrp">
                ₹{product.base_mrp?.toLocaleString("en-IN")}
              </span>
            )}
          </div>
          {product.discount_percentage > 0 && (
            <span className="price-discount">
              {Math.round(product.discount_percentage)}% OFF
            </span>
          )}
        </div>
      </div>
    </div>
  );
};
