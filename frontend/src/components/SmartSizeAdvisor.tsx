"use client";

import React, { useState } from "react";
import { Ruler, Sparkles, CheckCircle2, ChevronRight, AlertCircle } from "lucide-react";
import { api } from "@/lib/api";

interface SmartSizeAdvisorProps {
  productId: string;
  onSelectSize?: (size: string) => void;
}

export const SmartSizeAdvisor: React.FC<SmartSizeAdvisorProps> = ({
  productId,
  onSelectSize
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [chest, setChest] = useState<number | "">("");
  const [waist, setWaist] = useState<number | "">("");
  const [fitPref, setFitPref] = useState<string>("REGULAR");
  const [loading, setLoading] = useState(false);
  const [recommendation, setRecommendation] = useState<{
    recommended_size: string;
    confidence_score: number;
    fit_analysis: string;
  } | null>(null);

  const calculateSize = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await api.post(`/products/${productId}/size-advisor`, {
        chest_in: chest ? Number(chest) : undefined,
        waist_in: waist ? Number(waist) : undefined,
        fit_preference: fitPref
      });
      setRecommendation(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="border border-brand-200 bg-brand-50/50 rounded-xl p-4 my-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-brand-900 text-white flex items-center justify-center">
            <Ruler size={16} />
          </div>
          <div>
            <div className="text-xs font-bold text-brand-950 uppercase tracking-wider flex items-center gap-1">
              <span>Size & Fit Intelligence</span>
              <Sparkles size={12} className="text-amber-600" />
            </div>
            <p className="text-[11px] text-gray-600">Find your ideal fit with brand measurement charts.</p>
          </div>
        </div>

        <button
          type="button"
          onClick={() => setIsOpen(!isOpen)}
          className="text-xs font-semibold text-brand-800 underline hover:text-brand-950 transition"
        >
          {isOpen ? "Hide Advisor" : "Calculate My Size"}
        </button>
      </div>

      {isOpen && (
        <form onSubmit={calculateSize} className="mt-4 pt-4 border-t border-brand-200 space-y-3">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="block text-[11px] font-semibold text-gray-700 uppercase mb-1">
                Chest (Inches)
              </label>
              <input
                type="number"
                step="0.5"
                value={chest}
                onChange={(e) => setChest(e.target.value ? Number(e.target.value) : "")}
                placeholder="e.g. 38"
                className="w-full px-3 py-1.5 bg-white border border-gray-300 rounded-lg text-sm focus:ring-1 focus:ring-brand-500 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-gray-700 uppercase mb-1">
                Waist (Inches)
              </label>
              <input
                type="number"
                step="0.5"
                value={waist}
                onChange={(e) => setWaist(e.target.value ? Number(e.target.value) : "")}
                placeholder="e.g. 32"
                className="w-full px-3 py-1.5 bg-white border border-gray-300 rounded-lg text-sm focus:ring-1 focus:ring-brand-500 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-[11px] font-semibold text-gray-700 uppercase mb-1">
                Fit Preference
              </label>
              <select
                value={fitPref}
                onChange={(e) => setFitPref(e.target.value)}
                className="w-full px-3 py-1.5 bg-white border border-gray-300 rounded-lg text-sm focus:ring-1 focus:ring-brand-500 focus:outline-none"
              >
                <option value="SLIM">Slim Fit</option>
                <option value="REGULAR">Regular Fit</option>
                <option value="OVERSIZED">Oversized / Relaxed</option>
              </select>
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 bg-brand-950 text-white rounded-lg text-xs font-bold uppercase tracking-wider hover:bg-brand-800 transition"
          >
            {loading ? "Analyzing Dimensions..." : "Get Fit Recommendation"}
          </button>

          {recommendation && (
            <div className="mt-3 p-3 bg-white rounded-lg border border-emerald-200 flex items-start gap-3">
              <CheckCircle2 size={20} className="text-emerald-600 flex-shrink-0 mt-0.5" />
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <div className="text-xs font-bold text-gray-900">
                    Recommended Size: <span className="text-base text-brand-900 font-extrabold">{recommendation.recommended_size}</span>
                  </div>
                  <span className="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                    {Math.round(recommendation.confidence_score * 100)}% Confidence
                  </span>
                </div>
                <p className="text-[11px] text-gray-600 mt-1 leading-relaxed">
                  {recommendation.fit_analysis}
                </p>
                {onSelectSize && (
                  <button
                    type="button"
                    onClick={() => onSelectSize(recommendation.recommended_size)}
                    className="mt-2 text-xs font-bold text-brand-700 hover:text-brand-950 flex items-center gap-1"
                  >
                    Apply Size {recommendation.recommended_size} <ChevronRight size={14} />
                  </button>
                )}
              </div>
            </div>
          )}
        </form>
      )}
    </div>
  );
};
