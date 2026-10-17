const API = "";  // тот же origin

const productsEl = document.getElementById("products");
const tabsEl = document.querySelectorAll(".tab");
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");

let state = { category: "", search: "" };

// API
async function fetchProducts() {
    const params = new URLSearchParams();
    if (state.category) params.set("category", state.category);
    if (state.search)   params.set("search", state.search);

    const res = await fetch(`${API}/api/products?${params}`);
    if (!res.ok) throw new Error("Failed to load products");
    return res.json();
}

async function addToCart(productId) {
    const res = await fetch(`${API}/api/cart/items`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",     // обязательно — cookie session_id
        body: JSON.stringify({ product_id: productId, quantity: 1 }),
    });
    if (!res.ok) throw new Error("Failed to add to cart");
    return res.json();
}

//  Render 
function renderProducts(products) {
    if (!products.length) {
        productsEl.innerHTML = "<p>Ничего не найдено</p>";
        return;
    }
    productsEl.innerHTML = products.map(cardHTML).join("");
}

function cardHTML(p) {
    const badge = p.is_sale ? '<span class="badge-sale">SALE</span>' : "";
    const img = p.image_url
        ? `<img src="${p.image_url}" alt="${escapeHtml(p.title)}">`
        : "";
    return `
        <article class="card">
            ${badge}
            ${img}
            <h3 class="card-title">${escapeHtml(p.title)}</h3>
            <p class="card-price">${p.price} $</p>
            <button class="card-btn" data-id="${p.id}">В корзину</button>
        </article>`;
}

function escapeHtml(s) {
    return s.replace(/[&<>"']/g, c => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
}

//  Events 
tabsEl.forEach(tab => {
    tab.addEventListener("click", async () => {
        tabsEl.forEach(t => t.classList.remove("is-active"));
        tab.classList.add("is-active");
        state.category = tab.dataset.category;
        await load();
    });
});

searchForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    state.search = searchInput.value.trim();
    await load();
});

productsEl.addEventListener("click", async (e) => {
    const btn = e.target.closest(".card-btn");
    if (!btn) return;
    btn.disabled = true;
    try {
        await addToCart(Number(btn.dataset.id));
        btn.textContent = "Добавлено";
        setTimeout(() => {
            btn.textContent = "В корзину";
            btn.disabled = false;
        }, 1000);
    } catch {
        btn.textContent = "Ошибка";
        btn.disabled = false;
    }
});


async function load() {
    productsEl.innerHTML = "<p>Загрузка...</p>";
    try {
        const products = await fetchProducts();
        renderProducts(products);
    } catch (err) {
        productsEl.innerHTML = "<p>Ошибка загрузки</p>";
        console.error(err);
    }
}

load();