# Myths to Disregard

Common misconceptions that waste hours of preparation work or cause unnecessary rejections. Each myth is corrected with the actual behavior.

## Myth 1: "You need 1500 successful API calls + <10% error rate before requesting Standard Access"

**Reality:** That requirement is for **Advanced Access**, not Standard.

- **Standard Access** (Marketing API): no minimum-call requirement. You just need to demonstrate correct usage in the screencast.
- **Advanced Access** (Marketing API): requires ~1500 successful calls with <10% error rate over 30 days, *plus* the standard review process.

The confusion comes from Meta's own dev community where someone got rejected for requesting Standard Access while being told the error-rate criterion applied — but the criterion link in the rejection email actually points to Advanced Access docs.

**What to do:** Submit Standard Access without "warming up" the API first. The warm-up matters only when you eventually request Advanced.

Sources: Meta dev thread #691016324664624; `/marketing-api/get-started/authorization` docs; cross-confirmed in Reddit r/MetaAppDevelopers discussions.

## Myth 2: "Screencast must show the OAuth login dialog"

**Reality:** Only required if your app actually uses OAuth.

For server-to-server apps with System User token:
- Meta's official "server-to-server sample submission" explicitly says screencasts are not strictly required for S2S apps.
- However, the form forces an upload, so the workaround is: upload a screencast that **explains** the S2S flow with captions, instead of trying to fake an OAuth screen.

The trap: skipping the explanation. If your video starts already-logged-in with no caption about why, reviewers reject as "unable to verify use case experience". Add an overlay in the first 4 seconds: `"Internal dashboard — auth via server-side System User token (no end-user OAuth)"`.

Source: Stack Overflow Q 51351881 referencing Meta's S2S sample submission; PostMoore case study; Reddit r/MetaAPIDevelopers.

## Myth 3: "Privacy Policy must be on the app's own domain"

**Reality:** Same business entity is what matters, not the same domain.

A Privacy Policy at `www.company.com/privacy` works fine for an app deployed at `app.company.com` or even `tools.company.com` — they share the parent domain and clearly belong to the same business.

What Meta actually checks:
1. URL responds 200 OK from a clean browser
2. Real privacy policy (not a 404 or "coming soon")
3. Mentions data collection and the same business entity name as the app

Source: Meta Business Help Center on App Review requirements; cross-validated in Reddit guides.

## Myth 4: "Need 2-5 minute screencast to look professional"

**Reality:** Meta has no published duration requirement. Focused beats long.

Approved internal-tool submissions exist with screencasts as short as 1 minute, as long as they:
- Show every requested permission in action
- Show real data
- Match the written description step-by-step

Padding the screencast with marketing tour footage doesn't help and can hurt (reviewers may flag as "generic screencast" if it doesn't focus on the specific permission flows).

Source: Meta Screen Recordings doc (no duration specified); PostMoore case study; this skill's own first-try approval used 1min07s.

## Myth 5: "English-only narration required"

**Reality:** UI can be non-English, but English captions/instructions help.

Meta's docs note that if your app isn't in English, flag it in the submission instructions. UI can be Portuguese/Spanish/etc. as long as the reviewer can follow the actions. Captions in English are strongly recommended because reviewers often watch muted.

Audio narration is **not** required at all. Many approved screencasts have no audio.

## Myth 6: "Site URL field should point to the app dashboard"

**Reality:** Site URL should be the **business marketing site**, not the app.

The Site URL is used by reviewers to validate that the entity exists and is a real business. The app dashboard URL goes inside the "Instructions for analyst" textbox, where you tell the reviewer how to access the actual product.

Mistake: putting `app.company.com` as Site URL when the marketing site is at `www.company.com`. Reviewer sees an empty/admin-only page and can't validate the business.

## Myth 7: "Meta will reject if you don't auto-detect every edge case in your code"

**Reality:** Meta reviews intent and demonstration, not code quality.

What they verify:
- Permission requested matches feature shown
- Screencast aligns with description
- Privacy policy works
- Business is real

They don't audit your code, your error handling, or your test coverage. Polishing those is good engineering hygiene but doesn't move the approval needle.
