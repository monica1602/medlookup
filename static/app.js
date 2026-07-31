// MedLookup — frontend logic

const searchForm    = document.getElementById('searchForm');
const searchInput   = document.getElementById('searchInput');
const resultsSection = document.getElementById('resultsSection');
const quickAccess   = document.getElementById('quickAccess');
const suggestionsEl = document.getElementById('suggestions');

// ── Carregar sugestões de autocomplete ──
async function carregarSugestoes() {
  try {
    const res = await fetch('/api/lista');
    if (!res.ok) return;
    const data = await res.json();
    data.medicamentos.forEach(nome => {
      const opt = document.createElement('option');
      opt.value = nome;
      suggestionsEl.appendChild(opt);
    });
  } catch (_) { /* silencioso */ }
}

// ── Buscar medicamento ──
async function buscar(query) {
  if (!query.trim()) return;

  // Esconde quick-access e mostra loading
  quickAccess.style.display = 'none';
  resultsSection.innerHTML = `
    <div class="loading">
      <div class="spinner"></div>
      <span>Buscando <strong>${escapeHtml(query)}</strong>…</span>
    </div>`;

  try {
    const res = await fetch(`/api/buscar?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    if (!res.ok) {
      renderErro(data.erro || 'Erro ao buscar o medicamento.');
      return;
    }

    if (data.multiplos) {
      renderMultiplos(data.multiplos, query);
    } else {
      renderResultado(data);
    }
  } catch (e) {
    renderErro('Não foi possível conectar ao servidor. Tente novamente.');
  }
}

// ── Renderizar resultado único ──
function renderResultado(med) {
  const isGenericKeyword = (nome) => nome.toLowerCase().includes('genéric') || nome.toLowerCase().includes('generic');

  const cardsHTML = med.marcas.map(marca => {
    const ehGenerico = isGenericKeyword(marca.nome);
    return `
      <div class="brand-card ${ehGenerico ? 'generic' : ''}">
        ${ehGenerico ? '<span class="generic-tag">Genérico</span>' : ''}
        <div class="brand-name">${escapeHtml(marca.nome)}</div>
        <div class="brand-lab">🏭 ${escapeHtml(marca.laboratorio)}</div>
        <div class="brand-presentation">📦 ${escapeHtml(marca.apresentacao)}</div>
      </div>`;
  }).join('');

  resultsSection.innerHTML = `
    <div class="result-card">
      <div class="result-header">
        <div class="result-sci-name">💊 ${escapeHtml(med.nome_cientifico)}</div>
        <div class="result-meta">
          <span class="badge">🗂 ${escapeHtml(med.categoria)}</span>
          <span class="badge">🩺 ${escapeHtml(med.indicacao)}</span>
        </div>
      </div>
      <div class="result-body">
        <p class="result-count">
          ${med.total} opção${med.total !== 1 ? 'ões' : ''} encontrada${med.total !== 1 ? 's' : ''} no mercado
        </p>
        <div class="brands-grid">${cardsHTML}</div>
      </div>
    </div>
    <div style="text-align:center; margin-top:16px;">
      <button class="pill" id="novaConsulta">← Nova consulta</button>
    </div>`;

  document.getElementById('novaConsulta').addEventListener('click', resetar);
}

// ── Renderizar múltiplos resultados ──
function renderMultiplos(lista, query) {
  const itensHTML = lista.map((med, idx) => {
    const cardsHTML = med.marcas.map(marca => {
      const ehGenerico = marca.nome.toLowerCase().includes('genéric') || marca.nome.toLowerCase().includes('generic');
      return `
        <div class="brand-card ${ehGenerico ? 'generic' : ''}">
          ${ehGenerico ? '<span class="generic-tag">Genérico</span>' : ''}
          <div class="brand-name">${escapeHtml(marca.nome)}</div>
          <div class="brand-lab">🏭 ${escapeHtml(marca.laboratorio)}</div>
          <div class="brand-presentation">📦 ${escapeHtml(marca.apresentacao)}</div>
        </div>`;
    }).join('');

    return `
      <div class="multiple-item" id="item-${idx}">
        <div class="multiple-item-header" onclick="toggleItem(${idx})">
          <div>
            <div class="multiple-item-name">💊 ${escapeHtml(med.nome_cientifico)}</div>
            <div class="multiple-item-cat">${escapeHtml(med.categoria)} — ${escapeHtml(med.indicacao)}</div>
          </div>
          <span class="expand-icon">▼</span>
        </div>
        <div class="multiple-item-body">
          <p class="result-count" style="margin-bottom:14px;">
            ${med.total} opção${med.total !== 1 ? 'ões' : ''} no mercado
          </p>
          <div class="brands-grid">${cardsHTML}</div>
        </div>
      </div>`;
  }).join('');

  resultsSection.innerHTML = `
    <div class="multiple-header">
      Vários medicamentos encontrados para <strong>"${escapeHtml(query)}"</strong>. Selecione o desejado:
    </div>
    <div class="multiple-list">${itensHTML}</div>
    <div style="text-align:center; margin-top:20px;">
      <button class="pill" id="novaConsulta">← Nova consulta</button>
    </div>`;

  document.getElementById('novaConsulta').addEventListener('click', resetar);
}

// ── Renderizar erro ──
function renderErro(mensagem) {
  resultsSection.innerHTML = `
    <div class="error-card">
      <span class="error-icon">❌</span>
      <div class="error-text">
        <strong>Nenhum resultado encontrado.</strong><br>
        ${escapeHtml(mensagem)}
        <br><br>
        <button class="pill" onclick="resetar()" style="border-color:#fca5a5; color:#dc2626;">← Tentar novamente</button>
      </div>
    </div>`;
}

// ── Toggle item na lista múltipla ──
function toggleItem(idx) {
  const el = document.getElementById(`item-${idx}`);
  el.classList.toggle('open');
}

// ── Reset para estado inicial ──
function resetar() {
  searchInput.value = '';
  resultsSection.innerHTML = '';
  quickAccess.style.display = 'block';
  searchInput.focus();
}

// ── Escape HTML ──
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Event listeners ──
searchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  buscar(searchInput.value.trim());
});

// Quick-access pills
document.querySelectorAll('.pill[data-q]').forEach(btn => {
  btn.addEventListener('click', () => {
    const q = btn.dataset.q;
    searchInput.value = q;
    buscar(q);
  });
});

// ── Init ──
carregarSugestoes();
