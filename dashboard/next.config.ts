import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    // Local dev: proxy /api/* to FastAPI on :8000
    // Production (Vercel): rewrites are overridden by vercel.json which routes
    // /api/* to the Python serverless function at api/index.py
    if (process.env.NODE_ENV === "development") {
      const backend = process.env.BACKEND_URL || "http://localhost:8000";
      return [{ source: "/api/:path*", destination: `${backend}/api/:path*` }];
    }
    return [];
  },
};

export default nextConfig;
