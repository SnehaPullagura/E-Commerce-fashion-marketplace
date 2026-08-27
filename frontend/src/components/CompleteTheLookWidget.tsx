"use client";

import React, { useState } from "react";
import { Sparkles, Check, Plus, ShoppingBag, ArrowRight } from "lucide-react";

interface OutfitPiece {
  id: string;
  title: string;
  category_role: string;
  brand_name?: string;
  price: number;
  mrp: number;
  image_url?: string;
  fit_type: string;
  match_reason: string;
}

interface CompleteTheLookProps {
  outfitData: {
    main_product_id: string;
    main_product_title: string;
    outfit_style_theme: string;
    occasion: string;
    outfit_items: OutfitPiece[];
    bundle_total_mrp: number;
    bundle_discount_price: number;
    bundle_savings: number;
    bundle_discount_percentage: number;
  };
  onAddBundleToCart?: (itemIds: string[]) => void;
}

export const CompleteTheLookWidget: React.FC<CompleteTheLookProps> = ({
  outfitData,
  onAddBundleToCart
}) => {
  const [selectedItemIds, setSelectedItemIds] = useState<string[]>(
    outfitData.outfit_items.map((i) => i.id)
  );

  const toggleItem = (id: string) => {
    if (selectedItemIds.includes(id)) {
      if (selectedItemIds.length > 1) {
        setSelectedItemIds(selectedItemIds.filter((item) => item !== id));
      }
    } else {
      setSelectedItemIds([...selectedItemIds, id]);
    }
  };

  const selectedItems = outfitData.outfit_items.filter((i) => selectedItemIds.includes(i.id));
  const subtotal = selectedItems.reduce((acc, item) => acc + item.price, 0);
  const bundleDiscount = selectedItems.length >= 3 ? Math.round(subtotal * 0.10) : 0;
  const finalPrice = subtotal - bundleDiscount;

  return (
    <div className="bg-gradient-to-br from-stone-900 via-brand-950 to-neutral-900 text-white rounded-2xl p-6 sm:p-8 shadow-2xl border border-stone-800 my-10">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-stone-800 pb-6">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-400/10 border border-amber-400/20 text-amber-300 text-xs font-semibold tracking-wider uppercase mb-2">
            <Sparkles size={14} className="text-amber-400" />
            Complete-the-Look Engine
          </div>
          <h2 className="font-serif text-2xl sm:text-3xl font-bold tracking-tight text-stone-100">
            {outfitData.outfit_style_theme || "Curated Outfit Set"}
          </h2>
          <p className="text-stone-400 text-sm mt-1">
            Stylist-curated full ensemble harmonized for {outfitData.occasion} wear.
          </p>
        </div>

        {/* Bundle Savings Highlight */}
        <div className="bg-stone-800/80 backdrop-blur border border-stone-700/80 rounded-xl p-4 flex items-center gap-4">
          <div>
            <div className="text-xs text-stone-400">Bundle & Save</div>
            <div className="text-lg font-bold text-amber-400">
              Save ₹{outfitData.bundle_savings?.toLocaleString("en-IN")}
            </div>
          </div>
          <span className="bg-amber-400 text-black text-xs font-black px-2.5 py-1 rounded-md">
            10% OFF
          </span>
        </div>
      </div>

      {/* Outfit Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 my-6">
        {outfitData.outfit_items.map((item, idx) => {
          const isSelected = selectedItemIds.includes(item.id);
          const isMain = item.category_role === "MAIN_PIECE";

          return (
            <div
              key={item.id}
              onClick={() => !isMain && toggleItem(item.id)}
              className={`relative rounded-xl p-3 border transition-all cursor-pointer ${
                isSelected
                  ? "bg-stone-800/90 border-amber-400/60 shadow-lg"
                  : "bg-stone-900/50 border-stone-800 opacity-60 hover:opacity-100"
              }`}
            >
              {/* Role badge */}
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider text-stone-400 bg-stone-950/80 px-2 py-0.5 rounded">
                  {item.category_role.replace("_", " ")}
                </span>
                <div
                  className={`w-5 h-5 rounded-full flex items-center justify-center border transition ${
                    isSelected
                      ? "bg-amber-400 border-amber-400 text-black"
                      : "border-stone-600 bg-stone-900"
                  }`}
                >
                  {isSelected && <Check size={12} strokeWidth={3} />}
                </div>
              </div>

              {/* Image */}
              <div className="aspect-[3/4] w-full rounded-lg overflow-hidden bg-stone-950 mb-3">
                <img
                  src={item.image_url || "https://images.unsplash.com/photo-1596755094514-f87e34085b2c"}
                  alt={item.title}
                  className="w-full h-full object-cover object-top"
                />
              </div>

              {/* Details */}
              <h4 className="text-xs font-medium text-stone-200 line-clamp-1">
                {item.title}
              </h4>
              <div className="flex items-baseline gap-2 mt-1">
                <span className="text-sm font-bold text-stone-100">
                  ₹{item.price?.toLocaleString("en-IN")}
                </span>
                {item.mrp > item.price && (
                  <span className="text-[11px] text-stone-500 line-through">
                    ₹{item.mrp?.toLocaleString("en-IN")}
                  </span>
                )}
              </div>
              <p className="text-[10px] text-stone-400 mt-1 line-clamp-2 leading-relaxed">
                {item.match_reason}
              </p>
            </div>
          );
        })}
      </div>

      {/* Bottom CTA Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-4 border-t border-stone-800">
        <div className="flex items-baseline gap-3">
          <span className="text-xs text-stone-400 uppercase tracking-wider">Total Outfit:</span>
          <span className="text-2xl font-black text-stone-100">
            ₹{finalPrice?.toLocaleString("en-IN")}
          </span>
          {bundleDiscount > 0 && (
            <span className="text-xs text-emerald-400 font-semibold bg-emerald-950/60 border border-emerald-800 px-2 py-0.5 rounded">
              Saved extra ₹{bundleDiscount}
            </span>
          )}
        </div>

        <button
          onClick={() => onAddBundleToCart && onAddBundleToCart(selectedItemIds)}
          className="px-8 py-3.5 bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-black font-bold text-sm rounded-xl shadow-xl transition flex items-center justify-center gap-2"
        >
          <ShoppingBag size={18} />
          Add Complete Outfit to Cart ({selectedItemIds.length} Items)
        </button>
      </div>
    </div>
  );
};
