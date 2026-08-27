/* ==========================================================================
   JENNIES DIGITAL - CORE JAVASCRIPT
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initThemeToggle();
  initScrollNav();
  initMobileMenu();
  initScrollColorText();
  initLiveClock();
  initCopyEmail();
  initBlogFilter();
});

/* Preloader Controller */
function initPreloader() {
  const preloader = document.getElementById('sitePreloader');
  const bar = document.getElementById('preloaderBar');
  const percent = document.getElementById('preloaderPercent');
  const status = document.getElementById('preloaderStatus');
  if (!preloader) return;

  let current = 0;
  let isReady = false;

  const interval = setInterval(() => {
    if (!isReady && current < 88) {
      current += Math.floor(Math.random() * 7) + 3;
      if (current > 88) current = 88;
    } else if (isReady) {
      current += 8;
      if (current >= 100) {
        current = 100;
        clearInterval(interval);
        if (bar) bar.style.width = '100%';
        if (percent) percent.innerText = '100%';
        if (status) status.innerText = 'READY';
        setTimeout(() => {
          preloader.classList.add('loaded');
        }, 250);
      }
    }
    if (bar) bar.style.width = current + '%';
    if (percent) percent.innerText = current + '%';
  }, 35);

  function markReady() {
    isReady = true;
  }

  if (document.readyState === 'complete') {
    markReady();
  } else {
    window.addEventListener('load', markReady);
  }

  // Safety fallback after 1.6s
  setTimeout(markReady, 1600);
}

/* Theme Manager */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;

  const savedTheme = localStorage.getItem('jd_theme');
  const isLight = savedTheme === 'light';
  
  if (isLight) {
    document.documentElement.classList.add('light');
  } else {
    document.documentElement.classList.remove('light');
  }
  updateThemeIcon(isLight);

  themeToggleBtn.addEventListener('click', () => {
    const currentlyLight = document.documentElement.classList.toggle('light');
    localStorage.setItem('jd_theme', currentlyLight ? 'light' : 'dark');
    updateThemeIcon(currentlyLight);
  });
}

function updateThemeIcon(isLight) {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;
  themeToggleBtn.innerHTML = isLight
    ? `<svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 0 1 1-9-9Z"></path></svg>`
    : `<svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
}

/* Seamless Scroll Nav Transition */
function initScrollNav() {
  const header = document.querySelector('.site-header');
  if (!header || header.classList.contains('subpage-nav')) return;

  function onScroll() {
    if (window.scrollY > 24) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* Mobile Menu */
function initMobileMenu() {
  const btn = document.getElementById('mobileMenuBtn');
  const overlay = document.getElementById('mobileNavOverlay');
  if (!btn || !overlay) return;

  btn.addEventListener('click', () => {
    const isOpen = overlay.classList.toggle('open');
    btn.innerHTML = isOpen
      ? `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" x2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line></svg>`;
  });
}

/* Scroll Color Text Reveal */
function initScrollColorText() {
  const container = document.getElementById('scrollColorTextContainer');
  if (!container) return;

  const rawText = container.innerText.trim();
  const words = rawText.split(/\s+/);

  container.innerHTML = words.map(word => {
    if (word.includes('Jennifer') || word.includes('AI') || word.includes('SaaS') || word.includes('PMM') || word.includes('Product') || word.includes('marketing')) {
      return `<span class="word brand-highlight">${word}</span>`;
    }
    return `<span class="word">${word}</span>`;
  }).join(' ');

  const wordSpans = container.querySelectorAll('.word');

  function update() {
    const rect = container.getBoundingClientRect();
    const windowHeight = window.innerHeight;
    const startOffset = windowHeight * 0.85;
    const endOffset = windowHeight * 0.25;
    const progress = Math.min(Math.max((startOffset - rect.top) / (startOffset - endOffset), 0), 1);
    const highlightCount = Math.floor(progress * wordSpans.length);

    wordSpans.forEach((span, i) => {
      span.classList.toggle('highlighted', i <= highlightCount);
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  update();
}

/* Lagos Live Clock */
function initLiveClock() {
  const clock = document.getElementById('liveClockWidget');
  if (!clock) return;

  function tick() {
    const now = new Date();
    try {
      const timeStr = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Africa/Lagos',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      }).format(now);
      clock.textContent = `Lagos (GMT+1): ${timeStr}`;
    } catch (e) {
      clock.textContent = 'Lagos, Nigeria (GMT+1)';
    }
  }

  tick();
  setInterval(tick, 1000);
}

/* Copy Email */
function initCopyEmail() {
  const btn = document.getElementById('copyEmailBtn');
  if (!btn) return;

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    navigator.clipboard.writeText('jennifer@jenniesdigital.com').then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = '✓ Copied to clipboard!';
      setTimeout(() => {
        btn.innerHTML = orig;
      }, 2500);
    });
  });
}

/* Blog Filter for blog.html */
function initBlogFilter() {
  const tabs = document.querySelectorAll('.blog-tab-btn');
  const cards = document.querySelectorAll('.blog-static-card[data-category]');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter?.toLowerCase() || 'all';

      cards.forEach(card => {
        const cat = card.dataset.category?.toLowerCase() || '';
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
