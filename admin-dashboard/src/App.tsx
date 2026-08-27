import React, { useState } from "react";
import {
  Shield,
  Users,
  Store,
  Package,
  ShoppingBag,
  TrendingUp,
  Sliders,
  CheckCircle,
  XCircle,
  AlertCircle,
  Clock,
  Eye,
  Check,
  X,
  FileText
} from "lucide-react";

export default function AdminApp() {
  const [activeTab, setActiveTab] = useState<"metrics" | "vendors" | "products" | "settings" | "audit">("metrics");

  const [pendingVendors, setPendingVendors] = useState([
    {
      id: "v-1",
      businessName: "Kala Cotton Guild",
      owner: "Devi Prasad",
      email: "devi@kalacotton.org",
      city: "Kutch, Gujarat",
      gst: "24AAACG1234F1Z5",
      appliedDate: "2026-08-26",
      status: "PENDING",
      commissionRate: 15.0
    },
    {
      id: "v-2",
      businessName: "Sartorial Menswear Studio",
      owner: "Arman Malik",
      email: "arman@sartorialstudio.in",
      city: "New Delhi",
      gst: "07AAACS9876M1Z2",
      appliedDate: "2026-08-25",
      status: "PENDING",
      commissionRate: 12.0
    }
  ]);

  const [platformSettings, setPlatformSettings] = useState({
    defaultCommission: 15.0,
    freeShippingThreshold: 999.0,
    stockReservationHoldMinutes: 15,
    maintenanceMode: false
  });

  const handleApproveVendor = (id: string) => {
    setPendingVendors(
      pendingVendors.map((v) => (v.id === id ? { ...v, status: "APPROVED" } : v))
    );
  };

  const handleRejectVendor = (id: string) => {
    setPendingVendors(
      pendingVendors.map((v) => (v.id === id ? { ...v, status: "REJECTED" } : v))
    );
  };

  return (
    <div className="flex h-screen bg-stone-100 font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-stone-900 text-stone-300 flex flex-col justify-between border-r border-stone-800">
        <div>
          <div className="p-6 border-b border-stone-800">
            <div className="flex items-center gap-2">
              <Shield size={22} className="text-amber-400" />
              <h1 className="font-serif text-lg font-black tracking-widest uppercase text-white">
                ATELIER ADMIN
              </h1>
            </div>
            <span className="text-[10px] uppercase tracking-wider text-amber-400 font-semibold mt-1 block">
              Marketplace Command Center
            </span>
          </div>

          <nav className="p-4 space-y-1 text-xs font-semibold uppercase tracking-wider">
            <button
              onClick={() => setActiveTab("metrics")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "metrics" ? "bg-amber-400 text-black font-bold" : "hover:bg-stone-800 text-stone-300"
              }`}
            >
              <TrendingUp size={18} />
              Platform KPIs
            </button>

            <button
              onClick={() => setActiveTab("vendors")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "vendors" ? "bg-amber-400 text-black font-bold" : "hover:bg-stone-800 text-stone-300"
              }`}
            >
              <Store size={18} />
              Vendor KYC Approvals
            </button>

            <button
              onClick={() => setActiveTab("products")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "products" ? "bg-amber-400 text-black font-bold" : "hover:bg-stone-800 text-stone-300"
              }`}
            >
              <Package size={18} />
              Product Moderation
            </button>

            <button
              onClick={() => setActiveTab("settings")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "settings" ? "bg-amber-400 text-black font-bold" : "hover:bg-stone-800 text-stone-300"
              }`}
            >
              <Sliders size={18} />
              Platform Settings
            </button>

            <button
              onClick={() => setActiveTab("audit")}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                activeTab === "audit" ? "bg-amber-400 text-black font-bold" : "hover:bg-stone-800 text-stone-300"
              }`}
            >
              <FileText size={18} />
              Audit Logs
            </button>
          </nav>
        </div>

        <div className="p-4 border-t border-stone-800 text-[11px] text-stone-500">
          Super Admin Session • Active
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top Header */}
        <header className="bg-white border-b border-stone-200 px-8 py-4 flex items-center justify-between">
          <h2 className="text-xl font-serif font-bold text-gray-900 capitalize">
            {activeTab === "metrics" && "Marketplace Financial & Operations Overview"}
            {activeTab === "vendors" && "Vendor Onboarding & KYC Moderation"}
            {activeTab === "products" && "Product Catalog Moderation"}
            {activeTab === "settings" && "Marketplace Platform Configurations"}
            {activeTab === "audit" && "Security & Activity Audit Logs"}
          </h2>

          <div className="flex items-center gap-3">
            <span className="text-xs font-bold text-stone-600 bg-stone-100 px-3 py-1.5 rounded-lg">
              Env: Production • v1.0.0
            </span>
          </div>
        </header>

        {/* Scrollable View Area */}
        <main className="flex-1 overflow-y-auto p-8">
          {/* TAB 1: METRICS */}
          {activeTab === "metrics" && (
            <div className="space-y-8">
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Gross Merchandise Value</div>
                  <div className="text-3xl font-black text-gray-900 mt-2">₹1,48,50,000</div>
                  <div className="text-xs text-emerald-600 font-semibold mt-1">3,420 Paid Transactions</div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Net Commission Revenue</div>
                  <div className="text-3xl font-black text-amber-600 mt-2">₹22,27,500</div>
                  <div className="text-xs text-gray-500 mt-1">Avg 15.0% Marketplace Take-Rate</div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Verified Vendors</div>
                  <div className="text-3xl font-black text-gray-900 mt-2">48</div>
                  <div className="text-xs text-amber-700 font-semibold mt-1">2 applications pending review</div>
                </div>

                <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
                  <div className="text-xs font-semibold text-gray-500 uppercase">Conversion Rate</div>
                  <div className="text-3xl font-black text-emerald-700 mt-2">3.4%</div>
                  <div className="text-xs text-gray-500 mt-1">From Complete-the-Look Outfits</div>
                </div>
              </div>

              {/* Conversion Funnel Breakdown */}
              <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
                <h3 className="font-serif text-lg font-bold text-gray-900 mb-4">Fashion Discovery Conversion Funnel</h3>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-center">
                  <div className="p-4 bg-stone-50 rounded-xl border border-stone-200">
                    <div className="text-xs text-gray-500 uppercase font-semibold">1. Product Views</div>
                    <div className="text-2xl font-bold text-gray-900 mt-1">1,24,000</div>
                    <div className="text-[11px] text-gray-400 mt-1">100% Traffic</div>
                  </div>
                  <div className="p-4 bg-stone-50 rounded-xl border border-stone-200">
                    <div className="text-xs text-gray-500 uppercase font-semibold">2. Added to Cart</div>
                    <div className="text-2xl font-bold text-brand-950 mt-1">28,500</div>
                    <div className="text-[11px] text-emerald-600 font-semibold mt-1">23.0% Cart Rate</div>
                  </div>
                  <div className="p-4 bg-stone-50 rounded-xl border border-stone-200">
                    <div className="text-xs text-gray-500 uppercase font-semibold">3. Checkout Initiated</div>
                    <div className="text-2xl font-bold text-amber-700 mt-1">11,200</div>
                    <div className="text-[11px] text-amber-700 font-semibold mt-1">39.3% Step-Through</div>
                  </div>
                  <div className="p-4 bg-stone-50 rounded-xl border border-stone-200">
                    <div className="text-xs text-gray-500 uppercase font-semibold">4. Paid Orders</div>
                    <div className="text-2xl font-bold text-emerald-700 mt-1">4,216</div>
                    <div className="text-[11px] text-emerald-700 font-bold mt-1">3.4% Total Conversion</div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: VENDOR APPROVALS */}
          {activeTab === "vendors" && (
            <div className="bg-white rounded-2xl border border-stone-200 shadow-sm p-6 space-y-6">
              <div>
                <h3 className="font-serif text-lg font-bold text-gray-900">Pending Vendor KYC Applications</h3>
                <p className="text-xs text-gray-500">Verify business documents, legal tax identifiers and set commission rates.</p>
              </div>

              <div className="space-y-4">
                {pendingVendors.map((v) => (
                  <div key={v.id} className="border border-stone-200 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                      <div className="flex items-center gap-2">
                        <h4 className="font-bold text-base text-gray-900">{v.businessName}</h4>
                        <span
                          className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                            v.status === "APPROVED"
                              ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
                              : v.status === "REJECTED"
                              ? "bg-rose-50 text-rose-700 border border-rose-200"
                              : "bg-amber-50 text-amber-700 border border-amber-200"
                          }`}
                        >
                          {v.status}
                        </span>
                      </div>
                      <p className="text-xs text-gray-600 mt-1">Owner: {v.owner} ({v.email}) • {v.city}</p>
                      <div className="flex items-center gap-3 text-[11px] text-gray-500 mt-2">
                        <span>GST: <strong className="text-gray-800">{v.gst}</strong></span>
                        <span>Commission: <strong className="text-brand-950">{v.commissionRate}%</strong></span>
                        <span>Applied: {v.appliedDate}</span>
                      </div>
                    </div>

                    {v.status === "PENDING" && (
                      <div className="flex items-center gap-2">
                        <button
                          onClick={() => handleRejectVendor(v.id)}
                          className="px-4 py-2 border border-rose-300 text-rose-700 hover:bg-rose-50 rounded-lg text-xs font-bold transition flex items-center gap-1"
                        >
                          <X size={14} /> Reject
                        </button>
                        <button
                          onClick={() => handleApproveVendor(v.id)}
                          className="px-5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1 shadow-sm"
                        >
                          <Check size={14} /> Approve Store
                        </button>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* TAB 3: PRODUCT MODERATION */}
          {activeTab === "products" && (
            <div className="bg-white rounded-2xl border border-stone-200 shadow-sm p-6 space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">Product Quality & Moderation Queue</h3>
              <p className="text-xs text-gray-500">Ensure high-fashion imagery resolution, fabric transparency and accurate size charts.</p>

              <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-xl flex items-center gap-3 text-emerald-900 text-xs">
                <CheckCircle size={18} className="text-emerald-600" />
                <span>All submitted products meet quality resolution standards and brand verification requirements.</span>
              </div>
            </div>
          )}

          {/* TAB 4: SETTINGS */}
          {activeTab === "settings" && (
            <div className="bg-white rounded-2xl border border-stone-200 shadow-sm p-6 space-y-6 max-w-2xl">
              <h3 className="font-serif text-lg font-bold text-gray-900">Marketplace Configuration Settings</h3>

              <div className="space-y-4 text-xs font-medium">
                <div>
                  <label className="block text-gray-700 font-bold mb-1">
                    Default Marketplace Commission Rate (%)
                  </label>
                  <input
                    type="number"
                    value={platformSettings.defaultCommission}
                    onChange={(e) =>
                      setPlatformSettings({ ...platformSettings, defaultCommission: Number(e.target.value) })
                    }
                    className="w-full px-3 py-2 border rounded-lg"
                  />
                </div>

                <div>
                  <label className="block text-gray-700 font-bold mb-1">
                    Free Shipping Minimum Order Threshold (₹)
                  </label>
                  <input
                    type="number"
                    value={platformSettings.freeShippingThreshold}
                    onChange={(e) =>
                      setPlatformSettings({ ...platformSettings, freeShippingThreshold: Number(e.target.value) })
                    }
                    className="w-full px-3 py-2 border rounded-lg"
                  />
                </div>

                <div>
                  <label className="block text-gray-700 font-bold mb-1">
                    2-Phase Stock Reservation Hold Duration (Minutes)
                  </label>
                  <input
                    type="number"
                    value={platformSettings.stockReservationHoldMinutes}
                    onChange={(e) =>
                      setPlatformSettings({ ...platformSettings, stockReservationHoldMinutes: Number(e.target.value) })
                    }
                    className="w-full px-3 py-2 border rounded-lg"
                  />
                </div>

                <button className="px-6 py-2.5 bg-brand-950 text-white rounded-xl font-bold uppercase tracking-wider text-xs shadow-md">
                  Save Platform Settings
                </button>
              </div>
            </div>
          )}

          {/* TAB 5: AUDIT LOGS */}
          {activeTab === "audit" && (
            <div className="bg-white rounded-2xl border border-stone-200 shadow-sm p-6 space-y-4">
              <h3 className="font-serif text-lg font-bold text-gray-900">Security & Operational Audit Trail</h3>
              <table className="w-full text-left text-xs">
                <thead className="bg-stone-50 border-b uppercase text-stone-500">
                  <tr>
                    <th className="py-2.5 px-4">Action</th>
                    <th className="py-2.5 px-4">Resource</th>
                    <th className="py-2.5 px-4">Actor</th>
                    <th className="py-2.5 px-4">Timestamp</th>
                  </tr>
                </thead>
                <tbody className="divide-y font-medium text-stone-800">
                  <tr>
                    <td className="py-3 px-4 font-bold text-emerald-700">VENDOR_APPROVED</td>
                    <td className="py-3 px-4">Vendor: House of Anita (anita-dongre)</td>
                    <td className="py-3 px-4">SuperAdmin</td>
                    <td className="py-3 px-4 text-stone-500">2026-08-27 15:42 UTC</td>
                  </tr>
                  <tr>
                    <td className="py-3 px-4 font-bold text-brand-900">COMMISSION_UPDATED</td>
                    <td className="py-3 px-4">Commission set to 10.0%</td>
                    <td className="py-3 px-4">SuperAdmin</td>
                    <td className="py-3 px-4 text-stone-500">2026-08-27 15:44 UTC</td>
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
