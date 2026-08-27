import React, { useState } from "react";
import {
  LayoutDashboard,
  Package,
  Layers,
  ShoppingBag,
  DollarSign,
  Store,
  Plus,
  Truck,
  CheckCircle2,
  Clock,
  AlertTriangle,
  TrendingUp,
  Search,
  ChevronRight
} from "lucide-react";

export default function VendorApp() {
  const [activeTab, setActiveTab] = useState<"overview" | "products" | "inventory" | "orders" | "payouts">("overview");
  const [showAddProductModal, setShowAddProductModal] = useState(false);

  // Sample vendor orders state
  const [vendorOrders, setVendorOrders] = useState([
    {
      id: "so-1",
      sub_order_number: "FM-2026-98124-V1",
      items: "Handcrafted Silk Kurta Set (Size: M, Color: Ruby Red)",
      customer: "Priya Sharma (Bengaluru)",
      total: 3999.0,
      commission: 599.85,
      net: 3399.15,
      status: "CONFIRMED",
      tracking: null
    },
    {
      id: "so-2",
      sub_order_number: "FM-2026-94210-V1",
      items: "Minimalist Linen Mandarin Shirt (Size: L, Off-White)",
      customer: "Rahul Verma (Mumbai)",
      total: 1999.0,
      commission: 299.85,
      net: 1699.15,
      status: "SHIPPED",
      tracking: "BLU-892147102"
    }
  ]);

  const [inventoryList, setInventoryList] = useState([
    { sku: "KURTA-A-M", title: "Handcrafted Silk Kurta Set (M)", physical: 25, reserved: 2, available: 23, status: "IN_STOCK" },
    { sku: "KURTA-A-L", title: "Handcrafted Silk Kurta Set (L)", physical: 18, reserved: 1, available: 17, status: "IN_STOCK" },
    { sku: "NOIR-LIN-M", title: "Minimalist Linen Mandarin Shirt (M)", physical: 8, reserved: 3, available: 5, status: "LOW_STOCK" },
    { sku: "NOIR-LIN-L", title: "Minimalist Linen Mandarin Shirt (L)", physical: 30, reserved: 0, available: 30, status: "IN_STOCK" }
  ]);

  const handleGenerateWaybill = (orderId: string) => {
    const randomWaybill = `BLU-${Math.floor(100000000 + Math.random() * 900000000)}`;
    setVendorOrders(
      vendorOrders.map((o) =>
        o.id === orderId ? { ...o, status: "SHIPPED", tracking: randomWaybill } : o
      )
    );
  };

  return (
    <div className="flex h-screen bg-gray-100 font-sans">
      {/* Sidebar Navigation */}
      <aside className="w-64 bg-stone-950 text-white flex flex-col justify-between border-r border-stone-800">
        <div>
          {/* Brand header */}
          <div className="p-6 border-b border-stone-800">
            <h1 className="font-serif text-xl font-black tracking-widest uppercase text-amber-400">
              ATELIER
            </h1>
            <span className="text-[10px] uppercase tracking-wider text-stone-400 font-medium">
              Vendor Portal • House of Anita
            </span>
          </div>

          <nav className="p-4 space-y-1.5 text-xs font-semibold uppercase tracking-wider">
            <button
              onClick={() => setActiveTab("overview")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "overview" ? "bg-amber-400 text-black font-bold" : "text-stone-300 hover:bg-stone-900"
              }`}
            >
              <LayoutDashboard size={18} />
              Overview
            </button>

            <button
              onClick={() => setActiveTab("products")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "products" ? "bg-amber-400 text-black font-bold" : "text-stone-300 hover:bg-stone-900"
              }`}
            >
              <Package size={18} />
              Catalog & Variants
            </button>

            <button
              onClick={() => setActiveTab("inventory")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "inventory" ? "bg-amber-400 text-black font-bold" : "text-stone-300 hover:bg-stone-900"
              }`}
            >
              <Layers size={18} />
              Stock & Reservations
            </button>

            <button
              onClick={() => setActiveTab("orders")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "orders" ? "bg-amber-400 text-black font-bold" : "text-stone-300 hover:bg-stone-900"
              }`}
            >
              <ShoppingBag size={18} />
              Orders & Waybills
            </button>

            <button
              onClick={() => setActiveTab("payouts")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "payouts" ? "bg-amber-400 text-black font-bold" : "text-stone-300 hover:bg-stone-900"
              }`}
            >
              <DollarSign size={18} />
              Commissions & Payouts
            </button>
          </nav>
        </div>

        {/* Storefront Link */}
        <div className="p-4 border-t border-stone-800">
          <a
            href="http://localhost:3000"
            target="_blank"
            rel="noreferrer"
            className="flex items-center justify-between p-3 rounded-xl bg-stone-900 text-stone-300 hover:text-white text-xs font-semibold"
          >
            <span className="flex items-center gap-2">
              <Store size={16} className="text-amber-400" />
              View Storefront
            </span>
            <ChevronRight size={14} />
          </a>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top Navbar */}
        <header className="bg-white border-b border-gray-200 px-8 py-4 flex items-center justify-between">
          <h2 className="text-xl font-serif font-bold text-gray-900 capitalize">
            {activeTab === "overview" && "Dashboard Overview"}
            {activeTab === "products" && "Product Catalog & Variants"}
            {activeTab === "inventory" && "2-Phase Inventory Reservation Monitor"}
            {activeTab === "orders" && "Order Fulfillment & Courier Logistics"}
            {activeTab === "payouts" && "Commissions & Payout Statements"}
          </h2>

          <div className="flex items-center gap-4">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              Storefront Live (Active)
            </span>
            <button
              onClick={() => setShowAddProductModal(true)}
              className="px-4 py-2 bg-brand-950 hover:bg-brand-900 text-white rounded-lg text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 shadow-md transition"
            >
              <Plus size={16} />
              Add Fashion Item
            </button>
          </div>
        </header>

        {/* Scrollable View Area */}
        <main className="flex-1 overflow-y-auto p-8">
          {/* TAB 1: OVERVIEW */}
          {activeTab === "overview" && (
            <div className="space-y-8">
              {/* KPI Cards Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Gross Sales</div>
                  <div className="text-2xl font-black text-gray-900 mt-2">₹2,48,500</div>
                  <div className="text-xs text-emerald-600 font-semibold mt-1 flex items-center gap-1">
                    <TrendingUp size={12} /> +18.4% from last month
                  </div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Net Payouts (85%)</div>
                  <div className="text-2xl font-black text-amber-700 mt-2">₹2,11,225</div>
                  <div className="text-xs text-gray-500 mt-1">Platform Commission (15%)</div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Total Orders</div>
                  <div className="text-2xl font-black text-gray-900 mt-2">128</div>
                  <div className="text-xs text-gray-500 mt-1">1 pending shipment</div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Fulfillment SLA</div>
                  <div className="text-2xl font-black text-emerald-700 mt-2">99.2%</div>
                  <div className="text-xs text-emerald-600 font-semibold mt-1">Tier-1 Designer Badge</div>
                </div>
              </div>

              {/* Pending Action Orders Table */}
              <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="font-serif text-lg font-bold text-gray-900">Recent Customer Sub-Orders</h3>
                  <span className="text-xs font-semibold text-gray-500">Auto-split by marketplace</span>
                </div>

                <div className="overflow-x-auto">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-gray-50 border-b border-gray-200 uppercase text-gray-500">
                      <tr>
                        <th className="py-3 px-4">Sub-Order #</th>
                        <th className="py-3 px-4">Customer & Items</th>
                        <th className="py-3 px-4">Amount</th>
                        <th className="py-3 px-4">Status</th>
                        <th className="py-3 px-4">Action</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100 font-medium">
                      {vendorOrders.map((ord) => (
                        <tr key={ord.id} className="hover:bg-gray-50/80">
                          <td className="py-3.5 px-4 font-mono font-bold text-brand-950">{ord.sub_order_number}</td>
                          <td className="py-3.5 px-4">
                            <div className="font-semibold text-gray-900">{ord.items}</div>
                            <div className="text-gray-500 text-[11px]">{ord.customer}</div>
                          </td>
                          <td className="py-3.5 px-4 font-bold">₹{ord.total.toLocaleString("en-IN")}</td>
                          <td className="py-3.5 px-4">
                            <span
                              className={`px-2.5 py-1 rounded-full text-[10px] font-bold ${
                                ord.status === "CONFIRMED"
                                  ? "bg-amber-50 text-amber-800 border border-amber-200"
                                  : "bg-emerald-50 text-emerald-800 border border-emerald-200"
                              }`}
                            >
                              {ord.status}
                            </span>
                          </td>
                          <td className="py-3.5 px-4">
                            {ord.status === "CONFIRMED" ? (
                              <button
                                onClick={() => handleGenerateWaybill(ord.id)}
                                className="px-3 py-1.5 bg-brand-950 hover:bg-brand-800 text-white rounded-lg text-[11px] font-bold flex items-center gap-1"
                              >
                                <Truck size={12} /> Pack & Generate Waybill
                              </button>
                            ) : (
                              <span className="font-mono text-gray-600 text-[11px]">Waybill: {ord.tracking}</span>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: PRODUCTS */}
          {activeTab === "products" && (
            <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-serif text-lg font-bold text-gray-900">Your Fashion Catalog</h3>
                  <p className="text-xs text-gray-500">Manage products, variants, fit tags and brand size guides</p>
                </div>
                <button
                  onClick={() => setShowAddProductModal(true)}
                  className="px-4 py-2 bg-brand-950 text-white rounded-lg text-xs font-bold flex items-center gap-1"
                >
                  <Plus size={14} /> Add Product
                </button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4">
                <div className="border border-gray-200 rounded-xl p-4 flex gap-4">
                  <img
                    src="https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=300&q=80"
                    alt="Kurta"
                    className="w-24 h-32 object-cover rounded-lg"
                  />
                  <div className="flex-1">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-amber-700 bg-amber-50 px-2 py-0.5 rounded">
                      WEDDING • SILK
                    </span>
                    <h4 className="font-bold text-sm text-gray-900 mt-1">Handcrafted Silk Kurta Set</h4>
                    <p className="text-xs text-gray-500">SKU: KURTA-A • Fit: Regular Fit</p>
                    <div className="mt-2 text-sm font-bold text-gray-900">₹7,999 <span className="text-xs line-through text-gray-400 font-normal">₹11,999</span></div>
                    <div className="mt-3 flex gap-2">
                      <span className="text-[11px] px-2 py-0.5 bg-gray-100 rounded font-medium">Variants: S, M, L, XL</span>
                      <span className="text-[11px] px-2 py-0.5 bg-emerald-50 text-emerald-700 font-bold rounded">Live</span>
                    </div>
                  </div>
                </div>

                <div className="border border-gray-200 rounded-xl p-4 flex gap-4">
                  <img
                    src="https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=300&q=80"
                    alt="Shirt"
                    className="w-24 h-32 object-cover rounded-lg"
                  />
                  <div className="flex-1">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-brand-700 bg-brand-50 px-2 py-0.5 rounded">
                      OFFICE • LINEN
                    </span>
                    <h4 className="font-bold text-sm text-gray-900 mt-1">Minimalist Linen Mandarin Collar Shirt</h4>
                    <p className="text-xs text-gray-500">SKU: NOIR-LIN • Fit: Slim Fit</p>
                    <div className="mt-2 text-sm font-bold text-gray-900">₹1,999 <span className="text-xs line-through text-gray-400 font-normal">₹2,999</span></div>
                    <div className="mt-3 flex gap-2">
                      <span className="text-[11px] px-2 py-0.5 bg-gray-100 rounded font-medium">Variants: M, L</span>
                      <span className="text-[11px] px-2 py-0.5 bg-emerald-50 text-emerald-700 font-bold rounded">Live</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* TAB 3: INVENTORY */}
          {activeTab === "inventory" && (
            <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 space-y-4">
              <div>
                <h3 className="font-serif text-lg font-bold text-gray-900">2-Phase Inventory Reservation Engine</h3>
                <p className="text-xs text-gray-500">
                  Formula: <span className="font-mono font-bold text-brand-950">Available = Physical Stock - Active Checkout Hold</span> (Prevents overselling)
                </p>
              </div>

              <table className="w-full text-left text-xs mt-4">
                <thead className="bg-gray-50 border-b border-gray-200 uppercase text-gray-500">
                  <tr>
                    <th className="py-3 px-4">Variant SKU</th>
                    <th className="py-3 px-4">Product Name</th>
                    <th className="py-3 px-4">Physical Stock</th>
                    <th className="py-3 px-4">Reserved Hold</th>
                    <th className="py-3 px-4">Available to Sell</th>
                    <th className="py-3 px-4">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100 font-medium">
                  {inventoryList.map((item) => (
                    <tr key={item.sku} className="hover:bg-gray-50">
                      <td className="py-3 px-4 font-mono font-bold">{item.sku}</td>
                      <td className="py-3 px-4 text-gray-900">{item.title}</td>
                      <td className="py-3 px-4 font-bold">{item.physical}</td>
                      <td className="py-3 px-4 text-amber-700 font-bold">{item.reserved} held</td>
                      <td className="py-3 px-4 text-emerald-700 font-black text-sm">{item.available}</td>
                      <td className="py-3 px-4">
                        <span
                          className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                            item.status === "LOW_STOCK"
                              ? "bg-amber-100 text-amber-900"
                              : "bg-emerald-100 text-emerald-900"
                          }`}
                        >
                          {item.status.replace("_", " ")}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {/* TAB 4: ORDERS */}
          {activeTab === "orders" && (
            <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">Vendor Order Fulfillment Workflow</h3>
              <p className="text-xs text-gray-500">Process multi-vendor split orders, print waybill labels and courier handovers.</p>

              <div className="space-y-4 pt-2">
                {vendorOrders.map((ord) => (
                  <div key={ord.id} className="border border-gray-200 rounded-xl p-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                      <span className="font-mono font-bold text-xs text-brand-950">{ord.sub_order_number}</span>
                      <h4 className="font-bold text-sm text-gray-900 mt-1">{ord.items}</h4>
                      <p className="text-xs text-gray-500 mt-0.5">Shipping to: {ord.customer}</p>
                    </div>

                    <div className="flex items-center gap-4">
                      <div className="text-right">
                        <div className="text-sm font-bold text-gray-900">₹{ord.total}</div>
                        <div className="text-[11px] text-emerald-700 font-semibold">Net Payout: ₹{ord.net}</div>
                      </div>

                      {ord.status === "CONFIRMED" ? (
                        <button
                          onClick={() => handleGenerateWaybill(ord.id)}
                          className="px-4 py-2 bg-brand-950 text-white rounded-lg text-xs font-bold uppercase tracking-wider flex items-center gap-1.5"
                        >
                          <Truck size={14} /> Pack & Ship
                        </button>
                      ) : (
                        <div className="text-xs text-emerald-800 bg-emerald-50 border border-emerald-200 px-3 py-1.5 rounded-lg font-bold">
                          Waybill: {ord.tracking}
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* TAB 5: PAYOUTS */}
          {activeTab === "payouts" && (
            <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">Commission & Payout Reconciliation</h3>
              <p className="text-xs text-gray-500">Automatic settlement statements processed weekly into your verified bank account.</p>

              <div className="p-4 bg-brand-50 border border-brand-200 rounded-xl">
                <div className="flex justify-between items-center text-xs text-brand-950">
                  <span className="font-bold">Next Payout Schedule: Friday, August 28, 2026</span>
                  <span className="font-bold text-emerald-800">Bank Account: HDFC Bank (****1234)</span>
                </div>
              </div>

              <table className="w-full text-left text-xs mt-4">
                <thead className="bg-gray-50 border-b border-gray-200 uppercase text-gray-500">
                  <tr>
                    <th className="py-3 px-4">Payout Ref</th>
                    <th className="py-3 px-4">Period</th>
                    <th className="py-3 px-4">Gross Sales</th>
                    <th className="py-3 px-4">Commission (15%)</th>
                    <th className="py-3 px-4">Net Settled</th>
                    <th className="py-3 px-4">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100 font-medium">
                  <tr>
                    <td className="py-3 px-4 font-mono font-bold">PO-2026-AUG-W3</td>
                    <td className="py-3 px-4">Aug 14 - Aug 21, 2026</td>
                    <td className="py-3 px-4">₹1,12,000</td>
                    <td className="py-3 px-4 text-rose-600">-₹16,800</td>
                    <td className="py-3 px-4 font-bold text-emerald-800">₹95,200</td>
                    <td className="py-3 px-4"><span className="px-2 py-0.5 bg-emerald-100 text-emerald-900 rounded font-bold">SETTLED</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
