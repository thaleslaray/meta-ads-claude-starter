import { Suspense } from "react";
import Header from "./Header";
import Sidebar from "./Sidebar";

export default function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <Suspense fallback={null}>
        <Header />
      </Suspense>
      <div className="max-w-[1280px] mx-auto px-8 grid grid-cols-[220px_1fr] gap-12 pt-8 pb-20">
        <Suspense fallback={null}>
          <Sidebar />
        </Suspense>
        <main className="min-w-0">{children}</main>
      </div>
    </div>
  );
}
