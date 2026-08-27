import axios from "axios";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export const api = axios.create({
  baseURL: API_BASE,
  headers: {
    "Content-Type": "application/json",
  },
});

// Attach token if present in localStorage
api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("fashion_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    const sessionId = localStorage.getItem("fashion_session_id") || "guest_default_session";
    config.headers["X-Session-ID"] = sessionId;
  }
  return config;
});

// API helper functions
export const fetchHomeCatalog = async () => {
  try {
    const [productsRes, collectionsRes, categoriesRes, feedRes] = await Promise.all([
      api.get("/products?limit=8&is_trending=true"),
      api.get("/collections"),
      api.get("/categories/tree"),
      api.get("/recommendations/personalized-feed")
    ]);
    return {
      trendingProducts: productsRes.data.items || [],
      collections: collectionsRes.data || [],
      categories: categoriesRes.data || [],
      personalizedFeed: feedRes.data.items || []
    };
  } catch (err) {
    console.error("Error fetching home catalog", err);
    return {
      trendingProducts: [],
      collections: [],
      categories: [],
      personalizedFeed: []
    };
  }
};

export const searchCatalog = async (query: string, filters: any = {}) => {
  const params = new URLSearchParams({ q: query, ...filters });
  const res = await api.get(`/search?${params.toString()}`);
  return res.data;
};

export const getProductDetails = async (slugOrId: string) => {
  const [prodRes, ctlRes, sizeGuideRes] = await Promise.all([
    api.get(`/products/${slugOrId}`),
    api.get(`/recommendations/complete-the-look/${slugOrId}`).catch(() => ({ data: null })),
    api.get(`/reviews/product/${slugOrId}/summary`).catch(() => ({ data: null }))
  ]);
  return {
    product: prodRes.data,
    completeTheLook: ctlRes.data,
    reviewsSummary: sizeGuideRes.data
  };
};

export const getCart = async () => {
  const res = await api.get("/cart");
  return res.data;
};

export const addToCart = async (productId: string, variantId: string, quantity = 1) => {
  const res = await api.post("/cart/items", {
    product_id: productId,
    variant_id: variantId,
    quantity
  });
  return res.data;
};

export const applyCoupon = async (code: string, cartAmount: number) => {
  const res = await api.post("/coupons/apply", {
    code,
    cart_amount: cartAmount
  });
  return res.data;
};
