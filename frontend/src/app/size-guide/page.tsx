"use client";

import React from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { ArrowLeft } from "lucide-react";

export default function SizeGuidePage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header />

      <main className="flex-1 max-w-5xl w-full mx-auto px-4 py-12 space-y-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="font-serif text-3xl font-bold text-gray-950">Universal Size Guide & Advisor</h1>
            <p className="text-xs text-gray-500 mt-1">Cross-brand conversion charts and anthropometric measuring instructions.</p>
          </div>
          <Link href="/" className="text-xs font-bold uppercase tracking-wider text-brand-900 flex items-center gap-1">
            <ArrowLeft size={14} /> Back to Runway
          </Link>
        </div>

        <div className="bg-white p-8 rounded-3xl border border-gray-100 shadow-sm space-y-6">
          <h3 className="font-serif text-lg font-bold text-gray-900">Women's Apparel Standard Conversion</h3>
          <table className="w-full text-left text-xs">
            <thead className="bg-stone-50 border-b uppercase text-stone-500">
              <tr>
                <th className="py-3 px-4">Size</th>
                <th className="py-3 px-4">Bust (Inches)</th>
                <th className="py-3 px-4">Waist (Inches)</th>
                <th className="py-3 px-4">Hips (Inches)</th>
                <th className="py-3 px-4">UK Size</th>
                <th className="py-3 px-4">EU Size</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 font-medium text-gray-800">
              <tr><td className="py-3 px-4 font-bold">XS</td><td className="py-3 px-4">32 - 34</td><td className="py-3 px-4">24 - 26</td><td className="py-3 px-4">34 - 36</td><td className="py-3 px-4">6</td><td className="py-3 px-4">34</td></tr>
              <tr><td className="py-3 px-4 font-bold">S</td><td className="py-3 px-4">34 - 36</td><td className="py-3 px-4">26 - 28</td><td className="py-3 px-4">36 - 38</td><td className="py-3 px-4">8 - 10</td><td className="py-3 px-4">36 - 38</td></tr>
              <tr><td className="py-3 px-4 font-bold">M</td><td className="py-3 px-4">36 - 38</td><td className="py-3 px-4">28 - 30</td><td className="py-3 px-4">38 - 40</td><td className="py-3 px-4">12 - 14</td><td className="py-3 px-4">40 - 42</td></tr>
              <tr><td className="py-3 px-4 font-bold">L</td><td className="py-3 px-4">38 - 40</td><td className="py-3 px-4">30 - 32</td><td className="py-3 px-4">40 - 42</td><td className="py-3 px-4">16</td><td className="py-3 px-4">44</td></tr>
              <tr><td className="py-3 px-4 font-bold">XL</td><td className="py-3 px-4">40 - 43</td><td className="py-3 px-4">32 - 35</td><td className="py-3 px-4">42 - 45</td><td className="py-3 px-4">18</td><td className="py-3 px-4">46</td></tr>
            </tbody>
          </table>
        </div>
      </main>

      <Footer />
    </div>
  );
}
