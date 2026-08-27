"use client";

import React, { useState } from "react";
import { X, Sparkles, Check, CheckCircle2 } from "lucide-react";
import { api } from "@/lib/api";

interface FashionDNAModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSaved?: () => void;
}

const STYLE_PERSONAS = [
  { id: "Minimalist", label: "Minimalist / Clean Aesthetic", desc: "Monochrome palettes, tailored cuts, subtle luxury" },
  { id: "Streetwear", label: "Streetwear / Urban", desc: "Oversized hoodies, graphic tees, cargo, sneakers" },
  { id: "Ethnic", label: "Contemporary Ethnic", desc: "Handcrafted silks, kurtas, fusion jackets, festive edit" },
  { id: "Formal", label: "Sharp & Formal", desc: "Blazers, crisp oxford shirts, tailored trousers" },
  { id: "Boho", label: "Bohemian & Chic", desc: "Flowing silhouettes, linen dresses, earthy aesthetics" },
  { id: "Athleisure", label: "Athleisure / Casual", desc: "Performance wear, joggers, breathable cottons" }
];

const COLORS = [
  { name: "Black", hex: "#111111" },
  { name: "Off-White", hex: "#FAF9F6" },
  { name: "Sage Green", hex: "#8A9A86" },
  { name: "Navy Blue", hex: "#1B2A4A" },
  { name: "Rust Orange", hex: "#C86D51" },
  { name: "Charcoal", hex: "#36454F" },
  { name: "Ruby Red", hex: "#9B111E" },
  { name: "Mustard Gold", hex: "#D4AF37" }
];

const OCCASIONS = ["Office", "Party", "Wedding", "Festival", "Casual", "Travel", "Date Night"];

export const FashionDNAModal: React.FC<FashionDNAModalProps> = ({
  isOpen,
  onClose,
  onSaved
}) => {
  const [selectedStyles, setSelectedStyles] = useState<string[]>(["Minimalist", "Streetwear"]);
  const [selectedColors, setSelectedColors] = useState<string[]>(["Black", "Sage Green"]);
  const [selectedOccasions, setSelectedOccasions] = useState<string[]>(["Office", "Party"]);
  const [priceSensitivity, setPriceSensitivity] = useState("MID_RANGE");
  const [savedSuccess, setSavedSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const toggleStyle = (id: string) => {
    setSelectedStyles(
      selectedStyles.includes(id)
        ? selectedStyles.filter((s) => s !== id)
        : [...selectedStyles, id]
    );
  };

  const toggleColor = (name: string) => {
    setSelectedColors(
      selectedColors.includes(name)
        ? selectedColors.filter((c) => c !== name)
        : [...selectedColors, name]
    );
  };

  const toggleOccasion = (name: string) => {
    setSelectedOccasions(
      selectedOccasions.includes(name)
        ? selectedOccasions.filter((o) => o !== name)
        : [...selectedOccasions, name]
    );
  };

  const handleSave = async () => {
    setLoading(true);
    try {
      await api.put("/users/me/fashion-dna", {
        style_personas: selectedStyles,
        favorite_colors: selectedColors,
        occasion_interests: selectedOccasions,
        price_sensitivity: priceSensitivity
      });
      setSavedSuccess(true);
      setTimeout(() => {
        setSavedSuccess(false);
        onClose();
        if (onSaved) onSaved();
      }, 1200);
    } catch (err) {
      console.error(err);
      // Even if unauthenticated in guest mode, close gracefully
      setSavedSuccess(true);
      setTimeout(() => {
        setSavedSuccess(false);
        onClose();
      }, 1000);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-gray-100 animate-in fade-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="sticky top-0 bg-white border-b border-gray-100 p-6 flex items-center justify-between z-10">
          <div className="flex items-center gap-2">
            <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-amber-500 to-orange-400 text-white flex items-center justify-center shadow-md">
              <Sparkles size={18} />
            </div>
            <div>
              <h3 className="font-serif text-xl font-bold text-gray-950">
                Your Fashion DNA Profile 🧬
              </h3>
              <p className="text-xs text-gray-500">
                Personalize recommendations, fit calculations & stylist feed
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-gray-100 hover:bg-gray-200 flex items-center justify-center text-gray-600 transition"
          >
            <X size={18} />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          {/* Step 1: Style Personas */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-gray-900 mb-3">
              1. What describes your personal style persona? (Select all that apply)
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {STYLE_PERSONAS.map((style) => {
                const isSelected = selectedStyles.includes(style.id);
                return (
                  <div
                    key={style.id}
                    onClick={() => toggleStyle(style.id)}
                    className={`p-3.5 rounded-xl border cursor-pointer transition-all ${
                      isSelected
                        ? "bg-amber-50/70 border-amber-400 text-amber-950 shadow-sm ring-1 ring-amber-400/40"
                        : "bg-gray-50/50 border-gray-200 text-gray-700 hover:border-gray-300"
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-semibold">{style.label}</span>
                      {isSelected && <Check size={16} className="text-amber-700 stroke-[3]" />}
                    </div>
                    <p className="text-[11px] text-gray-500 mt-1">{style.desc}</p>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Step 2: Favorite Color Palette */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-gray-900 mb-3">
              2. Your favorite signature colors
            </h4>
            <div className="flex flex-wrap gap-2.5">
              {COLORS.map((c) => {
                const isSelected = selectedColors.includes(c.name);
                return (
                  <button
                    key={c.name}
                    type="button"
                    onClick={() => toggleColor(c.name)}
                    className={`flex items-center gap-2 px-3 py-1.5 rounded-full border text-xs font-medium transition ${
                      isSelected
                        ? "border-black bg-black text-white shadow-sm"
                        : "border-gray-200 bg-white text-gray-700 hover:bg-gray-50"
                    }`}
                  >
                    <span
                      className="w-3 h-3 rounded-full border border-gray-300"
                      style={{ backgroundColor: c.hex }}
                    />
                    <span>{c.name}</span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Step 3: Occasions */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-gray-900 mb-3">
              3. Occasions you shop for most frequently
            </h4>
            <div className="flex flex-wrap gap-2">
              {OCCASIONS.map((occ) => {
                const isSelected = selectedOccasions.includes(occ);
                return (
                  <button
                    key={occ}
                    type="button"
                    onClick={() => toggleOccasion(occ)}
                    className={`px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider border transition ${
                      isSelected
                        ? "bg-brand-900 border-brand-900 text-white shadow-sm"
                        : "bg-gray-100 border-gray-200 text-gray-700 hover:bg-gray-200"
                    }`}
                  >
                    {occ}
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="sticky bottom-0 bg-white border-t border-gray-100 p-6 flex items-center justify-between">
          <button
            type="button"
            onClick={onClose}
            className="text-xs font-semibold text-gray-500 hover:text-black transition"
          >
            Cancel
          </button>

          <button
            onClick={handleSave}
            disabled={loading}
            className="px-8 py-3 bg-brand-950 hover:bg-brand-800 text-white rounded-xl text-xs font-bold uppercase tracking-wider shadow-lg flex items-center gap-2 transition"
          >
            {savedSuccess ? (
              <>
                <CheckCircle2 size={16} className="text-emerald-400" />
                Fashion DNA Updated!
              </>
            ) : (
              <>
                <Sparkles size={16} className="text-amber-400" />
                Save & Recalculate Feed
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
