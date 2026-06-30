# Desislava Webshop — Portfolio Write-up Brief

> Transferred from a remote-desktop session 2026-06-27. Reference for upgrading
> `docs/Projects/Ecommerce/Desislava.html`. Not published (lives outside `docs/`).

## What to highlight in the write-up
Lead with the technical stack — it's impressive for a solo build. A **headless
WooCommerce storefront**: decoupled frontend, WordPress + PHP backend, MySQL
database, all containerized in Docker on WSL. Not a typical freelance site.

Key talking points:
- Headless architecture (frontend / backend separation)
- Dockerized environment with automated maintenance + health checks
- Stripe + Apple Pay integration
- Cloudflare Zero Trust / WARP for secure tunneling
- Solo, end-to-end ownership — infra, backend, frontend, payments

## Screenshots to take — in priority order
1. **Storefront** — hero section, a product page, and the mobile view (show it's polished).
2. **Checkout + Apple Pay button** — differentiator; many devs never integrate native pay buttons.
3. **Thank-you / confirmation page** — proves the full purchase flow works.
4. **Docker container dashboard** — `docker ps` output or Portainer; proves infra depth.
5. **WordPress admin → WooCommerce orders** — shows the backend stack.
6. **Stripe dashboard** — a blurred/anonymized payment record; shows real production usage.
7. **Cloudflare Zero Trust dashboard** — tunnel setup; proves the networking layer.

## Anonymize / blur
Customer names, email addresses, sensitive order amounts, and any visible API keys.

## Status / TODO
- [ ] Fold the highlights above into `Desislava.html` (richer technical write-up).
- [ ] Add 7 labeled screenshot placeholder slots (in the priority order above).
- [ ] Drop real screenshots in once captured (anonymized per the list).
