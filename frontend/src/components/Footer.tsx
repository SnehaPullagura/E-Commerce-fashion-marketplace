"use client";

import React from "react";
import Link from "next/link";
import { ShieldCheck, Truck, RotateCcw, Sparkles } from "lucide-react";

export const Footer: React.FC = () => {
  return (
    <footer className="bg-brand-950 text-stone-300 pt-16 pb-12 border-t border-stone-800">
      {/* Guarantees bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12 border-b border-stone-800">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center sm:text-left">
          <div className="flex items-center gap-4 justify-center sm:justify-start">
            <div className="w-12 h-12 rounded-full bg-stone-900 border border-stone-800 flex items-center justify-center text-amber-400">
              <Sparkles size={22} />
            </div>
            <div>
              <div className="font-bold text-sm text-stone-100">Fashion DNA Curation</div>
              <div className="text-xs text-stone-400">Smart sizing & outfit engines</div>
            </div>
          </div>

          <div className="flex items-center gap-4 justify-center sm:justify-start">
            <div className="w-12 h-12 rounded-full bg-stone-900 border border-stone-800 flex items-center justify-center text-amber-400">
              <ShieldCheck size={22} />
            </div>
            <div>
              <div className="font-bold text-sm text-stone-100">100% Authentic Designers</div>
              <div className="text-xs text-stone-400">Direct from verified boutique brands</div>
            </div>
          </div>

          <div className="flex items-center gap-4 justify-center sm:justify-start">
            <div className="w-12 h-12 rounded-full bg-stone-900 border border-stone-800 flex items-center justify-center text-amber-400">
              <Truck size={22} />
            </div>
            <div>
              <div className="font-bold text-sm text-stone-100">Express Multi-Vendor Delivery</div>
              <div className="text-xs text-stone-400">Real-time courier waybill tracking</div>
            </div>
          </div>

          <div className="flex items-center gap-4 justify-center sm:justify-start">
            <div className="w-12 h-12 rounded-full bg-stone-900 border border-stone-800 flex items-center justify-center text-amber-400">
              <RotateCcw size={22} />
            </div>
            <div>
              <div className="font-bold text-sm text-stone-100">Hassle-Free 7-Day Returns</div>
              <div className="text-xs text-stone-400">Instant pickup & reverse logistics</div>
            </div>
          </div>
        </div>
      </div>

      {/* Main footer navigation */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid grid-cols-2 md:grid-cols-5 gap-8">
        <div className="col-span-2">
          <span className="font-serif text-2xl tracking-widest font-black text-stone-100 uppercase">
            ATELIER
          </span>
          <span className="block text-[10px] tracking-[0.25em] text-amber-400 font-semibold uppercase mt-0.5">
            Fashion Marketplace
          </span>
          <p className="text-xs text-stone-400 mt-4 max-w-sm leading-relaxed">
            The multi-vendor fashion ecosystem powered by Complete-the-Look Outfits, Smart Size Intelligence, and personalized stylist discovery.
          </p>
        </div>

        <div>
          <h4 className="text-xs font-bold uppercase tracking-wider text-stone-100 mb-4">Discover</h4>
          <ul className="space-y-2.5 text-xs text-stone-400">
            <li><Link href="/#women" className="hover:text-stone-100 transition">Women's Couture</Link></li>
            <li><Link href="/#men" className="hover:text-stone-100 transition">Men's Sartorial</Link></li>
            <li><Link href="/#occasions" className="hover:text-stone-100 transition">Occasion Shopping</Link></li>
            <li><Link href="/#collections" className="hover:text-stone-100 transition">Curated Collections</Link></li>
            <li><Link href="/#trending" className="hover:text-stone-100 transition">Fashion Trend Radar</Link></li>
          </ul>
        </div>

        <div>
          <h4 className="text-xs font-bold uppercase tracking-wider text-stone-100 mb-4">Marketplace</h4>
          <ul className="space-y-2.5 text-xs text-stone-400">
            <li><a href="/vendor" className="hover:text-stone-100 transition">Vendor Portal</a></li>
            <li><a href="/vendor/onboard" className="hover:text-stone-100 transition">Sell on Atelier</a></li>
            <li><a href="/admin" className="hover:text-stone-100 transition">Admin Command Center</a></li>
            <li><a href="/docs" target="_blank" className="hover:text-stone-100 transition">API Documentation</a></li>
          </ul>
        </div>

        <div>
          <h4 className="text-xs font-bold uppercase tracking-wider text-stone-100 mb-4">Customer Care</h4>
          <ul className="space-y-2.5 text-xs text-stone-400">
            <li><a href="#" className="hover:text-stone-100 transition">Order Tracking</a></li>
            <li><a href="#" className="hover:text-stone-100 transition">Size Guide & Advisor</a></li>
            <li><a href="#" className="hover:text-stone-100 transition">Returns & Exchanges</a></li>
            <li><a href="#" className="hover:text-stone-100 transition">Shipping Rates</a></li>
          </ul>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 border-t border-stone-800 text-center text-xs text-stone-500">
        © {new Date().getFullYear()} Atelier Fashion Marketplace Inc. All rights reserved.
      </div>
    </footer>
  );
};
