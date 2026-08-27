"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { Trash2, ArrowRight } from "lucide-react";

export default function CartPage() {
  const [couponCode, setCouponCode] = useState("");
  const [discountApplied, setDiscountApplied] = useState(false);

  const [cartItems, setCartItems] = useState([
    {
      id: "c1",
      title: "Black Velvet Bodycon Party Dress",
      vendor: "Maison Velvet",
      size: "M",
      color: "Midnight Black",
      price: 3499.0,
      mrp: 4999.0,
      qty: 1,
      image: "https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=300&q=80"
    },
    {
      id: "c2",
      title: "Minimalist Linen Mandarin Collar Shirt",
      vendor: "Noir Atelier",
      size: "L",
      color: "Off-White",
      price: 1999.0,
      mrp: 2999.0,
      qty: 1,
      image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=300&q=80"
    }
  ]);

  const removeItem = (id: string) => {
    setCartItems(cartItems.filter((i) => i.id !== id));
  };

  const subtotal = cartItems.reduce((acc, item) => acc + item.price * item.qty, 0);
  const totalMrp = cartItems.reduce((acc, item) => acc + item.mrp * item.qty, 0);
  const discount = discountApplied ? Math.round(subtotal * 0.15) : 0;
  const shipping = subtotal >= 999 ? 0.0 : 99.0;
  const finalTotal = subtotal - discount + shipping;

  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header cartCount={cartItems.length} />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <h1 className="font-serif text-3xl font-bold text-gray-950 mb-8">
          Your Shopping Bag ({cartItems.length} items)
        </h1>

        {cartItems.length === 0 ? (
          <div className="bg-white p-12 rounded-3xl text-center border border-gray-100 shadow-sm space-y-4">
            <p className="text-gray-500 text-sm">Your shopping bag is currently empty.</p>
            <Link
              href="/shop"
              className="inline-block px-6 py-3 bg-brand-950 text-white rounded-xl text-xs font-bold uppercase tracking-wider"
            >
              Explore Collection
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className="lg:col-span-2 space-y-4">
              {cartItems.map((item) => (
                <div key={item.id} className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex gap-6">
                  <img src={item.image} alt={item.title} className="w-24 h-32 object-cover rounded-xl" />
                  <div className="flex-1 flex flex-col justify-between">
                    <div>
                      <span className="text-[10px] uppercase font-bold text-brand-700 bg-brand-50 px-2 py-0.5 rounded">
                        Vendor: {item.vendor}
                      </span>
                      <h3 className="font-bold text-base text-gray-900 mt-1">{item.title}</h3>
                      <p className="text-xs text-gray-500 mt-0.5">Size: {item.size} • Color: {item.color}</p>
                    </div>

                    <div className="flex items-center justify-between border-t border-gray-100 pt-3">
                      <div className="flex items-baseline gap-2">
                        <span className="text-lg font-bold text-gray-950">₹{item.price.toLocaleString("en-IN")}</span>
                        <span className="text-xs line-through text-gray-400">₹{item.mrp.toLocaleString("en-IN")}</span>
                      </div>

                      <button onClick={() => removeItem(item.id)} className="text-gray-400 hover:text-rose-600 transition">
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <div className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6 h-fit">
              <h3 className="font-serif text-lg font-bold text-gray-900">Order Summary</h3>

              <div className="flex gap-2">
                <input
                  type="text"
                  value={couponCode}
                  onChange={(e) => setCouponCode(e.target.value.toUpperCase())}
                  placeholder="PROMO CODE"
                  className="flex-1 px-3 py-2 border rounded-xl text-xs uppercase font-mono"
                />
                <button
                  onClick={() => setDiscountApplied(true)}
                  className="px-4 py-2 bg-brand-950 text-white rounded-xl text-xs font-bold uppercase tracking-wider"
                >
                  Apply
                </button>
              </div>

              <div className="space-y-3 text-xs font-medium text-gray-600 pt-2 border-t border-gray-100">
                <div className="flex justify-between">
                  <span>Total MRP</span>
                  <span>₹{totalMrp.toLocaleString("en-IN")}</span>
                </div>
                <div className="flex justify-between text-emerald-700 font-bold">
                  <span>Catalogue Discount</span>
                  <span>-₹{(totalMrp - subtotal).toLocaleString("en-IN")}</span>
                </div>
                {discountApplied && (
                  <div className="flex justify-between text-emerald-700 font-bold">
                    <span>Coupon (FASHION15)</span>
                    <span>-₹{discount.toLocaleString("en-IN")}</span>
                  </div>
                )}
                <div className="flex justify-between">
                  <span>Delivery Fee</span>
                  <span>{shipping === 0 ? "FREE" : `₹${shipping}`}</span>
                </div>
                <div className="flex justify-between text-base font-extrabold text-gray-950 border-t border-gray-100 pt-3">
                  <span>Total Amount</span>
                  <span>₹{finalTotal.toLocaleString("en-IN")}</span>
                </div>
              </div>

              <Link
                href="/checkout"
                className="w-full py-4 bg-brand-950 hover:bg-brand-900 text-white rounded-xl text-xs font-bold uppercase tracking-widest flex items-center justify-center gap-2 shadow-lg transition"
              >
                Proceed to Checkout <ArrowRight size={16} />
              </Link>
            </div>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}
