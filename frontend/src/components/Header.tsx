"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Search, ShoppingBag, Heart, User as UserIcon, Sparkles, Menu, X, ArrowRight } from "lucide-react";

interface HeaderProps {
  onOpenFashionDNA?: () => void;
  cartCount?: number;
  wishlistCount?: number;
  onSearchSubmit?: (query: string) => void;
}

export const Header: React.FC<HeaderProps> = ({
  onOpenFashionDNA,
  cartCount = 0,
  wishlistCount = 0,
  onSearchSubmit
}) => {
  const [searchQuery, setSearchQuery] = useState("");
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim() && onSearchSubmit) {
      onSearchSubmit(searchQuery.trim());
    }
  };

  const navCategories = [
    { name: "Women", href: "/#women" },
    { name: "Men", href: "/#men" },
    { name: "Occasions", href: "/#occasions" },
    { name: "Collections", href: "/#collections" },
    { name: "Trending", href: "/#trending" },
    { name: "Designers", href: "/#vendors" }
  ];

  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-100 transition-all">
      {/* Top Notification Bar */}
      <div className="bg-brand-950 text-white text-xs py-2 px-4 text-center font-medium tracking-wide flex justify-center items-center gap-2">
        <span>✨ Festive Edit Live: Enjoy up to 40% off on Curated Designer Collections</span>
        <span className="hidden md:inline font-mono bg-brand-800 px-2 py-0.5 rounded text-[11px]">USE CODE: FASHION15</span>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20 gap-4">
          
          {/* Logo */}
          <div className="flex-shrink-0 flex items-center gap-3">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-2 rounded-md text-gray-700 hover:text-black"
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
            <Link href="/" className="flex flex-col">
              <span className="font-serif text-2xl tracking-widest font-black text-brand-950 uppercase">
                ATELIER
              </span>
              <span className="text-[10px] tracking-[0.25em] text-brand-600 font-semibold uppercase -mt-1">
                Fashion Marketplace
              </span>
            </Link>
          </div>

          {/* Search Bar with Natural Language Fashion Extractor hint */}
          <div className="hidden md:flex flex-1 max-w-lg mx-4">
            <form onSubmit={handleSearch} className="w-full relative">
              <div className="relative flex items-center">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Try 'black velvet party dress' or 'oversized linen shirt'..."
                  className="w-full pl-11 pr-24 py-2.5 bg-gray-50 border border-gray-200 rounded-full text-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:bg-white transition-all"
                />
                <Search size={18} className="absolute left-4 text-gray-400" />
                <button
                  type="submit"
                  className="absolute right-1.5 px-4 py-1.5 bg-brand-950 hover:bg-brand-800 text-white rounded-full text-xs font-medium transition"
                >
                  Search
                </button>
              </div>
            </form>
          </div>

          {/* Right Action Icons */}
          <div className="flex items-center gap-3 sm:gap-5">
            {/* Fashion DNA Button */}
            <button
              onClick={onOpenFashionDNA}
              className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 text-amber-900 text-xs font-semibold hover:shadow-sm transition"
            >
              <Sparkles size={14} className="text-amber-600 animate-pulse" />
              <span className="hidden sm:inline">Fashion DNA</span>
            </button>

            {/* Wishlist */}
            <button className="relative p-2 text-gray-700 hover:text-black transition">
              <Heart size={22} />
              {wishlistCount > 0 && (
                <span className="absolute top-1 right-1 bg-rose-500 text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold">
                  {wishlistCount}
                </span>
              )}
            </button>

            {/* Shopping Cart */}
            <button className="relative p-2 text-gray-700 hover:text-black transition">
              <ShoppingBag size={22} />
              {cartCount > 0 && (
                <span className="absolute top-1 right-1 bg-brand-900 text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold">
                  {cartCount}
                </span>
              )}
            </button>

            {/* User Account / Vendor Portals */}
            <div className="flex items-center gap-2 border-l pl-3 border-gray-200">
              <a
                href="/vendor"
                className="hidden xl:inline-block text-xs font-medium text-gray-600 hover:text-black transition"
              >
                Sell on Atelier
              </a>
              <button className="p-2 text-gray-700 hover:text-black transition">
                <UserIcon size={22} />
              </button>
            </div>
          </div>
        </div>

        {/* Category Navigation Bar */}
        <nav className="hidden lg:flex justify-center space-x-10 py-3 border-t border-gray-100 text-xs tracking-wider font-semibold uppercase text-gray-700">
          {navCategories.map((item) => (
            <Link
              key={item.name}
              href={item.href}
              className="hover:text-brand-900 hover:underline decoration-2 underline-offset-8 transition"
            >
              {item.name}
            </Link>
          ))}
        </nav>
      </div>

      {/* Mobile Menu Drawer */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-gray-200 bg-white px-4 pt-3 pb-6 space-y-3">
          <form onSubmit={handleSearch} className="relative mb-4">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search fashion..."
              className="w-full pl-10 pr-4 py-2 border rounded-full text-sm bg-gray-50"
            />
            <Search size={18} className="absolute left-3 top-2.5 text-gray-400" />
          </form>
          {navCategories.map((item) => (
            <Link
              key={item.name}
              href={item.href}
              onClick={() => setMobileMenuOpen(false)}
              className="block py-2 text-sm font-medium text-gray-800 border-b border-gray-50"
            >
              {item.name}
            </Link>
          ))}
          <div className="pt-2">
            <button
              onClick={() => {
                setMobileMenuOpen(false);
                if (onOpenFashionDNA) onOpenFashionDNA();
              }}
              className="w-full flex items-center justify-between p-3 rounded-lg bg-amber-50 text-amber-950 text-sm font-semibold"
            >
              <span className="flex items-center gap-2">
                <Sparkles size={16} className="text-amber-600" />
                Customize Fashion DNA
              </span>
              <ArrowRight size={16} />
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
