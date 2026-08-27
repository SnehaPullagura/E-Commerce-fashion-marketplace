"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { CheckCircle2, Lock } from "lucide-react";

export default function CheckoutPage() {
  const [selectedPayment, setSelectedPayment] = useState("UPI");
  const [orderComplete, setOrderComplete] = useState(false);

  return (
    <div className="min-h-screen flex flex-col bg-[#FAF9F6]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-12">
        {orderComplete ? (
          <div className="bg-white p-10 rounded-3xl border border-emerald-200 text-center shadow-xl space-y-4">
            <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto">
              <CheckCircle2 size={36} />
            </div>
            <h1 className="font-serif text-3xl font-bold text-gray-900">Order Confirmed!</h1>
            <p className="text-xs text-gray-600 max-w-md mx-auto">
              Your 2-phase stock reservation has been committed and vendor fulfillment has begun.
            </p>
            <div className="p-4 bg-stone-50 rounded-xl font-mono text-xs max-w-xs mx-auto text-brand-950 font-bold">
              Order ID: FM-2026-98124
            </div>
            <Link
              href="/"
              className="inline-block px-8 py-3 bg-brand-950 text-white rounded-xl text-xs font-bold uppercase tracking-wider"
            >
              Return to Runway
            </Link>
          </div>
        ) : (
          <div className="space-y-8">
            <h1 className="font-serif text-3xl font-bold text-gray-900">Secure Multi-Vendor Checkout</h1>

            {/* Delivery Address */}
            <div className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">1. Delivery Address</h3>
              <div className="p-4 border-2 border-brand-950 bg-brand-50/40 rounded-xl text-xs space-y-1">
                <span className="font-bold text-brand-950">Zara Roy (Home)</span>
                <p className="text-gray-600">Penthouse 12B, Sky High Towers, Indiranagar, Bengaluru, Karnataka - 560038</p>
                <p className="text-gray-500">Phone: +91 9876543210</p>
              </div>
            </div>

            {/* Payment Method */}
            <div className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">2. Payment Method</h3>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs font-bold">
                {["UPI", "CARD", "NET_BANKING", "COD"].map((method) => (
                  <button
                    key={method}
                    type="button"
                    onClick={() => setSelectedPayment(method)}
                    className={`py-3 px-4 rounded-xl border text-center transition ${
                      selectedPayment === method
                        ? "bg-brand-950 text-white border-brand-950 shadow-md"
                        : "border-gray-200 text-gray-700 hover:bg-gray-50"
                    }`}
                  >
                    {method.replace("_", " ")}
                  </button>
                ))}
              </div>
            </div>

            <button
              onClick={() => setOrderComplete(true)}
              className="w-full py-4 bg-brand-950 hover:bg-brand-900 text-white rounded-xl text-xs font-bold uppercase tracking-widest flex items-center justify-center gap-2 shadow-xl"
            >
              <Lock size={16} /> Confirm & Pay ₹5,498.00
            </button>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}
